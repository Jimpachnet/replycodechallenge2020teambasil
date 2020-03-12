import pickle
from replyviech.parser import parse_input

pickle_file = "output/d_maelstrom16862.p"
input_file = "input/d_maelstrom.txt"
output_file = "output/d.txt"

with open(pickle_file, 'rb') as f:
    data = pickle.load(f)

edges, nodes, developers, managers, n_dev, n_manager = parse_input(input_file)

from replyviech.serializer import write_output

print("Starting to write")
write_output(data, developers, managers, nodes, output_file)
print("Done.")


