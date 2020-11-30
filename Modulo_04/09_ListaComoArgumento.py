def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
    
lst = [5, 4, 3]
print(sumaDeLista(lst))