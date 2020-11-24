hours = input("How many hours did you work:")
minutes = input("How many minutes did you work:")
hours = int(hours)
minutes = int(minutes)
hours = hours * 2
def PlumberPay(hours,minutes):
    pay = 0
    hours = hours * 20
    minutes = minutes * 20
    pay = hours + minutes
    return pay

print PlumberPay(hours,minutes)
