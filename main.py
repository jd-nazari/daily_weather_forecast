import requests ## for get api



### api detail for reach weather info
KEY = "51fb54f0d12a82af5c6de73b81b28dce"  ## wheater map api key
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"  ## weather map endpoint

## main lat long
LAT = 38.096237
LON = 46.273800


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
today_data = weather_data["list"][:5]
# print(today_data)
# print(len(today_data))
rainy = False
snowy = False
## is today get rainy???? in the 9 hour of day from 10 at morning to 18 at evening
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

# send_params = { 
#   "from": "50002710087321", 
#   "to": ["09390687321", "09145804467"], 
#   "text": "امروز با احتمال فراوان باران می بارد\nباران ببار ببار و زمین را سیراب کن",
#   "udh": ""
# }

### send sms detail
source_num = '50002710087321'

send_to = ["09390687321","09914066587","09374475352","09338518314","09058419906","09901300672","09305028607"]
# print(len(send_to))



# api_end = 'https://console.melipayamak.com/api/send/simple/15ae8331315d409aa36b8217408b7677'
# api_end_2 = 'https://console.melipayamak.com/api/send/advanced/15ae8331315d409aa36b8217408b7677'
api_end_3 = 'https://console.melipayamak.com/api/send/multiple/15ae8331315d409aa36b8217408b7677'

text = "\nسلام\nامروز با احتمال فراوان باران می بارد\nباران ببار ببار و زمین را سیراب کن"
text_2 = "\nسلام\nامروز با احتمال فراوان برف می بارد\nبرف ببار ببار و زمین را سیراب کن"

text_multiple_1 = [text, text, text, text, text, text, text]
text_multiple_2 = [text_2, text_2, text_2, text_2, text_2, text_2, text_2]

if rainy:
    data = {'from':source_num, 'to':send_to, 'text':text_multiple_1, 'udh':''}
    response = requests.post(api_end_3, json=data)
    print(response.json())

elif snowy:
    data = {'from': source_num, 'to': send_to, 'text': text_multiple_2, 'udh':''}
    response = requests.post(api_end_3, json=data)
    print(response.json())



