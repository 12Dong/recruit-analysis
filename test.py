import jieba

word="熟悉Liux/Unix操作系统，具有良好的Shell/Perl/Python编程能力；"
data = jieba.cut(word,cut_all=False,HMM=True)
for i in data:
    print(i)