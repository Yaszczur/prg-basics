import json

with open ('09-DictionariesStacksAndQueues/reservations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

rooms = []
paid = 0
unpaid = 0
total_paid = 0
total_unpaid = 0
for reservation in data['reservations']:
    if reservation['room_number'] not in rooms:
        rooms.append(reservation['room_number'])
    
    if reservation['paid']:
        paid += 1
        total_paid += reservation['price_per_night'] * reservation['nights']
    else:
        unpaid += 1
        total_unpaid += reservation['price_per_night'] * reservation['nights']

print('number of rooms: ', len(rooms))
print('paid reservations: ', paid)
print('unpaid reservations: ', unpaid)
print('total value of paid reservations: ', total_paid)
print('total value of unpaid reservations: ', total_unpaid)