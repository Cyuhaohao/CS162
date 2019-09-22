import requests

APIKey=input("API Key:")

r = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=Chicago,'
                 'IL&destination=Los+Angeles,CA&waypoints=Joplin,MO|Oklahoma+City,OK&key=%s' % APIKey)
location=r.json()
print(location["routes"][0]["duration"]["text"])



pokemon = input("Input your pokemon:")
r=requests.get('https://pokeapi.co/api/v2/pokemon/%s' % pokemon)
Pokemon_name=r.json()

print("Name:",pokemon)
print("Attack:", Pokemon_name["stats"][4]["base_stat"])
print("Denfense:", Pokemon_name["stats"][3]["base_stat"])
print("HP:", Pokemon_name["stats"][5]["base_stat"])
print("Sp. Atk:", Pokemon_name["stats"][2]["base_stat"])
print("Sp. Def:", Pokemon_name["stats"][1]["base_stat"])
print("Speed:", Pokemon_name["stats"][0]["base_stat"])
