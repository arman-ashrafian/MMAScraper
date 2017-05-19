import bs4 as bs
import urllib.request

URL = 'https://www.bestfightodds.com/'
class URLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def scrape():
    opener = URLopener()
    res = opener.open(URL).read()
    soup = bs.BeautifulSoup(res, 'lxml')

    div = soup.find_all('div',{'class':'table-header'})

    children = div[0].findChildren()

    eventName = children[0].text
    eventDate = children[1].text

    return (eventName, eventDate)
