x=0
total=0
while x<7:
    num=int(input('number:'))
    if num == 0:
        break
    if num <0:
        print('negative')
        continue
    total = total+num
    x=x+1
print(total)
