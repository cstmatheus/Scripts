n1 = int(input('N1: '))
n2 = int(input('N2: '))
# print('a SOMA E {}'.format(n1+n2))
s = n1 + n2
sub = n1 - n2
div = n1 / n2
m = n1 * n2
di = n1 // n2
mod = n1 % n2

p = n1**n2
p1 = pow(n1, n2)
r = n1 ** (1/2)

print('A SOMA = {}, A SUBTRACAO = {}, DIV = {}, MULT = {}, DIV INT = {}, RES = {}, POTE = {}, {}, RAIZ = {:.2f}'.format(s, sub, div, m, di, mod, p, p1, r))

