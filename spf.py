import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s]')

graph = {
    'start': {
        'a': 4,
        'b': 3,
        'c': 7
    },
    'a': {
        'b': 6,
        'd': 5
    },
    'b': {
        'd': 11,
        'c': 8
    },
    'c': {
        'd': 2,
        'e': 5
    },
    'd': {
        'end': 2,
        'e': 10
    },
    'e': {
        'end': 3
    },
    'end': {}
}

costs = dict()
costs['a'] = 4
costs['b'] = 3
costs['c'] = 7
costs['d'] = float("inf")
costs['e'] = float("inf")
costs['end'] = float("inf")

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = 'start'
parents['d'] = None
parents['e'] = None
parents['end'] = None


def spf():
    already_processed = []
    node = get_lowest_node_cost(nodes_costs=costs, processed_nodes=already_processed)
    while node:
        cost = costs[node]
        neighbors = graph[node].keys()
        for n in neighbors:
            new_cost = cost + graph[node][n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        already_processed.append(node)
        node = get_lowest_node_cost(nodes_costs=costs, processed_nodes=already_processed)


def get_lowest_node_cost(nodes_costs, processed_nodes):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs.keys():
        if nodes_costs[node] < lowest_cost and node not in processed_nodes:
            lowest_cost = nodes_costs[node]
            lowest_cost_node = node

    return lowest_cost_node


def prepare_output():
    path = []
    next_step = 'end'
    while next_step:
        step, next_step = get_step(a=next_step)
        if step:
            path.append(step)
    path.reverse()
    return path


def get_step(a):
    for i, v in parents.items():
        if i == a:
            if v != "start":
                path_string = "%s " % v \
                              + " " * 3 \
                              + " --> %s : %s points" % (i, graph[v][i])
            else:
                path_string = "%s --> %s : %s points" % (v, i, graph[v][i])
            return path_string, v
    return None, None


if __name__ == '__main__':
    spf()
    path = prepare_output()
    for string in path:
        logging.info(string)
    logging.info('Shortest path: %s points', costs['end'])
