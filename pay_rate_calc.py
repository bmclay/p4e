hrs = input("Enter Hours:")
rate = input("Enter Hourly Rate:")
pay = 0

if float(hrs) <= float(40) :
    pay = float(hrs) * float(rate)
else:
    othrs = float(hrs) - float(40)
    otrate = float(rate) / 2 + float(rate)
    pay = float(othrs) * float(otrate) + 40 * float(rate)
print(pay)        
