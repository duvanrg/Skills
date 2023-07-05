# Valor Metro cubico
valor= int(input("ingrese el valor por metro cubico"))  
#b: Total metros cúbicos consumidos en el mes
consumo = int(input("ingrese el total de metros cubicos consumidos"))  
iva = 0.19  #e: Valor del impuesto (iva) 19%

#valor sin iva incluido
print(f"el valor del cosumo normal es: {valor*consumo}")  

#valor con iva incluido
print(f"el valor con el iva incluido es: {(valor*consumo)+(valor*consumo*iva)}")  
