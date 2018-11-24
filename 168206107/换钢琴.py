class Dijkstra_algorithm():
    def __init__(self):
        self.graph = {}
        self.costs = {}
        self.parents = {}
        self.processed = [] 
        self.diagram_head_node = None
        self.diagram_tail_node = None
        
    def find_lowest_cost_node(self):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node           
    
    def handle(self,diagram):
        infinity = float('inf')
        head_nodes = []
        tail_nodes = []
        total_nodes = []
        for edge in diagram:                    #至57行找出图中的起点与终点
            if len(edge) !=1:
                head_nodes.append(edge[0])
                tail_nodes.append(edge[1])
                total_nodes.append(edge[0])
                total_nodes.append(edge[1])
        total_nodes = set(total_nodes)
        for node in total_nodes:
            if node not in head_nodes:
                self.diagram_tail_node = node
            if node not in tail_nodes:
                self.diagram_head_node = node
        for node in tail_nodes:                 #先为costs表与parents表赋予初值
            self.costs[node] = infinity
            self.parents[node] = None
        for edge in diagram:                
            self.graph[edge[0]] = {}
        for edge in diagram:                    #为graph表赋值，且遇到父节点是起点的为其costs表和parents表赋值
            if edge[0] != self.diagram_tail_node:
                self.graph[edge[0]][edge[1]] = edge[2]
            if edge[0] == self.diagram_head_node:
                self.costs[edge[1]] = edge[2]
                self.parents[edge[1]] = edge[0]
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
        node = self.diagram_tail_node
        lines =[ self.diagram_tail_node ]
        for i in range(0,len(self.parents)):
           for key,value in self.parents.items():
               if key == node:
                   node = value
                   lines.append(node)
        lines.reverse()
        lines = '->'.join(lines)
        print(lines)
        
question = Dijkstra_algorithm()
question.handle([["乐谱","唱片",5],["乐谱","海报",0],["唱片","吉他",15],["唱片","鼓",20],["海报","吉他",30],["海报","鼓",35],["吉他","钢琴",20],["鼓","钢琴",10],["钢琴"]])
question.print_line()
