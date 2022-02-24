from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests

from parser_shop.models import Product, Product_Info, Mentions


main_url = 'https://dermo-cosmetique.ru'
url = 'https://dermo-cosmetique.ru/catalog/'

    


HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
    }



def page_parse(links: list):
    for link in links:
        soup_page = requests.get(link, headers=HEADERS, params='',verify=False)
        page = BeautifulSoup(soup_page.text, "html.parser")
        try:
            company = page.find('div',class_='product-page-main__section').find('p').get_text()
        except AttributeError:
            company = "default_name"
        try:
            title = page.find('div',class_='product-page-main__section').find('h1').get_text()
        except AttributeError:
            title = "default_name"
        try:
            price = page.find('div',class_='product-page-main__section').find('p' , class_='product-page-main__price-current js-price').get_text()
        except AttributeError:
            price = "default_name"

        descriptions = page.findAll('div',class_='product-page-features__columns-item')
        try:
            description = descriptions[0].find('p', class_='product-page-features__mini-desc').get_text()
        except AttributeError:
            description = "default_name"
        
        try:
            applying = descriptions[1].find('p', class_='product-page-features__mini-desc').get_text()
        except AttributeError:
            applying = "default_name"
        try:
            composition = descriptions[2].find('p', class_='product-page-features__mini-desc').get_text()
        except AttributeError:
            composition = "default_name"
        try:
            country = descriptions[3].find('p', class_='product-page-features__mini-desc').get_text()
        except AttributeError:
            country = "default_name"
        mentions = page.findAll('div',class_='product-page-feedbacks__row')

        obj, created = Product.objects.update_or_create(
            url=link, 
            title=title,
            company=company,
            price=price,

            )

        obj_info, created = Product_Info.objects.update_or_create(
            product=obj, 
            description=description,
            applying=applying,
            composition=composition,
            country=country,

            )
            
        
        for mention in mentions:
            mention_mail = mention.find('p', class_='product-page-feedbacks__user-email').get_text()
            mention_text =  mention.find('p', class_='js-product-feedback product-page-feedbacks__message').get_text()
            obj_mention, created = Mentions.objects.update_or_create(
                product=obj, 
                mention_mail=mention_mail,
                mention_text=mention_text,

            )
            



def main_parser():
    links_on_product = []

    


    catalog_page = requests.get(url, headers=HEADERS, params='',verify=False)

    soup = BeautifulSoup(catalog_page.text, "html.parser")

    allNews = soup.find('div', class_='products-list').findAll('div', class_='product-card')
    count = 0 
    for link in allNews:
        my_link = link.find('a', class_='product-card__pic-wrapper').get('href')
        links_on_product.append(main_url+my_link)
        count +=1


    page_parse(links_on_product)






class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        main_parser()


