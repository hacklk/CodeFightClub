game_inventory = {'Star Wars': 5, 'ToyStory': 7, 'WowG': 10, 'Office': 8}

print("{:<10} {:<10}".format('item name', 'count'))

for key, value in game_inventory.items():
    print("{:<10} {:<10}".format(key, value))
