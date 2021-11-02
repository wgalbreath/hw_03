import argparse
import requests
from bs4 import BeautifulSoup
import json

def parse_itemssold(text): # you don't have to create doctests to parse this, but it helps to isolate each example
    '''
    Takes as input a string and returns the number of items sold, as specified in the string.
    
    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

def parse_price(text): # you don't have to create doctests to parse this, but it helps to isolate each example
    '''
    Takes as input a string and returns the price, as specified in the string.
    
    >>> parse_price('$38.99')
    3899
    >>> parse_price('$45.03 to $152.99')
    4503
    >>> parse_price('Free Shipping')
    0
    '''
    # accumulator = []
    numbers = ''
    if '$' not in text:
        return 0
    elif ' to ' in text:
        list = text.split()
        text = list[0]
    for char in text:
        if char in '1234567890':
            numbers += char
    return int(numbers)


# this 'if' statement says only run the code below when the python file is run "normally"
# where normally means not in the doctests 
if __name__ == '__main__': 


    # get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages',default=10)
    args = parser.parse_args()
    # print('args.search_term=',args.search_term)

    # list of all items found in all ebay webpages
    items = []

    # loop over the ebay webpages
    for page_number in range(1,int(args.num_pages)+1):
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + args.search_term + '&_sacat=11450&LH_TitleDesc=0&_pgn=' + str(page_number) + '&rt=nc'
        print('url=', url)

        # download the html
        r = requests.get(url)
        status = r.status_code
        # print('status=', status)
        html = r.text

        # process the html
        soup = BeautifulSoup(html, 'html.parser')

        # loop over the items in the page
        tags_items = soup.select('.s-item')
        for tag_item in tags_items: 

            # extract the name; compute the name
            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            # extract the free_returns; compute free returns
            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True
            
            # convert price dollars to cents
            priceCents = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                priceCents = parse_price(tag.text)

            
            # extract the item status
            status = None
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                status = tag.text
            
            # extract the item shipping
            shipping = None
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_price(tag.text)
                

            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)
            
            item = {
                'name': name,
                'price': priceCents,
                'status': status,
                'shipping': shipping,
                'free_returns': freereturns,
                'items_sold': items_sold,
            }
            items.append(item)

        print('len(tags_items)=',len(tags_items))
        print('len(items)=',len(items))



    # write  the json file FINISH
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))


