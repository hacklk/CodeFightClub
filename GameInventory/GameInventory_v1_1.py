
def display_inventory(inventory):               #print any given Dictionary displaying each key, followed by a colon
    for supply, amount in inventory.items():    #then a space, then the corresponding value, then a newline
        print(supply, ': ', amount)             #Calling the function with an empty dictionary results in displaying nothing


def add_to_inventory(inventory, added_items):   #add the contents of the added_items list to the inventory dictionary
    for supply in added_items:                  #calling with dictionary and items list results in adding items into dictionary
        inventory[supply] = inventory.get(supply, 0) + 1    #as keys and values are set to 1 , or +1 if existed in inventory before
                                                #if same occures more, then dictionary values are incremented those amounts o time


def remove_from_inventory(inventory, removed_items):        #remove the contents of the removed_items list from the inventory dictionary
    for supply in removed_items:
        inventory[supply] = inventory.get(supply, 0) - 1    #decrease by one at every mention -> leaves supplies with 0 volume
    [inventory.pop(supply) for supply in [amount for amount in inventory if inventory[amount] < 1]]  #Remove less-than-one supplies by key
                                                            #as nothing < 1 stays, will not display deducted items, not in original dict


def print_table(inventory, order):
    pass


def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, mode="r") as csv_file:
        added_items = csv_file.read().split(',')
    add_to_inventory(inventory, added_items)
    #return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    export_list = [supply for supply, amount in inventory.items() for count in range(0, amount)]    #creating export list
    with open(filename, 'w') as f:                                                                  #writing to file
        f.write(",".join(export_list))
''' 
# Original Version, withouth comprehension was:
    export_list = []
    for supply, amount in inventory.items():
        for count in range(0, amount):
            exportList.append(supply)
    with open(filename, 'w') as f:
        f.write(",".join(export_list))
'''

if __name__ == "__main__":
    game_inventory = {'Star Wars':5, 'ToyStory':7, 'WowG':10, 'Office':8}
    non_inventory = {}
    added_items = ['Star Wars', 'ToyStory', 'HubalaBaba', 'Seventh', 'Star Wars']
    no_exist = ['rubber', 'boy', 'leToy']

    print('Game Inventory: ')
    display_inventory(game_inventory)
    print('\nNon Inventory: ')
    display_inventory(non_inventory)

    print("\nAdd these items: ", added_items, " to the inventory, so ")
    add_to_inventory(game_inventory, added_items)
    print("Inventory is now ", )
    display_inventory(game_inventory)

    print("\nRemove these items: ", added_items, " from the inventory, so ")
    remove_from_inventory(game_inventory, added_items)
    print("Inventory is now ", )
    display_inventory(game_inventory)

    print("\nRemove these items: ", no_exist, " from the inventory, so ")
    remove_from_inventory(game_inventory, no_exist)
    print("Inventory is now ", )
    display_inventory(game_inventory)

    print("\nExporting file: ... ")
    export_inventory(game_inventory)
    
    print("\nImporting file: ... ")
    import_inventory(game_inventory, "export_inventory.csv")
    display_inventory(game_inventory)

    #print("\nCreate a table: from the inventory, so ")
    #print_table(game_inventory, None)    
