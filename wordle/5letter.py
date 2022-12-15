def compare_strings(a, b):
    count = 0 
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                count += 1 
    return count

def compareStrings(word, words):
    a = word
    wordsRet = [a]
    for i in range(len(words)):
        if compare_strings(word, words[i]) == 0:
            if compare_strings(a if len(wordsRet) < 2 else wordsRet[1], words[i]) == 0:
                if compare_strings(a if len(wordsRet) < 3 else wordsRet[2], words[i]) == 0:
                    if compare_strings(a if len(wordsRet) < 4 else wordsRet[3], words[i]) == 0:
                        a = words[i]
                        wordsRet.append(a)
                
    return(wordsRet)

with open ("C:/Users/emili/Desktop/python old programs/wordle/5letter.txt", "r") as myfile:
    data = myfile.read().splitlines()

data1 = []
for word in data:
    if len(set(word)) == len(word):
        data1.append(word)

for data in data1:
    if len(compareStrings(data, data1)) > 4:
        print(compareStrings(data, data1))
    
