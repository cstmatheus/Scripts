m = float(input('Metros ?\n'))

con = m*1000

print('O \033[1;31mVALOR\033[m EM METROS E {}{:.2f}{}'.format('\033[1;34m', con, '\033[m').replace('.' ,','))