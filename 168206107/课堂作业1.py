from collections import deque
def search(start,end,*ad):
    adict = list(ad)
    graph = {}
    adict.insert(0,start)
    for dot in range(0,len(adict)):
        graph[adict[dot]] = []
        for neighbour in range(0,len(adict)):
            xiangsidu = 0
            for i in range(0,len(adict[dot])):
                if adict[dot][i] == adict[neighbour][i]:
                    xiangsidu += 1 
                if xiangsidu == len(adict[dot])-1:
                    if adict[neighbour] not in graph.keys():
                        graph[adict[dot]].append(adict[neighbour])
    for key in graph.keys():
        graph[key] = list(set(graph[key]))
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    line = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is(person,end):
                while person != start:
                    for key,value in graph.items():
                        if  person in value:
                            line.append(key)
                            person = key
                line.reverse()
                return line
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
def person_is(this_word,end):
    if this_word == end:
        return True
    for letter in range(0,len(this_word)):
        panduan = this_word
        for i in range(0,27):
            panduan = panduan[0:letter] + chr(97+i) +panduan[letter+1:]
            if panduan == end:
                return True
    return False

print(search('hit','cog','hot','dot','dog','lot','log'))  
        
   
