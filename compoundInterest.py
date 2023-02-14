
def calculate_compound_interest():
    client_one_principal = float(input("Princple (amount): "))
    client_one_time =      float(input("Time:       "))
    client_one_rate =      float(input("Rate:       "))
    total_amount = client_one_principal * ((1+(client_one_rate/100)) ** client_one_time)
    
    print("Compound Interest: "+ str(round(total_amount - client_one_principal,2)))

def calculateCompoundInterest():
    calculate_compound_interest()
    print("---")
    calculate_compound_interest()
    print("---")
    calculate_compound_interest()  

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
