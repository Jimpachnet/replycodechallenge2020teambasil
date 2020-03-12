from replyviech.util import calculate_potential, optimize
from replyviech.workers import Developer, Manager
from replyviech.parser import parse_input


edges, nodes, developers, managers = parse_input("input/b_dream.txt")