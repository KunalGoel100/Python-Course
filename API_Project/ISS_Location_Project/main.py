import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()["iss_position"]
Iss_Lat = float(data["latitude"])
Iss_Lon = float(data["longitude"])

My_Lat = 17.425093
My_Lon = 78.375105

if abs(Iss_Lat - My_Lat) <= 5 and abs(Iss_Lon - My_Lon) <=5:
    print("Close Call")
else:
    print("No chance")


