PLP Python Week 8 Toolkit

shopping_list = []

Tool 1: Check whether a number is positive, negative, or zero.

def number_checker():
print("\n--- Number Checker ---")

number = float(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

Tool 2: Manage a shopping list that can change while the program runs.

def shopping_list_tool():
while True:
print("\n--- Shopping List ---")
print("1. Add item")
print("2. Remove item")
print("3. Show list")
print("4. Back to main menu")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter an item to add: ")
        shopping_list.append(item)
        print(f"{item} was added to your shopping list.")

    elif choice == "2":
        item = input("Enter an item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} was removed from your shopping list.")
        else:
            print(f"{item} is not on your shopping list.")

    elif choice == "3":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")

    elif choice == "4":
        print("Returning to the main menu.")
        break

    else:
        print("Sorry, that is not a valid shopping list option.")

Tool 3: Print a multiplication table using a loop.

def multiplication_table():
print("\n--- Multiplication Table ---")

number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    answer = number * multiplier
    print(f"{number} x {multiplier} = {answer}")

Main menu loop

print("Welcome to My Python Toolkit!")

while True:
print("\n=== My Python Toolkit ===")
print("1. Number Checker")
print("2. Shopping List")
print("3. Multiplication Table")
print("4. Quit")

choice = input("Choose an option: ")

if choice == "1":
    number_checker()

elif choice == "2":
    shopping_list_tool()

elif choice == "3":
    multiplication_table()

elif choice == "4":
    print("Thanks for using My Python Toolkit. Goodbye!")
    break

else:
    print(f"Sorry, '{choice}' is not a valid option. Please choose 1, 2, 3, or 4.")