print ("¿quieres saber la los minutos?")

horas= int(input('ingresa la hora: '))
minutos= int(input('ingresa los minutos: '))
segundos= int(input('ingresa los segundos: '))

total_segundos= (horas*3600) + (minutos*60) + segundos

print (f'el total en segundos es: {total_segundos}')