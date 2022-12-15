import itertools

def per(n, steps=0):
    if len(str(n)) == 1:
        return steps
        
    steps += 1
    digits = [int(i) for i in str(n)]
    
    result = 1
    for j in digits:
        result *= j
    #print(result)
    return per(result, steps)


number = []
limit = 2
#most large number: 277777788888899
set1 = [2, 3, 5, 7, 8, 9]
for i in range(0, len(set1)+1):
    
    for subset in itertools.combinations(set1, i):
        if subset[1] != null:
            num = int(''.join(map(str,subset)))
        print(num)
    if per(i) >= limit:
        number.append((i, per(i)))
        
print(number)

