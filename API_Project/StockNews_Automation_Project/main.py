import requests
import datetime
import json
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_Key_Stock = "D1O2SO0R34KYKQB9"

address_Stock = "https://www.alphavantage.co/query"
param_Stock = {"function":"TIME_SERIES_DAILY",
         "symbol":STOCK,
         "apikey":API_Key_Stock}

API_Key_News = "966402df34f64dcb88aa9e8083abb85d"
address_News = "https://newsapi.org/v2/everything"
param_News = {"q":COMPANY_NAME,
              "sortby":"popularity",
              "apikey":API_Key_News}

response = requests.get(url=address_News,params=param_News)
NewsTitle = ["","",""]
News = ["","",""]
for i in range(0,3,1):
    NewsTitle[i] = response.json()["articles"][i]["title"]
    News[i] = response.json()["articles"][i]["description"]


response = requests.get(url=address_Stock,params=param_Stock)
data = response.json()["Time Series (Daily)"]
print(data)
# file = open("jsondata.json","r")
# data = json.load(file)["Time Series (Daily)"]
# # print(data)
new_data = [value for value in data.values()]
print(new_data)
Today1_Closing = float(new_data[0]["4. close"])
Today2_Closing = float(new_data[1]["4. close"])

diff = ((Today1_Closing-Today2_Closing)/Today2_Closing)*100

def sendmessage(Text):
    Actual_SID = "ACb890420c4e9555ef114ae4d3970a7b43"
    Actual_Token = "cde9dd3a009c066aae349b77da800da9"
    Actual_Number = "whatsapp:+14155238886"
    Actual_Receiver_Number = "whatsapp:+919654291639"

    client = Client(Actual_SID,Actual_Token)
    for i in range(0,3,1):
        message = client.messages.create(
            body = Text[i],
            from_ = Actual_Number,
            to = Actual_Receiver_Number
        )
        print(message.status)

if abs(diff) >= 5:
    text = ["","",""]
    if diff > 0:
        for i in range(0,3,1):
            text[i] = (f"{STOCK}: 🔺{round(abs(diff))}%\n"
                    f"Headline: {NewsTitle[i]}\n"
                    f"Brief: {News[i]}")
        sendmessage(text)
    else:
        for i in range(0,3,1):
            text[i] = (f"{STOCK}: 🔻{round(abs(diff))}%\n"
                    f"Headline: {NewsTitle[i]}\n"
                    f"Brief: {News[i]}")
        sendmessage(text)
else:
    print(f"Less Diff {diff}")
