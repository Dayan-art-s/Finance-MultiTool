print("=== WELCOME TO FINANCE MULTI-TOOL ===")

usd_to_rub = 80
usd_to_kzt = 450

while True:
    print("Choose action:")
    print("1 - Convert USD to KZT / RUB")
    print("2 - Calculate Saving Goal")
    print("3 - Exit program")

    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        usd_amount = float(input("Enter amount in USD ($): "))
        rub_result = usd_amount * usd_to_rub
        kzt_result = usd_amount * usd_to_kzt
        print(f"Result:")
        print(f"• In Rubles: {rub_result} RUB")
        print(f"• In Tenge: {kzt_result} KZT")

    elif choice == "2":
        goal_name = input("What are you saving for? (e.g., PC, Trip): ").lower()
        goal_price = float(input("Enter goal price in USD ($): "))
        monthly_save = float(input("How much can you save per month in USD ($): "))

        months = 0
        current_savings = 0
        while current_savings < goal_price:
            current_savings += monthly_save
            months += 1

        print(f"Target achieved!")
        print(f"For your goal '{goal_name}', you need to save for {months} months.")

    elif choice == "3":
        print("Thank you for using Finance Multi-Tool!")
        break

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")

print("=== PROGRAM END ===")
