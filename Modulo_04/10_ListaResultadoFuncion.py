def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))