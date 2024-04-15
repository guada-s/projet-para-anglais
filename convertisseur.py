while ' ':
    print("Repondez par A ou par B")
    answer = input ("Quelle unitée souhaitez vous convertir ?" )
    A= "fahrenheit"
    B = "celsius"
    
    if answer == "A":
        f = input ("fahrhenheit:" )
        c = ( int(f) - 32) * 5//9
        print ( str(c) + "c°" )
        break
    
    elif answer == "B":
            c = input ("celsius:")
            f = ( int(c) * 9/5) + 32
            print ( str(f) + "F°")
            break
"""
f = input("fahrenheit:")
c = ( int(f) - 32) * 5//9
print ( str(c) + "c°")
"""

"""
t = input("tasse:")
ml = int(t) * 250
print ( str(ml) + "ml" )
"""

"""
h = input ("combien d'heures écoulées?")
m = input ("combien de minutes écoulées?")
s = input ("combien de  secondes écoulées?")
secondes = (int(h) * 3600 ) + ( int(m) * 60 ) + int(s)
input ( str(secondes) + "s se sont écoulées")
"""
"""
secondes = input("combien de secondes se sont écoulées?")
heures = int(secondes)//3600
minutes =  (int(secondes) - 3600 ) //60
sec = ( int(secondes) - 3600) - ( int(minutes) * 60)
print ( str(heures) + "heures," + str(minutes) + "minutes et " + str(sec) + "secondes" )
"""
