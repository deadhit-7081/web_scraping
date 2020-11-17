import re
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get('https://keithgalli.github.io/web-scraping/webpage.html')
soup = bs(r.content,"html.parser")
print(soup.prettify())

#Grab all the links of social media

#1st method
links = soup.select("ul.socials a")
act_link = [link['href'] for link in links]
print(act_link)

#2nd method
ulist = soup.find("ul",attrs={"class":"socials"})
links = ulist.find_all("a")
act_link = [link['href'] for link in links]
print(act_link)

#3rd method
links = soup.select("li.social a")
act_link = [link['href'] for link in links]
print(act_link)

#Grabbing a table
table_class = soup.select("table.hockey-stats")[0]
print("Table Stats --")
print(table_class)
#getting table head
columns = table_class.find("thead").find_all("th")
print("Columns--")
print(columns)
columns_name = [c.string for c in columns]
print(columns_name)
#getting table row
table_rows = table_class.find("tbody").find_all("tr")
l =[]
for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

print("List--",l)
df = pd.DataFrame(l, columns=columns_name)

print(df.head())

#Removes the duplicates columns
df = df.T.drop_duplicates().T
print(df.head())

#Grab all fun fact that contains word is
fun_fact = soup.select("ul.fun-facts li")
print("Fun Fact--")
print(fun_fact)

fun_is = [fact.find_all(string=re.compile("is")) for fact in fun_fact]

fa = []
for fact in fun_fact:
    fl = fact.find(text=re.compile("is"))
    if(fl!=None):
        fa.append(fact.get_text())
print(fa)

#download an image from webpage
imag = soup.select("div.row div.column img")
print(imag)
#getting url of first image
imag_url = imag[0]['src']
print("Image url of 1st image-- ",imag_url)
full_url = url+imag_url
print(full_url)

img_data = requests.get(full_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
print("Image Saved")

#mystery file
file = soup.select("div.block a")
print(file)
rel_file = [file['href'] for file in file]
print(rel_file)

for f in rel_file:
    full_url = url+f
    page = requests.get(full_url)
    bs_page = bs(page.content,"html.parser")
    s_word = bs_page.find("p",attrs={"id":"secret-word"})
    print(s_word.get_text())