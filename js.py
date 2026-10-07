# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# response=requests.get("https://books.toscrape.com/")
# print(response)
# soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
# names=soup.find_all('a',title=True)
# print(names)

# name=[]
# for i in names[0:10]:
#     result=i["title"]
#     name.append(result)
# print(name)

# price=soup.find_all('p',class_="price_color")
# print(price)
# prices=[]
# for i in price:
#     result=i.get_text()
#     prices.append(result)
# print(prices)
# result=[float(i.replace("£","")) for i in prices]
# print(result)
# images=soup.find_all('img',class_="thumbnail")
# print(images)
# image=[]
# for i in images:
#     data=i['src']
#     image.append(data)
# print(image)
# sample="https://books.toscrape.com/"
# result_2=[sample +i for i in image]
# print(result_2)
# df=pd.DataFrame()
# print(df)
# df["NAMES"]=name
# df["PRICE"]= result

# print(df)
import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, "html.parser")

names = soup.find_all("a", title=True)
name = [i["title"] for i in names[:10]]

price = soup.find_all("p", class_="price_color")
prices = [i.get_text() for i in price[:10]]
result = [float(i.replace("£", "")) for i in prices]

images = soup.find_all("img", class_="thumbnail")
image = [i["src"] for i in images[:10]]

sample = "https://books.toscrape.com/"
result_2 = [sample + i for i in image]

df = pd.DataFrame()
df["NAMES"] = name
df["PRICE"] = result
df["IMAGE"] = result_2

print(df)

df.to_csv("books.csv")