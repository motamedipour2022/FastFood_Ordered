pizza = input("choise your size S or M or L ?")
coca = input("Do you want sodawater ? Y or N  :")
sos = int(input("How much sose you needed ?"))
bill_sos = sos * 1000

bill = 0

if pizza == "S":
    bill += 60000
elif pizza == "M":
    bill += 85000
elif pizza == "L":
    bill += 110000
else:
    print("Somthing rong order agan")

if coca == "Y":
    bill +=8000

if sos :
    bill = bill_sos + bill
    
print(f"Your final bill is {bill}$")
