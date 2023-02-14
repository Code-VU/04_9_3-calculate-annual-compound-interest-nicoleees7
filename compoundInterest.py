def print_math_ci(principle,time,rate):
    total_amount = principle*(1+(rate/100))**time
    print(total_amount)
    print("Compound Interest: "+ str(round(total_amount - principle,2)))

def collect_inputs_and_convert():
    client_prin = float(input("Princple (amount): "))
    client_time = float(input("Time: "))
    client_rate = float(input("Rate: "))

    return client_prin, client_time, client_rate

def calculateCompoundInterest():
    line_break = "---"
    client_prin_1, client_time_1, client_rate_1 = collect_inputs_and_convert()
    print_math_ci(client_prin_1,client_time_1,client_rate_1)
    print(line_break)
    
    client_prin_2, client_time_2, client_rate_2 = collect_inputs_and_convert()
    print_math_ci(client_prin_2,client_time_2,client_rate_2)
    print(line_break)
    client_prin_3, client_time_3, client_rate_3 = collect_inputs_and_convert()
    print_math_ci(client_prin_3,client_time_3,client_rate_3)
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you

 #print("Compound Interest: "+str(intrest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
