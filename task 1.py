allowables = ["GBP", "USD", "EUR", "JPN"]
rates = [1,1.7,1.25, 173]
pounds = 'GBP'
dollars = 'USD'
yen = 'JPN'
euro = 'EUR'
print("This is the currency converter, welcome!")

var1 = None
while var1 not in range(len(allowables)):
    print('Type the currency you wish to convert from')
    for index, currency in enumerate(allowables):
        print ('enter {0} for {1}'.format(index, currency))
    var1 = input("Type the currency you wish to convert from ")
var1 = int(var1)

var2 = None
while var2 not in range(len(allowables)):
    print('Type the currency you wish to convert to')
    for index, currency in enumerate(allowables):
        print ('enter {0} for {1}'.format(index, currency))
    var2 = input("Type the currency that you wish to convert to ")
var2 = int(var2)

var3 = float(input("Type the amount of currency you wish to convert "))

ammount = var3/rates[var1] *rates[var2]
print(' The converted ammount is {0} {1}'.format(ammount,allowables[var2]))
