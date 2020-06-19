'''
print("每天前进或者后退的数值为0.001")
dayup = pow(1.001, 365)
daydown = pow(0.999, 365)
print("每年向上{:.2f}，向下{:.2f}".format(dayup,daydown))
print("-----------------------")
dayfactor = input("请输入每天前进或者后退的数值：")
dayup = pow(1 + eval(dayfactor), 365)
daydown = pow(1 - eval(dayfactor), 365)
print("每年向上{:.2f}，向下{:.2f}".format(dayup,daydown))
print("-----------------------")
print("工作日0.01")
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1-dayfactor)
    else:
        dayup = dayup * (1+dayfactor)
print("每年向上{:.2f}".format(dayup))
'''
t = pow(1.01, 365)
print("A每年向上{:.2f}".format(t))
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < t:
    dayfactor += 0.001
print("B工作日向上{:.3f}".format(dayfactor))
