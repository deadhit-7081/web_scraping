import re
import requests
#Requests allows you to send HTTP/1.1 requests extremely easily
from bs4 import BeautifulSoup as bs
#Beautiful Soup is a library that makes it easy to scrape information from web pages.
# It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching,
# and modifying the parse tree.

#Load the web page content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
#r.content contains the content of the web page
soup = bs(r.content)
print(soup.prettify())
#getting the first header
first_header = soup.find("h2")
print("Header - ")
print(first_header)
header = soup.find_all("h2")
print("All header -")
print(header)
#searching multiple things
multiple = soup.find_all(["h1","h2"])
print("Multiple Search --")
print(multiple)
#finding a para with specific Id
para = soup.find_all("p",attrs={"id":"paragraph-id"})
print("Para with specific Id--")
print(para)
#nesting find/find_all
body = soup.find("body")
print("Body --",body)
#finding a div tag inside body
div = body.find("div")
print("Div --",div)
#finding specific text
#finding all para with text some
text = soup.find_all("p",text="Some bold text")
print("Text Some --")
print(text)
#searchng general text
para_text = soup.find_all("p",text=re.compile("Some"))
print("General Text --")
print(para_text)
#finding text with different cases
toggle = soup.find_all("h2",text=re.compile("(H|h)eader"))
print("Toggle General --")
print(toggle)

#CSS selector
#selecting para inside div tag
div_para = soup.select("div p")
print("Div_para--")
print(div_para)
#selecting a para tag just after header tag
head_para = soup.select("h2 ~p")
print("Head-para--")
print(head_para)
#select a bold tag afer a para of specific id
para_id = soup.select("p#paragraph-id b")
print("Para_id--")
print(para_id)

#Getting Different property of header
#Getting header text not text with header tag
headers = soup.find("h2")
print("Headet --",headers)
print("Header String --",headers.string)

#bigger object printing text(If multiple child elements
div_s = soup.find("div")
print("Div--",div.prettify())
print("Div text with string--",div.string)
print("Div text with gettext--",div.get_text())

div_h1 = div_s.find("h1")
print("H1 in div with string --",div_h1.string)

#getting link,src etc in webpage(get specific property of elements
a = soup.find("a")
print("Link--",a)
print("Link value--",a["href"])

#grabbing id of a paragraph
parag_id = soup.select("p#paragraph-id")
print("Para with spec id--",parag_id)
print(parag_id[0]["id"])

#code navigation
#simpler way to navigate
print("Body--",soup.body) #Alternative --body = soup.find(body)
print(soup.body.div.h1.string)

#find siblings
print("Siblings--",soup.body.find("div").find_next_siblings())

