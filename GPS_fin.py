import requests

ip = ''  # Replace with your own IP address or leave blank to use your current IP
url = f'https://freegeoip.app/json/{ip}'
response = requests.get(url)

data = response.json()
latitude = data['latitude']
longitude = data['longitude']
print(f'Latitude: {latitude}, Longitude: {longitude}')
f1=open("GPS_Location.txt","w")

f1.write(f'Latitude: {latitude}, Longitude: {longitude}')