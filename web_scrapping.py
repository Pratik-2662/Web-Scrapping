import requests
from bs4 import BeautifulSoup
import pandas as pd
page=requests.get('https://www.amazon.in/b/ref=s9_acss_bw_cg_compacc_1b1_w?node=1375248031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-10&pf_rd_r=KKPQGZ09JVS373M2PFV4&pf_rd_t=101&pf_rd_p=f002c026-20fb-4d36-86e0-2b7c29262b04&pf_rd_i=976392031')
soup=BeautifulSoup(page.content,'html.parser')
Offer_Price=[]
Original_Price=[]
Product_Name=[]
Rating=[]
for a in soup.find_all('span',{'class':'a-price-whole'}):
    Offer_Price.append(a.get_text())
 


for b in soup.find_all('span',{'class':'a-size-mini a-color-tertiary a-text-strike'}):
     copy=b.get_text().lstrip().rstrip()
     Original_Price.append(copy[2:len(copy)])
 


for c in soup.find_all('div',{'class':'a-section octopus-pc-asin-title'}):
     Product_Name.append(c.get_text().lstrip().rstrip())
 


for d in soup.find_all('span',{'class':'a-size-mini a-color-tertiary'}):
     Rating.append(d.get_text())
 

Save_Content=pd.DataFrame({'Product Name ':Product_Name,'Original Price ':Original_Price,'Offer Price ':Offer_Price,'Ratings ':Rating,})
print(Save_Content)
Save_Content.to_csv('products.csv', index=False, encoding='utf-8')
print("Done")






 
