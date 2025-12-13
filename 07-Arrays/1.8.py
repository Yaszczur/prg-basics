computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
computer_games.sort()
i = 1
for item in computer_games:
    print(i,item)
    i += 1

i = 0
while i < len(computer_games):
    print(i+1,computer_games[i])
    i += 1

for i, item in enumerate(computer_games):
    print(i+1, item)