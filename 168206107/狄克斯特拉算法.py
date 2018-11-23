
class Dijkstra_algorithm():
    def __init__(self,g,c,p):
        self.graph = g
        self.costs = c
        self.parents = p
        self.processed = []   
        
    def find_lowest_cost_node(self):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node           
    
    def begin(self):
        node =  self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                new_costs = cost + neighbors[n]
                if self.costs[n] > new_costs:
                    self.costs[n] = new_costs
                    self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()      
            
    def print_line(self):
        lines = 'start'
        previous_node = 'start'
        for i in range(0,len(self.parents)):
            for key,value in self.parents.items():
                if value == previous_node:
                    lines += ("->"+ key)
                    previous_node = key
        print(lines)
