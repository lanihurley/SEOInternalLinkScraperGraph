#install webdriver-manager
#you need to install chromedriver before you can run this and must have path to file.
# Program allows you to Visualize internal links and then display them with a grade and nodes
#Must import python packages BeautifulSoup, Selenium webdriver, service, pandas, networkx and matplotlib
#MUST have a "file_name.txt" file in same directory

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#creation of Service object
s = Service("C:/Users/lhurl/Documents/WA2106/WA170-Python/HOZIO/chromedriver_win32/chromedriver.exe")
browser = webdriver.Chrome(service=s)

# URL's list to be scraped * Must manually enter any page url's desired to be scraped
list_urls = ["https://www.creativedock.com/", "https://www.creativedock.com/about-us"] # this list holds the pages to be scraped
links_with_text = []

# for() loop to iterate through URL list and parse
for url in list_urls:
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for line in soup.find_all("a"):
        href = line.get("href")
        links_with_text.append([url, href])
# turn data into a Pandas DataFrame and write to csv .txt file to give to team to fix broken links
df = pd.DataFrame(links_with_text, columns=["from", "to"])
df.to_csv("file_name.txt", index=False) # save links to .txt file

# Nodes edgelist
GA = nx.from_pandas_edgelist(df, source="from", target="to")
nx.draw(GA, with_labels=True)

# spring layout of graph
G = nx.from_pandas_edgelist(df, "from", "to", create_using=nx.DiGraph())
nx.draw(G, with_labels=True, alpha=0.4, arrows=True, pos=nx.spring_layout(GA))
# show the graph on the DataFrame
plt.show()