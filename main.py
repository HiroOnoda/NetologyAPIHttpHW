
import requests
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
names_list = ["Hulk", "Captain America", "Thanos"]
int_list = []

response = requests.get(url)
buffer = response.json()
for name in names_list:
    for hero in buffer:
        if hero['name'] == name:
            int_list.append(hero['powerstats']['intelligence'])
            #print(hero['powerstats']['intelligence'])

output_list = sorted(zip(names_list, int_list), key = lambda x: x[1])
print(output_list[2])

#print(buffer[0]['powerstats']['intelligence'])
#print(response)
#print(response.json())
