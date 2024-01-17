m = 'CELSIUS TO FAHRENHEIT'
print('\033[1;31m{:=^40}\033[m'.format(m))

c = float(input('CELSIUS ?'))

f = (c*1.8)+32

print('\033[1;31m=\033[m'*40)
m2 = 'FAHRENHEIT ='
print('{}\033[1;36m{}\033[m'.format(m2, f))
print('\033[1;31m=\033[m'*40)