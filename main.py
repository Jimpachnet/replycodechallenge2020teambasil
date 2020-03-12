from replyviech.util import calculate_potential, optimize
from replyviech.workers import Developer, Manager
from replyviech.parser import parse_input
import pickle

inputfile = "input/f_glitch.txt"
outputfile = "output/f_glitch.p"

edges, nodes, developers, managers, n_dev, n_manager = parse_input(inputfile)

map = {"edges": edges, "nodes": nodes}
map["n_devstoassign"] = n_dev
map["n_managerstoassign"] = n_manager

workers = {"developer": developers, "manager":managers}


assignment = optimize(map,workers)

pickle.dump( assignment, open( outputfile, "wb" ) )