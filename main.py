from replyviech.util import calculate_potential, optimize
from replyviech.workers import Developer, Manager
from replyviech.parser import parse_input
from replyviech.serializer import write_output
import pickle

inputfile = "input/a_solar.txt"
outputfile = "output/a_solar"

edges, nodes, developers, managers, n_dev, n_manager = parse_input(inputfile)

map = {"edges": edges, "nodes": nodes}
map["n_devstoassign"] = n_dev
map["n_managerstoassign"] = n_manager

workers = {"developer": developers, "manager":managers}


assignment = optimize(map,workers)

write_output(assignment, developers, managers, nodes, outputfile+".txt")

pickle.dump( assignment, open( outputfile+".p", "wb" ) )
