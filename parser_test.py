from replyviech.parser import parse_input


edges, nodes, developers, managers = parse_input("input/a_solar.txt")

print(f"{len(developers)} Developers:")
for dev in developers:
    print(f"\t{dev}")

print(f"{len(managers)} Managers:")
for man in managers:
    print(f"\t{man}")

print(f"{len(nodes)} Nodes:")
for node in nodes:
    print(f"\t{node}")

print(f"{len(edges)} Edges:")
for edge in edges:
    print(f"\t{edge}")

print(f"Loaded {len(developers)} developers, {len(managers)} managers, {len(nodes)} nodes and {len(edges)} edges.")