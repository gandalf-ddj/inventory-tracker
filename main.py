import json
import os

inventory = [

]

def save_inventory():
    with open('inventory.json', 'w') as file:
        json.dump(inventory, file, indent=4)
    print('Inventory saved.')

def load_inventory():
    global inventory
    if os.path.exists('inventory.json'):
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
    else:
        inventory = []
        print('Inventory does not exist, starting with a new inventory.')

def new_inventory():
    name = input('What product are you recieving?\n').lower()
    category = input('What category are you recieving? "ingredient" or "product"\n').lower()
    quantity = int(input('How many items do you have?\n'))
    unit = input('What unit are you recieving?\n').lower()

    item = {
        'name': name,
        'category': category,
        'quantity': quantity,
        'unit': unit
    }

    inventory.append(item)
    save_inventory()

def view_inventory():
    if not inventory:
        print('Inventory is empty.')
    else:
        print('Current inventory is:\n')
        for items in inventory:
            print(f'| Name: {items["name"]} '
                  f'| Category: {items["category"]} '
                  f'| Quantity: {items["quantity"]} {items["unit"]} |')

def search_inventory(name_to_search):
    for item in inventory:
        if item['name'].lower() == name_to_search.lower():
            return item
    return None

def edit_item():
    name = input('What product would you like to edit?\n')
    item = search_inventory(name)
    if item:
        print(f'Found: {item}')
        new_quantity = input('What is the updated quantity of product?\n')
        if new_quantity:
            item['quantity'] = int(new_quantity)
        new_unit = input('Enter new unit of measurement (press enter if no change)\n')
        if new_unit:
            item['unit'] = new_unit
        print(f'Item updated: {item}')
        save_inventory()
    else:
        print('Item not found.')

def delete_item():
    name = input('What product would you like to delete?\n')
    item = search_inventory(name)
    if item:
        confirm = input(f'Are you sure you want to delete item {item["name"]}?'
                         f' Type "y" for yes or "n" for no\n')
        if confirm.lower() == 'y':
            inventory.remove(item)
            print(f'Item {item["name"]} deleted!')
            save_inventory()
    else:
        print('Item not found.')

def user_search():
    name = input('What product would you like to search for?\n')
    item = search_inventory(name)
    if item:
        print(f'Found: {item}')
    else:
        print('Item not found.')

def menu():
    while True:
        print('Welcome to the product management system.')
        print('\n--- Inventory Menu ---')
        print('1. View Inventory\n'
              '2. Add New Item\n'
              '3. Edit Item\n'
              '4. Delete Item\n'
              '5. Search Inventory\n'
              '6. Exit')
        user_choice = str(input('What would you like to do? (1-6): \n'))

        if user_choice == '1':
            view_inventory()
        elif user_choice == '2':
            new_inventory()
        elif user_choice == '3':
            edit_item()
        elif user_choice == '4':
            delete_item()
        elif user_choice == '5':
            user_search()
        elif user_choice == '6':
            print('Thank you for using product management system.')
            break
        else:
            print('Invalid choice. Pease enter a number 1-6.')

if __name__ == '__main__':
    load_inventory()
    menu()