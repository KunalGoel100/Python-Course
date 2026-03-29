import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Bluetooth-Tribit-Upgraded-Portable-Waterproof/dp/B078S4P3J9/?_encoding=UTF8&pd_rd_w=ObQjN&content-id=amzn1.sym.1cde463e-0316-4b4b-a52e-a6bd52339fb2&pf_rd_p=1cde463e-0316-4b4b-a52e-a6bd52339fb2&pf_rd_r=Y64SVDGY69JGBTEZH10S&pd_rd_wg=XdghL&pd_rd_r=0f54f4a6-e2ea-4b4c-b5d6-0058311b5b89&ref_=pd_hp_d_atf_dealz_cs&th=1"
# HEADER = {"User-Agent":"CCBot/2.0 (https://commoncrawl.org/faq/)",
#           "Accept-Language":"en-US,en;q=0.5",
#           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#           "Connection": "keep-alive"}
HEADER = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36 Edg/146.0.0.0",
    "Accept-Language": "en-IN,en-US;q=0.9",
    "Accept": "text/html,application/xhtml+xml",
    "Connection": "keep-alive"
}

response = requests.get(url= URL, headers= HEADER)
# print(response)
soup = BeautifulSoup(response.text, "html.parser")
#
temp1 = soup.select(selector=".a-price-whole")
# temp2 = soup.select(selector=".a-price-fraction")
#
# price = [temp1[0].getText() + temp2[0].getText()]
price = temp1[0].getText()
temp = price.split(",")
price = [temp[0]+temp[1]]
Actualprice = float(price[0])
Targetprice = float(2000.0)
if Actualprice <= Targetprice:
    print(f"Go Buy the cooker for {Actualprice} Rs")
else:
    print(f"Current price is {Actualprice} Rs, and Target price is {Targetprice} Rs")
