unit=int(input("enter the value of unit"))
if unit >=0 and unit <=100:
    amound=unit*1
elif unit >=101 and unit<=200:
    amound=100+(unit-100)*2
elif unit >=201 and unit<=300:
    amound=300+(unit-200)*3
elif unit >=301 and unit<=400:
    amound=600+(unit-300)*4
elif unit >=401 and unit<=500:
    amound=1000+(unit-400)*5
print(amound)
