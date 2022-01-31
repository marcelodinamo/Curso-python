import os
os.system('clear')
dia1 = 5
hora1 = 8
minuto1 = 12
segundo1 = 23
dia2 = 9
hora2 = 5
minuto2 = 12
segundo2 = 23
total_segundo = segundo1 + segundo2
total_minuto = minuto1 + minuto2
total_hora = hora1 + hora2
if total_segundo > 60:
    total_segundo = total_segundo - 60
    total_minuto = total_minuto + 1
if total_minuto > 60:
    total_minuto = total_minuto - 60
    total_hora = total_hora + 1     
     
print(total_hora, ":", total_minuto, ":", total_segundo)  
