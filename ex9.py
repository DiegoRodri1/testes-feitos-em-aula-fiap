#9
from doctest import set_unittest_reportflags

from encodings.punycode import segregate

horas = float(input("Me fale quantas horas vc trabalhou: "))
minutos = horas * 60
segundos = minutos * 60

print(horas, "em minutos: ", minutos, "\ne em segundos: ",segundos )
