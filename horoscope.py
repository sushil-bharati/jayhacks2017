from urllib.request import urlopen
from bs4 import BeautifulSoup

# Grab live horoscope from ganeshaspeaks.com (trust me, it is reliable :P)
def horoscopedaily(starsign):
    address='http://www.ganeshaspeaks.com/'+starsign+'/'+starsign+'-daily-horoscope.action'
    data = urlopen(address).read()
    soup = BeautifulSoup(data, "html.parser")
    tags = soup('span')
    return str(tags[7].contents[0])


