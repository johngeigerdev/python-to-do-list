# initiate empty list variable
# function that will offer to add, view, delete or quit

to_dos = []
options = ['add', 'remove', 'view', 'quit']
def todo_options ():
    selection = input('Would you like to add, remove, view or quit? ')
    try: 
        if (selection == 'add'):
            print('Type the name of the item you would like to add. ')
        if selection not in options:
            raise ValueError(f'{selection.title()} not a valid option')
        elif (selection == 'remove'):
            print('Please type the name of the item you would like to remove. ')
        elif (selection == 'view'):
            print('We are showing your list')
        elif (selection == 'quit'):
            print('quit')
    except ValueError: 
        print('Enter a valid value. ')

todo_options()