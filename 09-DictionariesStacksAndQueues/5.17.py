import json

with open ('09-DictionariesStacksAndQueues/cities.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Print the JSON data
for city in data:
   for key , value in city.items():
      print(key,':',value)
   print()