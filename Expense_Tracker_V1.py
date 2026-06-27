import json
from datetime import date


print("WELCOME !")

try:
    with open("Symbols.json","r") as symbols_file:
        Symbols = json.load(symbols_file)
except (FileNotFoundError, json.JSONDecodeError):
    Symbols = {}

currency = Symbols.get("currency_symbol")
if not currency:
    currency = input("Please enter your currency symbol (e.g., $, €, ₹) : ")
    Symbols["currency_symbol"] = currency
    with open("Symbols.json","w") as symbols_file:
        json.dump(Symbols, symbols_file, indent=4)

try:
    with open("Expenses.json", "r") as expenses_file:
        expenses_data = json.load(expenses_file)
        expenses_data.setdefault("daily", {})
        expenses_data.setdefault("monthly", {})
except (FileNotFoundError, json.JSONDecodeError):
    expenses_data = {"daily": {}, "monthly": {}}

today = date.today()
monthly_date = today.strftime("%Y-%m")
daily_date = today.strftime("%Y-%m-%d")

print("Date : " + str(today))

expenses_data["monthly"].setdefault(monthly_date, {})
expenses_data["daily"].setdefault(daily_date, {})

while True:
    category = input("(1.) 💵 - Monthly expenditure\n(2.) 🪙 -  Daily expenditure \n(3.) 📊 - View Expenses \n(4.) Exit \nPlease select an expense category (Enter the number): ")

    while category not in ["1", "2", "3", "4"]:
        print("Invalid input. Please enter '1' for monthly expenditure, '2' for daily expenditure, '3' to view expenses, or '4' to exit.(Enter the number)")
        category = input("(1.) 💵 - Monthly expenditure\n(2.) 🪙 -  Daily expenditure\n(3.) 📊 - View Expenses \n (4.) Exit \nPlease select an expense category (Enter the number): ")

    if category == "1":
        expense = input("(1.) 🏠- Housing Rent \n(2.) 🏦 - Loan (or) EMI \n(3.) 🛒 - Groceries \n(4.) 💧 - Water Bill \n(5.) 📚 - Education \n(6.) 💡 - Electricity \n(7.) 🌐 - Internet \n(8.) 🧴 - LPG Cylinders \n(9.) 💊 - Medicines \n(10.) 🕑 - Other \n(0.) 🔙 - Back \nPlease select an expense : ")
        if expense not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            print("Invalid input. Please enter a number between 0 and 11.")
        elif expense == "0":
            print("Going back to the category selection.")
            continue
        elif expense == "1":
            amount1 = input("Please enter Your housing rent amount : " + currency)
            expenses_data["monthly"][monthly_date]["Housing Rent"] = float(amount1)
            print("Housing Rent amount added successfully.")
        elif expense == "2":
            amount2 = input("Please enter Your loan/EMI amount : " + currency)
            expenses_data["monthly"][monthly_date]["Loan/EMI"] = float(amount2)
            print("Loan/EMI amount added successfully.")
        elif expense == "3":
            amount3 = input("Please enter Your groceries amount : " + currency )
            expenses_data["monthly"][monthly_date]["Groceries"] = float(amount3)
            print("Groceries amount added successfully.")
        elif expense == "4":
            amount4 = input("Please enter Your water bill amount : " + currency)
            expenses_data["monthly"][monthly_date]["Water Bill"] = float(amount4)
            print("Water Bill amount added successfully.")
        elif expense == "5":
            amount5 = input("Please enter Your education amount : " + currency)
            expenses_data["monthly"][monthly_date]["Education"] = float(amount5)
            print("Education amount added successfully.")
        elif expense == "6":
            amount6 = input("Please enter Your electricity amount : " + currency)
            expenses_data["monthly"][monthly_date]["Electricity"] = float(amount6)
            print("Electricity amount added successfully.")
        elif expense == "7":
            amount7 = input("Please enter Your internet amount : " + currency)
            expenses_data["monthly"][monthly_date]["Internet"] = float(amount7)
            print("Internet amount added successfully.")
        elif expense == "8":
            amount8 = input("Please enter Your LPG cylinders amount : " + currency)
            expenses_data["monthly"][monthly_date]["LPG Cylinders"] = float(amount8)
            print("LPG Cylinders amount added successfully.")   
        elif expense == "9":
            amount9 = input("Please enter Your medicines amount : " + currency)
            expenses_data["monthly"][monthly_date]["Medicines"] = float(amount9)
            print("Medicines amount added successfully.")
        elif expense == "10":
            amount10 = input("Please enter Your other amount : " + currency)
            expenses_data["monthly"][monthly_date]["Other"] = float(amount10)
            print("Other amount added successfully.")

    elif category == "2":
        expense = input("(1.) 🍔 - Food \n(2.) ☕ - Coffee \n(3.) 🥤 - Drinks \n(4.) 🏪 - Shopping \n(5.) 🎬 - Entertainment \n(6.) 📦 - Miscellanous \n(7.) 🍬 - chewing gum (or) 🚬 - cigarettes \n(8.) 🚕 - Transportation \n(9.) 🍎 - Fruits & Vegetables \n(10.) 🕑 - Other \n(0.) 🔙 - Back \nPlease select an expense : ")
        if expense not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            print("Invalid input. Please enter a number between 0 and 10.")
        elif expense == "0":
            print("Going back to the category selection.")
            continue
        elif expense == "1":
            amount10 = input("Please enter Your food amount : " + currency)
            expenses_data["daily"][daily_date]["Food"] = float(amount10)
            print("Food amount added successfully.")
        elif expense == "2":
            amount11 = input("Please enter Your coffee amount : " + currency)
            expenses_data["daily"][daily_date]["Coffee"] = float(amount11)
            print("Coffee amount added successfully.")
        elif expense == "3":
            amount12 = input("Please enter Your drinks amount : " + currency)
            expenses_data["daily"][daily_date]["Drinks"] = float(amount12)
            print("Drinks amount added successfully.")
        elif expense == "4":
            amount13 = input("Please enter Your shopping amount : " + currency)
            expenses_data["daily"][daily_date]["Shopping"] = float(amount13)
            print("Shopping amount added successfully.")
        elif expense == "5":
            amount14 = input("Please enter Your entertainment amount : " + currency)
            expenses_data["daily"][daily_date]["Entertainment"] = float(amount14)
            print("Entertainment amount added successfully.")
        elif expense == "6":
            amount15 = input("Please enter Your miscellanous amount : " + currency)
            expenses_data["daily"][daily_date]["Miscellaneous"] = float(amount15)
            print("Miscellaneous amount added successfully.")
        elif expense == "7":
            amount16 = input("Please enter Your chewing gum/cigarettes amount : " + currency)
            expenses_data["daily"][daily_date]["Chewing Gum/Cigarettes"] = float(amount16)
            print("Chewing Gum/Cigarettes amount added successfully.")
        elif expense == "8":
            amount17 = input("Please enter Your transportation amount : " + currency)
            expenses_data["daily"][daily_date]["Transportation"] = float(amount17)
            print("Transportation amount added successfully.")
        elif expense == "9":
            amount18 = input("Please enter Your fruits & vegetables amount : " + currency)
            expenses_data["daily"][daily_date]["Fruits & Vegetables"] = float(amount18)
            print("Fruits & Vegetables amount added successfully.")
    
    elif category == "3":
        expense_type = input("Enter '1' to view Daily expenses or '2' to view Monthly expenses: ")
        while expense_type not in ["1", "2"]:
            print("Invalid input. Please enter '1' for Daily expenses or '2' for Monthly expenses.")
            expense_type = input("Enter '1' to view Daily expenses or '2' to view Monthly expenses: ")
        if expense_type == "1":
            view_date = input("Enter date in YYYY-MM-DD format to view Daily expenses for that date (Note : Don't forget the hyphens):")
            if view_date in expenses_data["daily"]:
                print(f"Daily expenses for {view_date}:")
                for expense_name, amount in expenses_data["daily"][view_date].items():
                    print(f"{expense_name}: {currency}{amount}")
            else:
                print(f"No daily expenses recorded for {view_date}.")
        elif expense_type == "2":
            view_date = input("Enter date in YYYY-MM format to view Monthly expenses for that date (Note : Don't forget the hyphens):")
            if view_date in expenses_data["monthly"]:
                print(f"Expenses for {view_date}:")
                for expense_name, amount in expenses_data["monthly"][view_date].items():
                    print(f"{expense_name}: {currency}{amount}")
                if not expenses_data["monthly"][view_date]:
                    print(f"No expenses recorded for {view_date}.")
            else:
                print(f"No monthly expenses recorded for {view_date}.")

    elif category == "4":
        print("Exiting the Expense tracker !")
        break

            
    with open("Expenses.json", "w") as expenses_file:
        json.dump(expenses_data, expenses_file, indent=4)