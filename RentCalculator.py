## Inputs we need from the user
#Total rent
#Total food ordered for snacking 
#Electricity units spent
#Charge per unit
#No. of persons living in the room/Flat

##Output
#Total amount you have to pay is

rent = int(input("Enter your hostel/flat rent: Rs."))
food = int(input("Enter the amount of food ordered: Rs."))
electricity_spent = int(input("Enter the total units of electricity spent: "))
charge_per_unit = int(input("Enter the charge per unit in your area: Rs."))
persons = int(input("Enter the number of persons living in the room: "))


total_bill = electricity_spent * charge_per_unit

output = (rent + food + total_bill) // persons

print("Each person will pay : Rs.", output)