from wordcloud import WordCloud
import matplotlib.pyplot as plt
f = open("divide-text.txt","rt")
text = f.read()
font_path = "C:\Windows\Fonts\simfang.ttf"
wc = WordCloud(font_path=font_path,background_color="white",max_words=80,width=1000,height=860,margin=2)
wc.generate(text)
plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file("fourth.png")
