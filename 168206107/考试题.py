'''
A：我没有偷钻石。        -------非A                               
B：D就是罪犯。           -------D
C：B是盗窃这块钻石的罪犯。 -------B  
D：B有意诬陷我。        ------B诬陷，即非D
假定只有一个人说的是真话，编程序判断谁偷走了钻石。
所以题目的话可以简述成：
A:非A
B:D
C:B
D:非D
先假设所有人都没偷
'''
from copy import deepcopy
class Solution():
    def solution(self,*tuple):
        panduan = {}
        for people in tuple:
            panduan[people[0:1]] = people[2:]
        zhenzhibiao = deepcopy(panduan)
        conflict =  deepcopy(panduan)
        peoples = []
        for people in panduan.keys():
            peoples.append(str(people))
        for key in zhenzhibiao.keys():
            zhenzhibiao[key] =  float('inf')
            conflict[key] = 0
        for this_true in peoples:
            for people,talk in panduan.items():
                if this_true == people:
                    if len(talk) == 2:
                        if zhenzhibiao[talk[1:]] != 0:
                            conflict[talk[1:]] += 1
                        zhenzhibiao[talk[1:]] = 0
                    else :
                        if zhenzhibiao[talk] != 1:
                            conflict[talk] += 1
                        zhenzhibiao[talk] = 1
                    continue
                if len(talk) == 2:
                    if zhenzhibiao[talk[1:]] != 1:
                        conflict[talk[1:]] += 1
                    zhenzhibiao[talk[1:]] = 1
                else :
                    if zhenzhibiao[talk] != 0:
                        conflict[talk] += 1
                    zhenzhibiao[talk] = 0
            if max(conflict.values()) < 2 :
                people = []
                for key,value in zhenzhibiao.items():
                    if value == 1:
                          people.append(key)  
                if len(people)>1:
                    string = '若有多人偷则是：' + ','.join(people) 
                    print(string)
                else :
                    print('若一个人偷，则是：' + str(people[0]))                                                   
            for key in zhenzhibiao.keys():
                zhenzhibiao[key] =  float('inf')
                conflict[key] = 0
a = Solution()
a.solution('A:非A','B:D','C:B','D:非D')


