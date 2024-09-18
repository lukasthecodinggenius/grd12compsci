def main():
    inventory = []

    try:
        while True:
            choice = input('Add or Remove? ')
            if choice.lower() == 'add':

                dict = {
                    'item':0,
                    'quantity':0,
                    'price':0,
                }
                item, quantity, price = input('what are you adding (item,quantity,price)? ').split(',')
                if item in inventory:
                    print('item already in inventory')
                else:
                    add_item(item,quantity,price,inventory,dict)
                    totalvalue = total_inventory_value(inventory)
                    print(f'total value: ${totalvalue:.2f}')
            elif choice.lower() == 'remove':
                remove = input('what item would you like to remove? ')
                if remove in inventory:
                    remove_item(remove)
                else:
                    print('item not in inventory')

    except EOFError:
        totalvalue = total_inventory_value(inventory)
        print(f'final inventory value: ${totalvalue:.2f}')


def add_item(i,q,p,inventory,dict):
    dict['item'] = i
    dict['quantity'] = q
    dict['price'] = p
    inventory.append(dict)

def total_inventory_value(inventory):

    total = 0
    for dict in inventory:
        total += (int(dict['quantity']) * int(dict['price']))
    return total

def remove_item(remove, inventory):

    inventory.remove(remove)
    return inventory



main()






