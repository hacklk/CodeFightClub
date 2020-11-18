def print_table(inventory, order=None):
    # sort dict in ascending order
    if order == 'count,asc':
        inventory = {k: v for k, v in sorted(
            inventory.items(), key=lambda item: item[1])}
    # sort dict in descending order
    elif order == 'count,desc':
        inventory = {k: v for k, v in sorted(
            inventory.items(), key=lambda item: item[1], reverse=True)}

    # determine longest key for table width
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
