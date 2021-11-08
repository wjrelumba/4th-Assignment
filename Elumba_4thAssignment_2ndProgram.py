# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def prices():
    applef = 20
    orangef = 25
    return applef, orangef

def UserInput():
    appleAmo = int(input("Enter the amount of apple/s you want: "))
    orangeAmo = int(input("Enter the amount of orange/s you want: "))
    return appleAmo, orangeAmo

def calculation(applePrF, appleF, orangePrF, orangeF):
    priceF = (applePrF*appleF) + (orangePrF*orangeF)
    return priceF

def displayOutput(priceF):
    print(f"The total amount is {priceF}.")

applePr, orangePr = prices()
apple, orange = UserInput()
price = calculation(applePr, apple, orangePr, orange)
displayOutput(price)