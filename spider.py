from urllib import request
import time
from bs4 import BeautifulSoup
if __name__=="__main__":
    q = open("url.txt","rt")
    f = open('dataaa.txt','wt')
    num = 0
    for tar_url in q:
        head={ }
        head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        try:
            http_req = request.Request(url=tar_url,headers=head)
            http_response = request.urlopen(http_req)
            http_content = http_response.read().decode()
            #print(http_content)
            http_content_soup = BeautifulSoup(http_content,'lxml')
            info = http_content_soup.find_all('div',class_="compaydetail-box")
            flag = False
            try:
                for i in info[0]:
                    try:
                        text = i.text
                        if flag :
                            f.write(text)
                            f.write("\n")
                        if(text=="任职要求：" or text=="任职要求" or text=="岗位要求：" or text=="岗位要求"
                           or text=="任职资格" or text=="任职资格：" or text=="要求" or text=="要求："
                           or text=="职位要求：" or text=="职位要求"):
                            flag = True
                            num += 1
                            f.write(str(num))
                            f.write("\n")
                            print("over")
                    except:
                        continue
            except:
                continue
            time.sleep(0.1)
        except:
            continue
    f.close()