
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
        node = None
        for key in self.graph.keys():
            if len(self.graph[key]) == 0:
                node = key
        lines = node
        for i in range(0,len(self.parents)):
           for key,value in self.parents.items():
               if key == node:
                   node = value
                   lines += '-'+node
        print(lines)
        
        
graph = {
        "乐谱":{
                "唱片":5,
                "海报":0
                },
        "唱片":{
                "吉他":15,
                "鼓":20
                },
        "海报":{
                "吉他":30,
                "鼓":35
                },
        "吉他":{
                "钢琴":20
                },
        "鼓":{
                "钢琴":10
                },
        "钢琴":{
                }
        }
        
infinity = float("inf")
costs = {
        "唱片":5,
        "海报":0,
        "吉他":infinity,
        "鼓":infinity,
        "钢琴":infinity
        }
parents = {
        "唱片":"乐谱",
        "海报":"乐谱",
        "吉他":None,
        "鼓":None,
        "钢琴":None
        }

question = Dijkstra_algorithm(graph,costs,parents)
question.begin()
question.print_line()
