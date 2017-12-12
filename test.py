f = open("url.txt","rt")
num = 1
for text in f:
    print(num,text)
    num+=1
f.close()