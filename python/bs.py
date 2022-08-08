import bs4,requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#price')
    return elems[0].text.strip()



price = getAmazonPrice('https://www.amazon.com.au/Automate-Boring-Stuff-Python-Programming/dp/1593279922/ref=sr_1_2?crid=3CYN35V4A00ER&keywords=automate+the+boring+stuff+with+python&qid=1659936831&sprefix=automate+%2Caps%2C253&sr=8-2')
print('The price is ' + price)
