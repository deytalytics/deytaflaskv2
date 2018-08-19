from urllib.request import urlopen
from bs4 import BeautifulSoup
ifile=open("links.txt","r")
print('<HTML>')
print('<BODY>')
for line in ifile:
                title=""
 #               try:
                soup=BeautifulSoup(urlopen(line),'lxml')
                title=soup.title.string.strip()
 #               except:
 #                               pass
                link=line.strip()
                if title=="":
                                if ('://www.') in line:
                                                www_addr=link.split('://www.')
                                else:
                                                www_addr=link.split('://')
                                text=www_addr[1].split('.')
                                title=text[0]
                print('<br><a href="'+link+'">'+title+'</a>')
print('</BODY>')
print('</HTML>')
