n = 0
while n<1:
    Inventario_actual = []
    Dosis_solicitada =  []
    nm = input().split(' ')
    n = int(nm[0])
    m = int(nm[1])

def condicional(pacientes,sucursal,presion_sistolica,presion_distolica):
     if 0 < sucursal <= n:
        if presion_sistolica <75 and presion_distolica <55:
            Dosis_solicitada[sucursal - 1] += 7
        elif 125 <= presion_sistolica < 135 and 80 <= presion_distolica < 85:
            Dosis_solicitada[sucursal - 1] += 1
        elif 135 <= presion_sistolica < 155 and 85 <= presion_distolica < 95:
            Dosis_solicitada[sucursal - 1] += 7
        elif 155 <= presion_sistolica < 175 and 95 <= presion_distolica < 105:
            Dosis_solicitada[sucursal - 1] += 15
        elif presion_sistolica >= 135 and presion_distolica < 85:
            Dosis_solicitada[sucursal - 1] += 15
        elif presion_sistolica >= 175 and presion_distolica >= 105:
            Dosis_solicitada[sucursal - 1] += 30

for i in range(n): 
    Existe = 0
    while Existe < 1:
        Existe = int(input())
    Inventario_actual.append(Existe)
    Dosis_solicitada.append(0)

for i in range(m): 
    Inventario_final = []
    divisiones = []
    pacientes = input().split(' ')
    sucursal = int(pacientes[0])
    presion_sistolica = float(pacientes[1])
    presion_distolica = float(pacientes[2])
    condicional(pacientes,sucursal,presion_sistolica,presion_distolica)
for i in range(n):
    Inventario_final.append(Inventario_actual[i]-Dosis_solicitada[i])

for i in range(n):
    divisiones.append(Dosis_solicitada[i]/Inventario_actual[i])
Valor_Minmimo = min(Inventario_final)
Valor_Maximo = max(Inventario_final)
Resultado_valor_minimo = Inventario_final.index(Valor_Minmimo) + 1
Resultado_valor_maximo = Inventario_final.index(Valor_Maximo) + 1
print(Resultado_valor_minimo, Valor_Minmimo)
print(Resultado_valor_maximo, Valor_Maximo)
for i in range(n):
    print('{:}{: .2f}%'.format(i+1, divisiones[i] * 100))
