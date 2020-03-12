from replyviech.util import calculate_potential, optimize
from replyviech.workers import Developer, Manager
from replyviech.parser import parse_input
from replyviech.serializer import write_output
import pickle
import numpy as np
import uuid
import copy

level = 'e'
prefix = dict(
        a="a_solar",
        b="b_dream",
        c="c_soup",
        d="d_maelstrom",
        e="e_igloos",
        f="f_glitch")[level]
inputfile = "input/" + prefix + ".txt"
outputfile = "output/" + prefix

edges, nodes, developers, managers, n_dev, n_manager = parse_input(inputfile)

managers_before=copy.deepcopy(managers)

if level == 'c':
    for i in range(618):
        newmanager = Manager(company=str(uuid.uuid4()),bonus=0)
        managers.append(newmanager)

if level == 'e':
    for i in range(8699-6549):
        newmanager = Manager(company=str(uuid.uuid4()),bonus=0)
        managers.append(newmanager)


map = {"edges": edges, "nodes": nodes}
map["n_devstoassign"] = n_dev
map["n_managerstoassign"] = n_manager

workers = {"developer": developers, "manager":managers}


assignment = optimize(map,workers, developers, managers, nodes, outputfile)

write_output(assignment, developers, managers_before, nodes, outputfile+".txt")

pickle.dump( assignment, open( outputfile+".p", "wb" ) )
