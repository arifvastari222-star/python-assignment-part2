# Part 2: Data Structures
menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

# Task 1 — Explore the Menu

print("\n===== MENU =====\n")

categories = []

for item in menu:
    cat = menu[item]["category"]
    if cat not in categories:
        categories.append(cat)

for cat in categories:
    print(f"===== {cat} =====")

    for item in menu:
        if menu[item]["category"] == cat:
            price = menu[item]["price"]
            available = menu[item]["available"]

            if available:
                status = "Available"
            else:
                status = "Unavailable"

            print(f"{item} ₹{price:.2f} [{status}]")

    print()

total_items = len(menu)

available_items = 0
for item in menu:
    if menu[item]["available"]:
        available_items += 1

print("Total items:", total_items)
print("Available items:", available_items)

max_price = 0
exp_item = ""

for item in menu:
    price = menu[item]["price"]

    if price > max_price:
        max_price = price
        exp_item = item

print("Most expensive item:", exp_item, "-", max_price)

print("\nItems under ₹150:")

for item in menu:
    price = menu[item]["price"]

    if price < 150:
        print(item, "-", price)

# Task 2 — Cart Operations

print("\n===== CART OPERATIONS =====\n")

cart = []

# function to add item
def add_to_cart(item_name, qty):

    if item_name not in menu:
        print("Item not found in menu")
        return

    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable")
        return

    # check if already exists
    for c in cart:
        if c["item"] == item_name:
            c["quantity"] += qty
            print(f"Updated {item_name} quantity to {c['quantity']}")
            return

    # add new item
    cart.append({
        "item": item_name,
        "quantity": qty,
        "price": menu[item_name]["price"]
    })

    print(f"Added {item_name} x{qty}")


# function to remove item
def remove_from_cart(item_name):

    for c in cart:
        if c["item"] == item_name:
            cart.remove(c)
            print(f"{item_name} removed from cart")
            return

    print("Item not found in cart")


# function to update quantity
def update_quantity(item_name, qty):

    for c in cart:
        if c["item"] == item_name:
            c["quantity"] = qty
            print(f"{item_name} quantity updated to {qty}")
            return

    print("Item not found in cart")


# function to print cart
def print_cart():
    print("\nCurrent Cart:")
    for c in cart:
        print(c)


# ----------- Simulation -----------

add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)   # should become 3
print_cart()

add_to_cart("Mystery Burger", 1)  # not exist
print_cart()

add_to_cart("Chicken Wings", 1)   # unavailable
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()


# ----------- Order Summary -----------

print("\n========== Order Summary ==========")

subtotal = 0

for c in cart:
    item_total = c["quantity"] * c["price"]
    subtotal += item_total

    print(f"{c['item']} x{c['quantity']} ₹{item_total:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst:.2f}")
print(f"Total Payable: ₹{total:.2f}")
print("====================================")

# Task 3 — Inventory Tracker with Deep Copy

import copy

print("\n===== TASK 3 =====\n")

inventory_backup = copy.deepcopy(inventory)

# testing deep copy
inventory["Paneer Tikka"]["stock"] = 5

print("Original:", inventory["Paneer Tikka"])
print("Backup:", inventory_backup["Paneer Tikka"])

# restoring
inventory = copy.deepcopy(inventory_backup)

# updating inventory from cart
print("\n--- Updating Inventory ---")

for c in cart:
    item = c["item"]
    qty = c["quantity"]

    if item in inventory:
        stock = inventory[item]["stock"]

        if stock >= qty:
            inventory[item]["stock"] -= qty
        else:
            print(f"Not enough stock for {item}")
            inventory[item]["stock"] = 0

# reorder alerts
print("\n--- Reorder Alerts ---")

for item in inventory:
    stock = inventory[item]["stock"]
    reorder = inventory[item]["reorder_level"]

    if stock <= reorder:
        print(f"⚠ Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {reorder})")

# final print
print("\n--- Final Inventory ---")
print(inventory)

print("\n--- Backup Inventory ---")
print(inventory_backup)

# Task 4 — Daily Sales Log Analysis

print("\n===== TASK 4 =====\n")

print("Revenue per day:")

daily_revenue = {}

for date in sales_log:
    total = 0

    for order in sales_log[date]:
        total += order["total"]

    daily_revenue[date] = total
    print(date, "->", total)

max_rev = 0
best_day = ""

for date in daily_revenue:
    if daily_revenue[date] > max_rev:
        max_rev = daily_revenue[date]
        best_day = date

print("\nBest selling day:", best_day, "-", max_rev)

item_count = {}

for date in sales_log:
    for order in sales_log[date]:
        for item in order["items"]:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

max_item = ""
max_count = 0

for item in item_count:
    if item_count[item] > max_count:
        max_count = item_count[item]
        max_item = item

print("\nMost ordered item:", max_item, "-", max_count)

# adding new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue per day:")

daily_revenue = {}

for date in sales_log:
    total = 0
    for order in sales_log[date]:
        total += order["total"]

    daily_revenue[date] = total
    print(date, "->", total)

max_rev = 0
best_day = ""

for date in daily_revenue:
    if daily_revenue[date] > max_rev:
        max_rev = daily_revenue[date]
        best_day = date

print("\nUpdated Best selling day:", best_day, "-", max_rev)

print("\nAll Orders:\n")

count = 1

for date in sales_log:
    for order in sales_log[date]:
        items = ", ".join(order["items"])

        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")
        count += 1