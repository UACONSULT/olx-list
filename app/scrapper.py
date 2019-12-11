import requests
from bs4 import BeautifulSoup


def fetchItems(q):
    splitted_query = q.split()
    parsed_string = '-'.join(splitted_query)
    BASE_URL = f'https://www.olx.ua/list/q-{parsed_string}'

    webpage = requests.get(BASE_URL).text
    new_soup = BeautifulSoup(webpage, 'lxml')
    all_elements = new_soup.find_all('div', class_='offer-wrapper')

    result = []

    for element in all_elements:
        element_header = element.find('h3')        
        
        ELEMENT_TITLE = element_header.a.strong.text.strip()
        ELEMENT_LINK = element_header.a['href'].strip()

        try:
            ELEMENT_IMAGE = element.find('img')['src']
            splitted = ELEMENT_IMAGE.split(';')

            for q in splitted:
                if q.startswith('s='):
                    splitted.remove(q)
                    q ='s=400x400'
                    splitted.append(q)
                    ELEMENT_IMAGE = ';'.join(splitted)
        except:
            ELEMENT_IMAGE = None

        try:
            ELEMENT_PRICE = element.find('p', class_='price').text.strip()
        except:
            ELEMENT_PRICE = 'N/A'

        ELEMENT_CAT = element.find('small', class_='breadcrumb').text.strip()

        ELEMENT_DOA = element.find('i', {'data-icon':"clock"}).parent.text.strip()
        ELEMENT_LOCATION = element.find('i', {'data-icon':"location-filled"}).parent.text.strip() 

        bd = {
            'title' : ELEMENT_TITLE,
            'price' : ELEMENT_PRICE,
            'link' : ELEMENT_LINK,
            'cat' : ELEMENT_CAT,
            'image' : ELEMENT_IMAGE,
            'doa' : ELEMENT_DOA,
            'location' : ELEMENT_LOCATION,
        }

        result.append(bd)
    
    return result
