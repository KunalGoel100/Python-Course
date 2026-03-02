import requests
import datetime
import pandas as pd
from pandas import read_table

API_KEY = "nix_live_H5wmq985OZMnJZ1VSS25TzBfHsnaryH0"
API_ID = "app_0724a5f55f1a4783b5c4a4c9"

URL = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

UserInput = input("Describe your activity, eg. Walking for 1 hour :\n")

header = {"x-app-id":API_ID,
          "x-app-key":API_KEY
        }

param = {"query":UserInput,
         "weight_kg": 58,
         "height_cm": 165,
         "age": 25,
         "gender": "male"
}
response = requests.post(url = URL,json=param,headers=header)
data = response.json()["exercises"][0]
duration = data["duration_min"]
calorie = data["nf_calories"]
activity = data["name"]

Temp = datetime.datetime.now()
date = Temp.date()
date = date.strftime("%d/%m/%Y")
time = Temp.time()
time = time.strftime("%H:%M:%S")

dict = {"Date":date,
        "Time":time,
        "Exercise":activity,
        "Duration":duration,
        "Calories":calorie
}

file = pd.read_excel("Workouts.xlsx",index_col=None)
dataframe = pd.DataFrame(data=[dict])

new_dataframe = pd.concat([file,dataframe])
print(new_dataframe)
new_dataframe.to_excel("Workouts.xlsx",index=False)

