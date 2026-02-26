import requests
import datetime

pixela_url = "https://pixe.la/v1/users"
pixela_url1 = "https://pixe.la/v1/users/kunalgoel100/graphs"
pixela_url2 = "https://pixe.la/v1/users/kunalgoel100/graphs/kggraph2"
pixela_Token = "1q2w3e4r5t6y7u8i9o"
path = "https://pixe.la/v1/users/kunalgoel100/graphs/kggraph2.html"

header = {"X-USER-TOKEN": pixela_Token}
param_createUser = {"token":pixela_Token,
         "username":"kunalgoel100",
         "agreeTermsOfService":"yes",
         "notMinor":"yes"
         }
param_CreateGraph = {"id":"kggraph2",
                     "name":"Distance Walked",
                     "unit":"Steps",
                     "type":"float",
                     "color":"sora"
                     }

date = datetime.date.today()
# date = date - datetime.timedelta(days=2)
date = date.strftime(format="%Y%m%d")
#
param_UpdateGraph = {"date":date,
                     "quantity":input("How many Steps?")
                     }

response = requests.post(pixela_url2,json=param_UpdateGraph,headers=header)
print(response.text)

# delete = requests.delete("https://pixe.la/v1/users/kunalgoel100/graphs/kggraph2",headers=header)
# print(delete.text)
# update = requests.put(url="https://pixe.la/v1/users/kunalgoel100/graphs/kggraph2/20260226",json=param_UpdateGraph,headers=header)
# print(update.text)

