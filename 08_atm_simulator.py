# ATM Simulator in Python

balance = 10000

print("         ATM SIMULATOR")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        print(f"\n💰 Current Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))

        if amount > 0:
            balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
            print(f"💰 New Balance: ₹{balance}")
        else:
            print("❌ Invalid amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("❌ Invalid amount.")

        elif amount > balance:
            print("❌ Insufficient Balance!")

        else:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
            print(f"💰 Remaining Balance: ₹{balance}")

    elif choice == "4":
        print("\n👋 Thank you for using our ATM!")
        break

    else:
        print("❌ Invalid choice! Please try again.")