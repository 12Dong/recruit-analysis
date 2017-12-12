from urllib import request
from bs4 import BeautifulSoup

if __name__=="__main__":
    f = open("url.txt","wt")
    for i in range(1,91):
        url_base="http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&jl=%E4%B8%8A%E6%B5%B7&sm=0&isfilter=0&fl=538&isadv=0&sg=44b41480a5814a11b14c9379449b7f68&p="
        url = url_base+str(i)
        head={}
        head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        html_req = request.Request(url=url,headers=head)
        html_response = request.urlopen(html_req)
        html_content = html_response.read().decode()
        html_content_soup = BeautifulSoup(html_content,"lxml")
        url_list = html_content_soup.find_all("td",class_="zwmc")
        num = 1
        for url in url_list:
            #print(str(num))
            #print(url)
            #print(url.a.get("href"))
            f.write(url.a.get("href"))
            f.write("\n")
    #			<table cellpadding="0" cellspacing="0" width="853" class="newlist">
    f.close()