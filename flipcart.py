from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/mobiles/pr?sid=tyy,4io&q=iphone&otracker=categorytree")

content = driver.page_source
soup = BeautifulSoup(content,features="lxml")

for a in soup.findAll('div',{'class':'_3pLy-c row'}):
	name=a.find('div', attrs={'class':'_4rR01T'})
	price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
	rating=a.find('div', attrs={'class':'_3LWZlK'})
	products.append(name.text)
	final_price = (price.text.split("₹"))[1]
	prices.append("Rs " +final_price)
	ratings.append(rating.text)
	

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
