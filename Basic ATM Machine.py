print('Welcome to Free Paisa Bank!!!!')
pin = 5678
chances = 3
balance = 50000
while chances != 0:
    user_pin = int(input('Please enter the four digit pin'))
    if user_pin != pin:
        chances -= 1
        print('Wrong pin number')
        print(f'You have {chances} number of chances left')

    else:
        user_choice = input('B : balance, D : deposit, W : withdraw')
        if user_choice == 'B':
            print(f"Your total balance is Rs. {balance}")

        if user_choice == 'D':
            deposit_user = int(input("Enter the amout that you would like to deposit: "))
            total_balance = deposit_user + balance
            print(f"You have deposited Rs.{deposit_user}")
            print(f"Your total is Rs.{total_balance}")

        if user_choice == 'W':
            withdraw_user = int(input("Enter the amount you want to withdraw"))
            total_balance = balance - withdraw_user
            print(f"You have withdrawn Rs.{withdraw_user}")
            print(f"Your total balance is Rs.{total_balance}")

    user_exit = input("Would you like exit? Yes/No")

    if user_exit == "Yes":
        print("Thank you for using Free Paisa Bank")
        break

    else:
        continue
        

    