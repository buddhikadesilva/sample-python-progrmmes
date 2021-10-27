data=[12,4,-9,7,15,26,-3,-7,11]
x=int(input('input the search item:'))
for i in data:
    if i==x:
        print('item is available')
        break
else:
    print('item is not available')

