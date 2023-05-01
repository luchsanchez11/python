R_etnico = input()
E_socioeconomico = int(input())
ingreso = int(input())
salario=908526
var_1=0



if R_etnico == 'afrodescendiente':
    var_1=(0.2)
elif R_etnico == 'indigena':
    var_1=(0.4)
elif R_etnico == 'raizal':
    var_1=(0.6)
elif R_etnico == 'palenquero':
    var_1=(0.8)
elif R_etnico == 'gitano':
    var_1=(1)
else:
    print("Se presento un error 1")

if E_socioeconomico == 1:
    E_socioeconomico=1
elif E_socioeconomico == 2:
    E_socioeconomico=0.8
elif E_socioeconomico== 3:
    E_socioeconomico=0.5
elif E_socioeconomico== 4:
    E_socioeconomico=0.2
elif E_socioeconomico== 5:
    E_socioeconomico=0
elif E_socioeconomico== 6 :
    E_socioeconomico=0
else:
    print("Se presento un error2")

if ingreso < salario:
    var_3=1
elif ingreso < (salario*2):
    var_3=0.8
elif ingreso < (salario*4):
    var_3=0.6
elif ingreso < (salario*5):
    var_3=0.2
else:
    var_3=0
    

puntaje=(var_1* 2 + E_socioeconomico *3 + var_3 * 5)/10

if puntaje<0.5:
    print("El candidato no continua en el proceso de seleccion")
else:
    print("El candidato continua en el proceso de seleccion")

peso1 = 2
peso2 = 3
peso3 = 5 
Contador = 1
CA = 0
CI = 0
CR = 0
CP = 0
CG = 0
CSR = 0
CAC = 0
SMMLV = 908526


NumeroAspirantes = int(input(""))

while Contador <= NumeroAspirantes:
  
  ReconocimientoEtnico = input("")
  
  if ReconocimientoEtnico == "afrodescendiente":
    x1 = 0.2
    CA += 1
  elif ReconocimientoEtnico == "indigena":
    x1 = 0.4
    CI += 1
  elif ReconocimientoEtnico == "raizal":
    x1 = 0.6
    CR += 1
  elif ReconocimientoEtnico == "palenquero":
    x1 = 0.8
    CP += 1
  elif ReconocimientoEtnico == "gitano":
    x1 = 1
    CG += 1
  elif ReconocimientoEtnico == "sin reconocimiento":
    x1 = 0
    CSR += 1
  else:
    print()

  EstratoSocioEconomico = int(input(""))

  if EstratoSocioEconomico == 1:
    x2 = 1
    
  elif EstratoSocioEconomico == 2:
    x2 = 0.8
  elif EstratoSocioEconomico == 3:
    x2 = 0.5
  elif EstratoSocioEconomico == 4:
    x2 = 0.2
  elif EstratoSocioEconomico == 5:
    x2 = 0
  elif EstratoSocioEconomico == 6:
    x2 = 0
  else:
    print()
    
  Ingresos = float(input(""))
    
  if Ingresos < SMMLV:
    x3 = 1
  elif Ingresos >= SMMLV and Ingresos < 2*SMMLV:
    x3 = 0.8
  elif Ingresos >= 2*SMMLV and Ingresos < 4*SMMLV:
    x3 = 0.6
  elif Ingresos >= 4*SMMLV and Ingresos < 5*SMMLV:
    x3 = 0.2
  else:
    x3 = 0
        
  Puntaje = (x1*peso1 + x2*peso2 + x3*peso3)/(peso1 + peso2 + peso3)
    
  if Puntaje >= 0.5:
    CAC += 1
  else:
    print()
    
  Contador += 1

print(f"{CAC}")
print(f"sin reconocimiento {CSR}")
print(f"afrodescendiente {CA}")
print(f"indigena {CI}")
print(f"raizal {CR}")
print(f"palenquero {CP}")
print(f"gitano {CG}")
