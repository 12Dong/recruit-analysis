import jieba
q = open("data.txt","rt")
f = open('divide-text.txt','wt')
text = q.read()
word_list = jieba.cut(text,cut_all=False,HMM=True)
for word in word_list:
    if len(word)>1:
        f.write(word+" ")
f.write("\n")
f.close()