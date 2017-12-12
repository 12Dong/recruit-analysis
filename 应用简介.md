# recruit-analysis
about recruit analysis and the data from zhilian
该应用分为四部分 1.招聘网址爬取get-url 2.应聘条件爬取spider 3.分词 divide-word 4.制作词云make-word-cloud
1.get-url 会将爬取到的 网址放置在url.txt中
2.spider 会将爬取的数据放在dataaa.txt中 现在爬取总量约为2w条 但是实际爬取约为5千 待以后爬虫理解更深一步 再再仔细研究一下
3.divide-word 会将dataaa中的数据进行分词 标准有stopwords停用词表 无实际意义的词 userdirt 新增词表 将一些我认为是一个意义的词加入分词词表
最终会将数据汇总到divide-word.txt中
4.make-word-cloud 前后制作四次词云 第三次被覆盖了Orz 根据词云内容增添停用词表stopwords和userdirt新增词表

                                                                                                                            2017/12/12更新
