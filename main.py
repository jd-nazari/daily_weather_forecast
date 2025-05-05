import requests ## for get api



### api detail for reach weather info
KEY = "YOUR API KEY"  ## wheater map api key
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"  ## weather map endpoint

## main lat long
LAT = "Latitude" ## your favorite location
LON = "Longitude"  ## your favorite location


# ## rainy location for test
# lat = 43.8561
# lon = 41.5851
# lat_2 = 40.5354
# lon_2 = 40.5354
# lat_3 = 40.6013
# lon_3 = 43.0975

## api params
params = {
   "lat": LAT,
   "lon": LON,
   "appid": KEY
}


## fetch data
response = requests.get(url=ENDPOINT, params=params)
# print(response.status_code)
# print(response.text)

weather_data = response.json()
today_data = weather_data["list"][:5] ### for next 15 hour
# print(today_data)
# print(len(today_data))
rainy = False
snowy = False
## is today get rainy???? in the 15 hour 
for weather in today_data:
   condition_code = weather["weather"][0]["id"]
   # condition_code = 601  ## for test
   if condition_code < 700:
      if condition_code > 600:
         snowy = True
      else:
         rainy = True

# print(rainy)
# print(snowy)

### send sms detail
source_num = 'SOURCE NUM'

send_to = "YOUR DESTINATION" ## your destination num or nums

api_end_3 = 'SEND SMS API'

text = "Rainy"
text_2 = "Snowy"

### how many peaple do you want to recive sms
text_multiple_1 = [text, text, text, text, text, text, text]
text_multiple_2 = [text_2, text_2, text_2, text_2, text_2, text_2, text_2]


## finally send the message
if rainy:
    data = {'from':source_num, 'to':send_to, 'text':text_multiple_1, 'udh':''}
    response = requests.post(api_end_3, json=data)
    print(response.json())

elif snowy:
    data = {'from': source_num, 'to': send_to, 'text': text_multiple_2, 'udh':''}
    response = requests.post(api_end_3, json=data)
    print(response.json())



