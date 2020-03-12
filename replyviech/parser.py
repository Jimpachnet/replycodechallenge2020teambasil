from itertools import islice
from .workers import Developer, Manager


class Node:
    def __init__(self, type, id, gid, position):
        self.type = type
        self.id = id
        self.gid = gid
        self.position = position

    def __str__(self):
        return f"Node(type={self.type}, id={self.id}, gid={self.gid}, position={self.position})"


def create_office(lines):
    nodes = []
    edges = []
    dev_id, man_id, id = 0, 0, 0
    last_row = None
    connect_to_prev = False
    for i, line in enumerate(lines):
        new_row = []

        def connect():
            if connect_to_prev:
                edges.append((id - 1, id))
            if last_row is not None:
                above = [node for node in last_row if node.position[0] == j]
                if above:
                    edges.append((above[0].gid, id))

        for j, c in enumerate(line):
            if c == '#':
                connect_to_prev = False
            elif c == 'M':
                new_row.append(Node(
                    type='M',
                    id=man_id,
                    gid=id,
                    position=(j, i)))
                connect()
                connect_to_prev = True
                id += 1
                man_id += 1
            elif c == '_':
                new_row.append(Node(
                    type='_',
                    id=dev_id,
                    gid=id,
                    position=(j, i)))
                connect()
                connect_to_prev = True
                dev_id += 1
                id += 1
            else:
                raise ValueError("Input file format wrong")
        nodes.extend(new_row)
        last_row = new_row

    return nodes, edges


def parse_input(path):
    with open(path) as f:
        office_dim = [*map(lambda x: int(x), next(f).split(' '))]
        nodes, edges = create_office(next(f).strip() for _ in range(office_dim[1]))
        n_developers = int(next(f))
        developers = [Developer.parse(next(f)) for _ in range(n_developers)]
        n_managers = int(next(f))
        managers = [Manager.parse(next(f)) for _ in range(n_managers)]

    return edges, nodes, developers, managers