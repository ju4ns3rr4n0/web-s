from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    new_height = 0


    while True:
        # Scroll down to bottom
        print(last_height)
        driver.execute_script("window.scrollTo("+str(new_height)+", document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

titulos=[] #List to store name of the product
anyos=[] #List to store price of the product
etiquetas=[] #List to store rating of the product
driver.get("https://www.justwatch.com/es/proveedor/filmin/peliculas")

driver.maximize_window()
scroll(driver, 10)
#print(driver.execute_script("window.scrollTo(0, document.body.scrollHeight)"))



content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
#print(soup)
titulos_soup = soup.find_all('img', class_ ='title-poster__image image-fade-in--out image-fade-in--in')

for t in titulos_soup:
	#print(t.attrs.get('alt'))
	titulos.append(t.attrs.get('alt'))

print(titulos)
print(len(titulos))
	

df = pd.DataFrame({'Titulo':titulos}) 
df.to_csv('peliculas.csv', index=False, encoding='utf-8')


driver.close()