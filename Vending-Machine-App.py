class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.category})"


class VendingMachine:
    def __init__(self, balance=5.0):
        self.balance = balance
        self.items = [
            Item("Chips", 0.50, "Snack"),
            Item("Soda", 0.75, "Drink"),
            Item("Chocolate", 0.65, "Snack"),
            Item("Water", 0.30, "Drink"),
            Item("Gum", 0.10, "Candy"),
        ]
        self.cart = {}  # {item.name: [Item, quantity]}

    def display_items(self):
        print("\n🛒 Available Items:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print(f"💵 Balance: ${self.balance:.2f}")

    def buy_items(self, item_numbers):
        for item_number in item_numbers:
            if 1 <= item_number <= len(self.items):
                item = self.items[item_number - 1]
                if self.balance >= item.price:
                    self.balance -= item.price
                    if item.name in self.cart:
                        self.cart[item.name][1] += 1
                    else:
                        self.cart[item.name] = [item, 1]
                    print(f"✅ Bought {item.name} for ${item.price:.2f}")
                else:
                    print(f"❌ Not enough balance for {item.name}")
            else:
                print(f"❌ Invalid item number: {item_number}")

    def total_spent(self):
        return sum(item.price * qty for item, qty in self.cart.values())

    def show_summary(self):
        print("\n🧾 Purchase Summary:")
        for item_name, (item, qty) in self.cart.items():
            total = item.price * qty
            print(f"- {item.name} × {qty} = ${total:.2f}")
        print(f"💳 Total Spent: ${self.total_spent():.2f}")
        print(f"💰 Remaining Balance: ${self.balance:.2f}")


# --- Main Program Loop ---
machine = VendingMachine()

while True:
    machine.display_items()
    print("\nEnter item numbers to buy (e.g. 1,3,3,5) or 0 to finish:")
    user_input = input("👉 Your choice: ")

    if user_input.strip() == "0":
        break

    try:
        item_numbers = [int(num.strip()) for num in user_input.split(",")]
        machine.buy_items(item_numbers)
    except ValueError:
        print("⚠️ Please enter valid numbers separated by commas.")

machine.show_summary()
