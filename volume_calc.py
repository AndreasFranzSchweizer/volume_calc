#programm berechnet volumen
a = input("Länge Seite angeben: ")
if a.isnumeric():
    a = float(a)
    if a <= 0:
        print ( "Bitte Länge größer 0 anheben")
        exit()
else:
    print ("Bitte Zahl angeben")
    exit()
b = input ( "Länge Seite angeben:")
if b.isnumeric():
    b= float(b)
    if b <= 0:
        print ( "Bitte Länge größer 0 anheben")
        exit()
else:
    print ("Bitte Zahl angeben")
    exit()
c = input ( "Länge Seite angeben:")
if c.isnumeric():
    c = float(c)
    if c <= 0:
        print ( "Bitte Länge größer 0 anheben")
        exit()
else:
    print ("Bitte Zahl angeben")
    exit()
print("Das volumen betragt:", a*b*c)
