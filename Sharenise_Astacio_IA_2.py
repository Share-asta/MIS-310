#Problem 1
temperature_fahrenheit=float(input("Enter the Temperature in Fahrenheit"))

temperature_celsius = (temperature_fahrenheit-32) * 5/9

print(round(temperature_celsius, 1))

if temperature_celsius<=0:
    print("Ice")

elif temperature_celsius>0 and temperature_celsius<=100:
    print("Liquid")

else:
    print("Gas")

#Problem 2
packages=float(input("Enter the Number of Packages: "))
shipping_type=input("Enter the Shipping Type (r/e): ").lower()

if shipping_type=="r":
    rate=10

elif shipping_type=="e":
    rate=15

else:
    print("Error.")
    exit()

delivery_charge=packages*rate

print("Total Delivery Charge: $",format(delivery_charge,".2f"))


