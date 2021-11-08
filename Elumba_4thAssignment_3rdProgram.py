# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def UserInput():
    moneyF = int(input("Enter the amount of money you have:"))
    applePrF = int(input("Enter the price of an apple: "))
    return moneyF, applePrF

def calculation(moneyF, applePrF):
    appleAmoF = moneyF // applePrF
    changeF = moneyF % applePrF
    return appleAmoF, changeF

def displayOutput(appleAmoF, changeF):
    print(f"You can buy {appleAmoF} apples and your change is {changeF} pesos.")

money, applePr = UserInput()
appleAmo, change = calculation(money, applePr)
displayOutput(appleAmo, change)