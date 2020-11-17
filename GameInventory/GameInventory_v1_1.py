import operator
import pandas as pd

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


def print_table(inventory, order=None):   # PLEASE make this ne prettier, or maybe lets use Pandas and DataFrames?
    label_1 = 'count'
    label_2 = 'item name'
    # Spacing between each column in table
label_1 = 'item name'
    label_2 = 'count  '
    # Spacing between each column in table
    values_spacing = 4
    # Find the longest string in each column of the table so the column can be wide enough to fit all the values.
    max_key_length = max(max(len(x) for x in inventory), len(label_1))
    max_value_length = max(max(len(str(x)) for x in inventory.values()), len(label_2))

    # Sort the inventory depending on which order parameter is passed to function
    if order == 'count,asc':
        sorted_inventory = sorted(inventory.items(), key=operator.itemgetter(1))
    elif order == 'count,desc':
        sorted_inventory = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
    elif order is None:
        sorted_inventory = inventory.items()
    else:
        raise ValueError("Wrong order argument!")

    # Print the table using rjust - a build-in function which right justifies the values.
    print('Inventory:')
    print(label_2.rjust(max_value_length  + values_spacing), label_1.rjust(max_key_length))
    print('  ', '-' * (max_key_length + max_value_length + values_spacing))
    for k, v in sorted_inventory:
        print(repr(v).rjust(max_value_length), " | ", k.rjust(max_key_length))
    print('  ', '-' * (max_key_length + max_value_length + values_spacing))
    print('Total number of items: %d' % sum(inventory.values()))

    
def print_table_df(inventory, order=None):
    #df = pd.DataFrame.from_dict(game_inventory)
    df = pd.DataFrame(list(inventory.items()), columns = ['Count', 'Item name'])
    print(df)

    
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, mode="r") as csv_file:
        added_items = csv_file.read().split(',')
    add_to_inventory(inventory, added_items)
    #return inventory

  
''' # Original  
def import_inventory_csv(inventory, filename="import_inventory.csv"):
    with open(filename, mode="r") as csv_file:
        for supply in csv.reader(csv_file, delimiter=','):
            print(supply)

'''


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

    print("\nCreate a df table from inventory: ")
    print_table_df(game_inventory, None)    
