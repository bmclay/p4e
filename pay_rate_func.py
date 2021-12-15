def computepay(h, r):
    if float(hrs) <= float(40) :
        pay = float(hrs) * float(rate)
    else:
        othrs = float(hrs) - 40
        otrate = float(rate) / 2 + float(rate)
        pay = float(othrs) * float(otrate) + 40 * float(rate)
    return(pay)

hrs = input("Enter Hours:")
rate = input("Enter Hourly Rate:")
p = computepay(hrs, rate)
print("Pay", p)
