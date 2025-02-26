def room():
    print("You are in a dimly lit room. You see a dusty bookshelf, a locked drawer, and a window.")
    
def bookshelf():
    print("You found a small key!")
    return True

def drawer(have_key):
    if have_key:
        print("The drawer is unlocked. You open it and find a mysterious note!")
        return True
    else:
        print("The drawer is locked!")
        return False

def window():
    print("You see a dark alleyway.")

def examine_bookshelf():
    action = input("Do you want to examine a book? (yes/no): ").strip().lower()
    if action == "yes":
        print("You found a small key!")
        return True
    elif action == "no":
        return False 
    else:
        print("I don't understand that action.")
        return False

def main():
    have_key = False
    escaped = False
    while not escaped:
        room()  
        action = input("What do you want to do? (open drawer/ examine bookshelf/ look out window): ").strip().lower()
        
        if action == "open drawer":
            have_key = drawer(have_key)
        elif action == "examine bookshelf":
            if not have_key: 
                have_key = examine_bookshelf()
            else:
                print("You've already found the key.")
        elif action == "look out window":
            window()  # No escaping when looking out the window now
        else:
            print("I don't understand that action.")
        
        # You can still escape by opening the drawer if the key is found
        if have_key:
            print("You can now escape the room by opening the drawer.")
        
        if escaped:
            print("Congratulations! You've escaped the room!")

if __name__ == '__main__':
    main()
