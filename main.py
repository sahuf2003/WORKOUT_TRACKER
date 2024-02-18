import datetime
x = datetime.datetime.now()
x_date = x.strftime("%d/%m/%Y")
x_time = x.strftime("%H:%M:%S")


import requests
TOKEN = YOUR TOKEN
endpoint = NUTRITIONIX ENDPOINT
APP_ID = APP ID
headers ={
    "x-app-id": APP_ID,
    "x-app-key": TOKEN,
}
bruh = {
    "query": input("Enter")
}
# param = json.dumps(bruh)
response = requests.post(url=endpoint, json=bruh, headers=headers)
duration_min = response.json()['exercises'][0]['duration_min']
name = response.json()['exercises'][0]['name']
calorie = response.json()['exercises'][0]['nf_calories']

sheets_url = SHEETY URL
head={
    "Authorization": AUTHORIZATION
}
body={
    'workout':{
    'date':x_date,
    'time':x_time,
    'exercise':name.title(),
    'duration':duration_min,
    'calories':calorie}
}
res = requests.post(url=sheets_url, json=body, headers=head)
print(res.json())
