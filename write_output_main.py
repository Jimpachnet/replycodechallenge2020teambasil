import pickle
from replyviech.parser import parse_input

pickle_file = "output/c_soup2625.p"
input_file = "input/c_soup.txt"
output_file = "output/c_new.txt"



with open(pickle_file, 'rb') as f:
    data = pickle.load(f)

edges, nodes, developers, managers, n_dev, n_manager = parse_input(input_file)

from replyviech.serializer import write_output

print("Starting to write")
write_output(data, developers, managers, nodes, output_file)
print("Done.")


