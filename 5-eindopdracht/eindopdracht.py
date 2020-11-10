import time #Zodat hij de secondes kan wachten

seconds = input("Sec: ")
s = int(seconds)
minute = input("Min: ")
m = int(minute)
hour = input("Hour: ")
h = int(hour)

    #Input voor de gewenste tijd

while (s < 60): #inplaats van een for gebruik ik while zodat hij stopt met tellen bij de 60 seconden marking

    print ("Hour:" +str(h) + " " + "Min:" + str(m) + " " + "Sec:" + str(s)) #Print statement voor output

    time.sleep(1) #aangegeven op regel 1 ... de seconden tellen
    s=s+1

    if (s == 60):
        m=m+1
        s = 0

    elif(m == 60):
        h=h+1
        m = 0
    
    elif(h == 24):
        h = 0

    #Hele blok gebruiken om de sec min en uur op 0 te zetten