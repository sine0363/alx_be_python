

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Input is not a number")
        

        if choice == '1':
            add_item = input("Enter  item to add:")
            shopping_list.append(add_item)
            print(shopping_list)
            # Prompt for and add an item
            pass
        elif choice == '2':
            remove_item = input("Enter the item you want to remove:")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print("Item not found in the shopping list")
            # Prompt for and remove an item
            pass
        elif choice == '3':
            if shopping_list:
                for add_item in shopping_list:
                    print(add_item)
            else:
                print("Your shoppint list is empty")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    

if __name__ == "__main__":
    main()