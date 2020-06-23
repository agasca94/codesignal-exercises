def areFollowingPatterns(strings, patterns):
    dic = {}
    for s, p in zip(strings, patterns):
        if s in dic and dic[s] != p: 
            return False
        dic[s] = p

    return len(dic) == len(set(dic.values()))



# Alternative solution using two hash-tables
def areFollowingPatterns(strings, patterns):
    dic = {}
    used = {}
    for s, p in zip(strings, patterns):
        if s in dic:
            if dic[s] != p: return False
        else:
            if p in used: return False
            
            used[p] = 1
            dic[s] = p
            
    return True
