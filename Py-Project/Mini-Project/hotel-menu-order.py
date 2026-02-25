# Hotel Menu >>>>

menu = {
    "Pizza":299,
    "Veg-Burger":99,
    "Non-Veg Burger":199,
    "Maggie":99,
    "Pasta":99,
    "Cold Drink" : 69,
    "Tea":50,
    "Hot Coffee": 69,
    "Cold Coffee":99

}

#Greet to coustomer 
name = input("Please enter your name :- ")
print(f"Welcome {name} to Hotel XYZ ")

# Hotel Menu 

print("Pizza - Rs. 299/-\nVeg-Burger - Rs. 99/-\nNon-Veg Burger - Rs. 199/- \nMaggie - Rs. 99/-\nPasta Rs. 99/- \nCold Drink - Rs.69/- \nTea - Rs.50/- \nHot Coffee: Rs. 69/- \nCold Coffee - Rs. 99")

order_total = 0 # This Variable take price of orderd food 


first_item = input("Enter the item you want to order :- ")

if first_item in menu:
    order_total += menu[first_item]
    print(f"your item {first_item} has been added to order")
else:
    print(f"your ordered item {first_item} is not available in menu please order something else that we can serve you")

another_order = input("Do you want to add another item (Yes/No):-")

if another_order == "Yes":
    second_item = input("Enter the second item you want to order :- ")
    if second_item in menu:
        order_total += menu[second_item]
        print(f"your item {second_item} has been added to order")
    else:
        print(f"your ordered item {second_item} is not available in menu please order something else that we can serve you")

print(f"The total amount of items to pay is {order_total}")