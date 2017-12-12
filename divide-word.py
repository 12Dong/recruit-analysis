import jieba
if __name__=="__main__":
    q = open("dataaa.txt", "rt")
    f = open('divide-text.txt', 'wt')
    file_path = "stopwords.txt"
    stopwords = [line.strip() for line in open(file_path, "r").readlines()]
    for text in q:
        word_list = jieba.cut(text, cut_all=False, HMM=True)
        for word in word_list:
            if word in stopwords:
                continue
            if len(word) > 1:
                f.write(word + " ")
        f.write("\n")
    f.close()