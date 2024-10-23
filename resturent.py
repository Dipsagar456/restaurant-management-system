menu = {
    'Pizza':425,
    'Burger':375,
    'Cheeseburger':560,
    'cheese sandwich':480,
    'Checken burger':875,
    'Spicy checken':900,
    'Hot dog':300,
    'Fruit salad':200,
    'Cocktails':150,
    'Sandwich':325,
    'Milk shake':80,
    'Milk tea':75,
    'Ilechi tea':80,
    'Iced tea':60,
    'orange tea':70,
    'Lemon tea':50,
    'Coffee':100,
    'Black coffee':150,
}
print("Wel come to  FULL_MOON Restaurent")
for items, price in menu.items():
    print(f"{items}:Rs {price}")

order_total =0


item_1 =input("enter the name of Items u want to order=").title()

if item_1 in menu:
     order_total += menu[item_1]
     print(f" Your item {item_1} has been added to your order")
else:
     print(f"Ordered item {item_1} is not available yet now....!!!")

another_order =input("Do you want to add another items..?(Yes/No)") 
if another_order.lower() =="Yes":
     itme_2=input("Enter the name of second item =").title()
     if itme_2 in menu:
          order_total +=menu[itme_2]
          print(f"Item {itme_2} has been added to your order")
     else:
        print(f"Ordered itme {itme_2} is not avaialable!")

print(f"The total amount of items is to pay {order_total}")
