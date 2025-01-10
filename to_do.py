# initiate empty list variable
# function that will offer to add, view, delete or quit
to_dos = []
options = ['add', 'remove', 'view', 'quit']


def add_item():
    to_do_item = input('Please type the name of the item you would like to add. ').title()
    if to_do_item in to_dos:
        print('This item is already in your to-do list. ')
    else:
        to_dos.append(to_do_item.title())

def remove_item():
    item_to_remove = int(input("Please type the number of the item you would like to remove. "))
    if item_to_remove > len(to_dos):
        print(f"{item_to_remove} is not a valid item in your to-do list. ")
    else:
        to_dos.pop(item_to_remove - 1)
        print(f"Item number {item_to_remove} has been removed from your to-do list. ")
    print('\n')

def view_list():
    if (len(to_dos) >= 1):
        for i, name in enumerate(to_dos):
            print(f"{i + 1} {name}")
        print("\n")
    else:
        print("There are no items in your list.")

def display_options():
    print("Your options are: ")
    for i, name in enumerate (options):
        print(f"{i + 1}. {name}")


def greeting ():
    print('Welcome to your to-do list!')

greeting()


while True:
    prompt = '\nPlease type the name of the option you would like to choose. '
    display_options()
    answer = input(prompt)
    try: 
        if answer not in options:
            raise ValueError
        if (answer == 'add'):
            add_item()
        elif (answer == 'remove'):
            view_list()
            remove_item()
        elif (answer == 'view'):
            print('Here is your list')
            view_list()
        elif (answer == 'quit'):
            break
            
    except ValueError:
        print('Enter a valid value. ')







