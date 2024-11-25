import os
import random
import sys
import textwrap
# ATTRIBUTE - ???

class shopperkepper:
    tempCount = 0
    def __init__(self, name, item): # Attribute
        self.name = name
        self.item = item
        self.inventory = []

    def __str__(self):
        return f"{self.name} - (Stock: {self.inventory})"
    
    def add_attribute(self, attribute):
        "Add Item"
        self.inventory.append(attribute)

    def shop_inventory(self):
        """Display all items in the inventory."""
        if not self.inventory:
            print("\nUnavailable.")
            return
        print(f"\n{self.name}'s Inventory:")
        for idx, item in enumerate(self.inventory, start=1):
            try:
                print(f"{idx}. {item['name']} - ${item['price']}")
            except KeyError:
                print(f"Invalid item structure: {item}")
    
# Now For The Shop    
def shop(shopperkepper):
    """inventory choose"""
    shopperkepper.add_attribute(("Sword"))
    shopperkepper.add_attribute(("Armor"))
    shopperkepper.add_attribute(("Extra"))
    
# Sword
def list_sword(shopperkepper):
    """Add swords to inventory."""
    shopperkepper.inventory.clear()
    shopperkepper.add_attribute({"name": "Wooden Sword", "price": 1.2})
    shopperkepper.add_attribute({"name": "Stone Sword", "price": 3.5})
    shopperkepper.add_attribute({"name": "Iron Sword", "price": 4.5})
    shopperkepper.add_attribute({"name": "Platinum Sword", "price": 9.5})

# Armor
def list_armor(shopperkepper):
    """Add armors to inventory."""
    shopperkepper.inventory.clear()
    shopperkepper.add_attribute({"name": "Leather Armor", "price": 3.5})
    shopperkepper.add_attribute({"name": "Chain Armor", "price": 4.6})
    shopperkepper.add_attribute({"name": "Iron Armor", "price": 2.5})
    shopperkepper.add_attribute({"name": "Platinum Armor", "price": 8.5})

# Extra
def list_extra(shopperkepper):
    """Add extra items to inventory."""
    shopperkepper.inventory.clear()
    shopperkepper.add_attribute({"name": "Medicine", "price": 4.5})
    shopperkepper.add_attribute({"name": "Potion", "price": 3.5})
    shopperkepper.add_attribute({"name": "Shield", "price": 4.5})
    shopperkepper.add_attribute({"name": "Cannon", "price": 7.5})

# Extra Shop
def extra_shop():
    """Setup the initial shop inventory."""
    shopperkepper_items = shopperkepper("The ShopperKepper", None)
    list_sword(shopperkepper_items)
    list_armor(shopperkepper_items)
    list_extra(shopperkepper_items)
    return shopperkepper_items

# dialouge shop
def dialouge(shopperkepper):
    """Dialouge for Store"""
    while True:
        print(f"Hello There! Would Like Order Some?")
        response = input("Response: ").strip().lower()
        
        if response == "yes":
            print(f"which one will you buy?")
            print(f"1. Sword\n2. Armor\n3. Extra")
            choose = input("Choose: ").strip()
            
            # Display The Items
                
            if choose == "1":
                print(f"List Sword:")
                list_sword(shopperkepper)
                shopperkepper.shop_inventory()
                
            elif choose == "2":
                print(f"List Sword:")
                list_armor(shopperkepper)
                shopperkepper.shop_inventory()
                
            elif choose == "3":
                print(f"List Sword:")
                list_extra(shopperkepper)
                shopperkepper.shop_inventory()
                
            else:
                print("Wrong, Number!")
                continue # back to response
            
            # Giving The Item List
            print(f"Choose Which Are Your Ordering?")
            
            try:
                shop_index = int(input("Choose Number: ")) - 1
                if 0 <= shop_index < len(shopperkepper.inventory):
                    choice_one = shopperkepper.inventory[shop_index]
                    # CHOOSEN ITEMS
                    if 'name' in choice_one and 'price' in choice_one:
                        print(f"you purchased: {choice_one['name']} for {choice_one['price']:.2f}")
                    else:
                        print(f"Invalid!")
            except(ValueError, IndexError) as e:
                print("Insert Valid Number Error: {e}")
                continue # back to giving item list
            
            # Order Of Choose
            
            print(f"-"*30)
            
        elif response == "no":
            print(f"alright no? ok then.")
            break # break from dialouge
        else:
            print("Have to response with yes or no")
            continue # back to response
        # If Item Doesn't Exist!
        
        # Repeat If you want another Purchase
        print(f"is there anything else?")
        while True:
            second_response = input("Response: ").strip().lower()
            if second_response == "yes":
                print(f"Alright, Then")
                break # return to shop
            elif second_response == "no":
                print(f"thank you, comeback soon if you anything!")
                return # Exit From The Program
            else:
                print("Have to response with yes or no")
                continue

# End Point
if __name__ == "__main__":
    shopperkepper = extra_shop()
    dialouge(shopperkepper)

    
