from random import choice


shopping_cart = {}

def add_info(item):
    shopping_cart.appened(item)
def del_info(item):
    shopping_cart.remove(item)
def show_info():
    print(shopping_cart)
                        
    
def main():
    while True:
        choice = input("what would you like to do? show/Add/Delete or Quit? ")
        if choice.lower() == "show":
            show_info
        elif choice.lower() == "add":
            item = input("what would you like to add? ")
            add_info(item)
        elif choice.lower() == "delete":
            item = input("what would you like to delete? ")
            del_info(item)
        else:
            print("you chose to quit")
            break
    print(shopping_cart)
     
main()

import my_module

length = int(input("What is the length of your house? "))
width = int(input("What is the width of your house? "))

print(f"Your houses square footage is {my_module.square_foot(length, width)}")

radius = int(input("What is the radius of your circle? "))

print(f"The circumference of your circle is {my_module.circumference(radius)}")

    