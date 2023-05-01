n = 0
k = 0
while n < 1 or k < 1:
    valores_nkm = input().split(' ') 
    n = int(valores_nkm[0]) 
    k = int(valores_nkm[1]) 
    m = int(valores_nkm[2]) 
existencias_actuales = [] 
existencias_solicitadas = [] 
atendidos_sucursal = [] 
 
for i in range(n): 
    existencias = input().split(' ') 
    lista_existencias = [int(i) for i in existencias] 
    existencias_actuales.append(lista_existencias) 
    existencias_solicitadas.append([0 for i in range(k)]) 
    atendidos_sucursal.append(0) 
 
for i in range(m): 
    info_pacientes = input().split(' ')
    sucursal = int(info_pacientes[0])
    tipo_medicamento = int(info_pacientes[1])
    cantidad_solicitada_medicamento = int(info_pacientes[2])
    presion_sistolica = int(info_pacientes[3])
    presion_distolica = int(info_pacientes[4])
  
    if 0 < sucursal <= n and 0 < tipo_medicamento <= k and cantidad_solicitada_medicamento >=0:
        atendidos_sucursal[sucursal - 1] += 1 
        if presion_sistolica < 75 and presion_distolica < 55:
            existencias_solicitadas[sucursal - 1][tipo_medicamento - 1] += cantidad_solicitada_medicamento
        elif presion_sistolica >=75 and presion_sistolica <115 and presion_distolica >=55 and presion_distolica <75:
            pass
        elif presion_sistolica >=115 and presion_sistolica <125 and presion_distolica >=75 and presion_distolica <80:
            pass
        elif presion_sistolica >=125 and presion_sistolica <135 and presion_distolica >=80 and presion_distolica <85:
            existencias_solicitadas[sucursal - 1][tipo_medicamento - 1] += cantidad_solicitada_medicamento
        elif presion_sistolica >=135 and presion_sistolica <155 and presion_distolica >=85 and presion_distolica <95:
            existencias_solicitadas[sucursal - 1][tipo_medicamento - 1] += cantidad_solicitada_medicamento
        elif presion_sistolica >=155 and presion_sistolica <175 and presion_distolica >=95 and presion_distolica <105:
            existencias_solicitadas[sucursal - 1][tipo_medicamento - 1] += cantidad_solicitada_medicamento
        elif presion_sistolica >=175 and presion_distolica >=105:
            existencias_solicitadas[sucursal - 1][tipo_medicamento - 1] += cantidad_solicitada_medicamento
        elif presion_sistolica >=135 and presion_distolica <85:
            existencias_solicitadas[sucursal - 1][tipo_medicamento - 1] += cantidad_solicitada_medicamento        
       
existencias_finales = [] 
minimo_promedio_maximo = [] 
 
for i in range(n): 
    fila = []
    for j in range(k): 
        fila.append(existencias_actuales[i][j] - existencias_solicitadas [i][j]) 
    existencias_finales.append(fila) 
    minimo_promedio_maximo.append([min(existencias_solicitadas[i]), sum(existencias_solicitadas[i])/k, max(existencias_solicitadas[i])])
  
 
 
for i in range(n): 
    cantidad_medicamento_minimo = min(existencias_finales[i]) 
    tipo_medicamento_minimo = existencias_finales[i].index(cantidad_medicamento_minimo) 
    cantidad_medicamento_maximo = max(existencias_finales[i]) 
    tipo_medicamento_maximo = existencias_finales[i].index(cantidad_medicamento_maximo) 
   
    print(i+1) 
    print(tipo_medicamento_minimo + 1, cantidad_medicamento_minimo) 
    print(tipo_medicamento_maximo + 1, cantidad_medicamento_maximo) 
    print("{:.2f} {:.2f} {:.2f}".format(minimo_promedio_maximo[i][0], minimo_promedio_maximo[i][1], minimo_promedio_maximo[i][2])) 
    if atendidos_sucursal[i] > 0: 
        print("{:.2f}".format(sum(existencias_solicitadas[i])/atendidos_sucursal[i]))
    else:
        print("0.00")
 
medicamento1 = [solicitados[0] for solicitados in existencias_solicitadas] 
minimo_medicamento1 = min(medicamento1) 
sucursal_minimo_medicamento1 = medicamento1.index(minimo_medicamento1) 
maximo_medicamento1 = max(medicamento1) 
sucursal_maximo_medicamento1 = medicamento1.index(maximo_medicamento1) 
print(sucursal_minimo_medicamento1 + 1, minimo_medicamento1) 
print(sucursal_maximo_medicamento1 + 1, maximo_medicamento1) 
