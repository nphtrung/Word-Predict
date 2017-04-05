def trie(word,fre,mean,tree):
    pointer = tree

    if pointer[27] is None:
        pointer[27]=fre
        pointer[29]=1
    elif pointer[27]<fre:
        pointer[27]=fre
        pointer[30]=word
    pointer[29]+=1

    for char in word:
        index = int(ord(char)-97)
        if pointer[index] is None:

            pointer[index]=[ None for i in range(31)]
            pointer = pointer[index]
            pointer[27]=fre
            pointer[29]=1
            pointer[30]=word


        else:
            pointer = pointer[index]
            pointer[29]+=1
            if pointer[27] < fre:
                pointer[27] = fre
                pointer[30] = word

    pointer[26] = "$"
    pointer[28] = mean

tree = [None for i in range(31)]

f = open("Dictionary.txt","r")
for line in f:
    line = line.split()
    w = line[1]

    line = f.readline()
    line = line.split()
    fre = int(line[1])

    line = f.readline().split()
    mean =""
    for word in line[1:]:
        mean = mean + word +" "

    trie(w,fre,mean,tree)
    f.readline()


prefix = input("Enter a prefix: ")

while prefix != "***":
    tmp=tree
    if prefix == "":
        print(tree[30])
        for char in tree[30]:
            index = int(ord(char)-97)
            tmp = tmp[index]
        print("Definition: " + tmp[28]+ ".")
        print("There are " + str(tree[29]) +" words in the dictionary that has " + '"' + '"' + " as a prefix.")
    else:
        check = True
        for char in prefix:
            index = int(ord(char)-97)
            if tmp[index]==None:
                print("There is no word in the dictionary that has " + '"' + prefix + '"' + " as a prefix.")
                check=False
                break
            tmp = tmp[index]
        if check==True:
            target = tmp
            tmp =tree

            for char in target[30]:
                index = int(ord(char)-97)
                tmp = tmp[index]

            print("Auto-complete suggestion: " + target[30])
            print("Definition: " + tmp[28]+ ".")
            print("There are " + str(target[29]) +" words in the dictionary that has " + '"' +prefix+ '"' + " as a prefix.")
    prefix = input("Enter a prefix: ")