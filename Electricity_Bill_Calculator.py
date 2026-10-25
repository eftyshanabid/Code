def main():
    Electricity_Consumption = int(input("Enter your Electricity Consumption for this month: "))
    unit_price_T1 = 5
    unit_price_T2 = 7
    unit_price_T3 = 10
    total_bill = 0
    remainder = 0

    if Electricity_Consumption < 0 :
        print("Invalid input")
    elif Electricity_Consumption <= 100 :
        total_bill = total_bill*unit_price_T1
    elif Electricity_Consumption >= 100 and Electricity_Consumption <= 200:
        total_bill = 500
        remainder = Electricity_Consumption - 100
        for i in range(0,remainder) :
            total_bill = total_bill + unit_price_T2
    else:
        total_bill = 1200
        remainder = Electricity_Consumption - 200
        for i in range (0,remainder):
            total_bill = total_bill + unit_price_T3
                

    if not Electricity_Consumption < 0 :
        print(total_bill)


main()

    