import numpy as np
import ray

def calculate_potential(w1, w2):
    wp = 0
    if type(w1) == "Developer" and type(w2) == "Developer":
        skill_union = len(w1.skillset | w2.skillset)
        skill_xor = len(w1.skillset - w1.skillset)
        wp = skill_union * skill_xor

    bp = 0
    if w1.company == w2.company:
        bp = w1.bonus * w1.bonus

    return wp+bp

@ray.remote
def cost(map, workers, assignment):
    cost = 0
    edges = map["edges"]
    nodes = map["nodes"]

    for edge in edges:
        node1_id = edge[0]
        node2_id = edge[1]
        type1 = nodes[node1_id].type
        type2 = nodes[node2_id].type
        jobid1 = nodes[node1_id].id
        jobid2 = nodes[node2_id].id


        cost -= calculate_potential(workers[type1][assignment[type1][jobid1]],workers[type2][assignment[type2][jobid2]])

    return cost, assignment

def bongo_optimizer(map, workers,n_devs, n_manager, n_devstoassign, n_managerstoassign):
    num_cpus = 1
    iterations = 1000

    best_assignment_cost = 0
    best_assignment = {}

    ray.init(num_cpus = num_cpus, local_mode = False)
    for i in range(iterations):
        futures = []
        for j in range(num_cpus):
            devassign = np.random.choice(range(n_devs),n_devstoassign,replace=False )
            managerassign = np.random.choice(range(n_manager), n_managerstoassign, replace=False)
            assignment = {"developer":devassign,"manager":managerassign}
            futures.append(cost.remote(map,workers,assignment))
        for result in ray.get(futures):
            if result[0] < best_assignment_cost:
                best_assignment = result[1]
                best_assignment_cost = result[0]
                print("[Info] New best assignment costs " + str(result[0]))

    ray.shutdown()

    return best_assignment, best_assignment_cost



def optimize(map, workers):
    n_devs = len(workers["developer"])
    n_manager = len(workers["manager"])

    n_devstoassign = map["n_devstoassign"]
    n_managerstoassign = map["n_managerstoassign"]

    assignment, cost = bongo_optimizer(map,workers,n_devs,n_manager,n_devstoassign, n_managerstoassign)

    print("[Info] Best assignment costs "+str(cost))

    return assignment