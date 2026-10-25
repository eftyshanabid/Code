def main():
    
    Electricity_Consumption = int(input("Enter your Electricity Consumption for this month: "))
    unit_price_T1 = 5
    unit_price_T2 = 7
    unit_price_T3 = 10
    total_bill = 0
    remainder = 0

    if Electricity_Consumption < 0:
        print("Invalid input")
    else:
        if Electricity_Consumption <= 100:
            total_bill = Electricity_Consumption * unit_price_T1
        elif Electricity_Consumption <= 200:
            remainder = Electricity_Consumption - 100
            total_bill = 500 + remainder * unit_price_T2
        else:
            remainder = Electricity_Consumption - 200
            total_bill = 1200 + remainder * unit_price_T3

    print(f"Your total electricity bill is: ${total_bill}")


main()

    