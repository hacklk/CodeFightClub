def print_table(inventory, order=None):

    keys = [len(key) for key in inventory]
    max_width_left = max(keys)
    max_width_right = len('count')
    left = 'item name'  # left column name
    right = 'count'     # right column name

    print((max_width_left + max_width_right + 5) * '-')
    print(f'{left:>{max_width_left}} | {right:>{max_width_right}}')
    print((max_width_left + max_width_right + 5) * '-')
    for key, value in inventory.items():
        print(f'{key:>{max_width_left}} | {value:>{max_width_right}}')


print_table({'Star Wars': 5, 'ToyStory': 7, 'WowG': 10, 'Office': 8})
