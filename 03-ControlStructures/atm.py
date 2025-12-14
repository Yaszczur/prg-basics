###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        pin_check = (input('Enter your pin: '))
        if pin_check.isdigit() and pin_check == pin:
            print('Your pin in correct!')
        else:
            print('Your pin in incorrect!')
    elif choice == '5':
        pin_check = input('Enter your current pin: ')
        if pin_check == pin:
            new_pin = input('Enter your new pin: ')
            confirm_new_pin = input('Confirm new pin: ')
            if new_pin.isdigit() and len(new_pin) == 4 and new_pin == confirm_new_pin:
                pin = new_pin
                print('PIN has been changed!')
            elif not new_pin.isdigit() or len(new_pin) != 4:
                print('New pin should contains 4 digits')
            elif new_pin != confirm_new_pin:
                print('Wrong pin')
        else:
            print('Wrong pin!')
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
