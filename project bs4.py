from bs4 import BeautifulSoup
import requests
import csv

column_name = ['Name', 'Price', 'Rating']
csvfile = open('movie_data.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)
url = 'https://www.amazon.com/s?k=playstation+5&crid=2VS3308STMBD1&fbclid=IwAR2l7w-D-QB4PRPanxdtdcF_pNWMexX3Y-pZ6rWgSGmBU66Aht8YRjrAI0g&sprefix=playstation+5%2Caps%2C244&ref=nb_sb_noss_1'
HEADERS = {
    'agent-user':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
webpage = requests.get(url,headers = HEADERS)
soup = BeautifulSoup(webpage.text,'html.parser')
psfives = soup.find_all("div",class_="puisg-col-inner")
scraped_psfives = []
for psfive in psfives:
    try:
        name_element = psfive.find('span', class_="a-size-medium a-color-base a-textnormal")
        if name_element:
            name = name_element.get_text().strip()
            scraped_psfives.append(name)
    except AttributeError as e:
        print(f"error procesing element: {e}")

scraped_prices = []
for prices in psfives:
    try:
        price_element = prices.find("span", class_="s-price-whole")
        if price_element:
            price - price_element.get_text().strip()
            scraped_prices.append(price)
    except AttributeError as e:
        print(f"error procesing element: {e}")
        scraped_rating = []
        for ratings in psfives:
            try:
                rating_element = ratings.find("i", class_="a-icon a-icon-star-small a-star-small-4-5 aok-aling-bottom")
                if rating_element:
                    rating = rating_element.get_text().strip()
                    scraped_rating.append(rating)
            except AttributeError as e:
                print(f"error procesing element: {e}")

        for name, price, rating in zip(scraped_psfives, scraped_prices, scraped_rating):
            print(f"Name:{name}\nPrice: {price}\nRating: {rating}\n")
            csvwriter.writerow([name, price, rating])

csvfile.close()