def write_output(assignment, original_devs, original_managers, nodes, outfile):
    developer = assignment['developer']
    manager = assignment['manager']
    dev_nodes = sorted([node for node in nodes if node.type == 'developer'], key=lambda node: node.id)
    man_nodes = sorted([node for node in nodes if node.type == 'manager'], key=lambda node: node.id)

    with open(outfile, "w") as f:
        for i, _ in enumerate(original_devs):
            ids = [id for id, x in enumerate(developer) if x == i]
            if ids:
                pos = dev_nodes[ids[0]].position
                f.write("{} {}\n".format(pos[0], pos[1]))
            else:
                f.write("X\n")

        for i, _ in enumerate(original_managers):
            ids = [id for id, x in enumerate(manager) if x == i]
            if ids:
                pos = man_nodes[ids[0]].position
                f.write("{} {}\n".format(pos[0], pos[1]))
            else:
                f.write("X\n")




