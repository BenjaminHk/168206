def solution(start,end,*ad):
    adict = list(ad)
    adict.append(start)
    word_value_table = {}
    for word in adict:
         word_value_table[word] = []
         for i in range(0,len((word))):
             word_value_table[word].append(ord(word[i]))
    line =  []
    word = end
    searched = []
    while word != start:
        for key in word_value_table.keys():
            xiangsidu = 0
            xiangsidu_with_qidian = 0
            for i in range(0,len(word)):
                if word_value_table[key][i] == ord(start[i]):
                    xiangsidu_with_qidian += 1
                if word_value_table[key][i] == ord(word[i]):
                    xiangsidu += 1 
            if xiangsidu_with_qidian >= 2:
                line.remove(end)
                line.reverse()
                return line 
            if xiangsidu >= 2:
                line.append(word)
                word = key 
                word_value_table.pop(key)
                break
            if set(searched)==set(adict):
                return False
            searched.append(key)
            
print(solution('hit','cog','lot','dot','fog','log','hot'))
#将输入的路径生成一个字典，各个单词的各个字母作为一个数值列表，接着通过数值（也就是相似度）进行扫描最后输出。
