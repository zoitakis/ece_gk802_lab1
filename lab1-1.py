import requests

#ΖΗΤΑΕΙ ΕΝΑ URL ΠΟΥ ΘΑ ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΤΗΣ ΜΟΡΦΗΣ "https://www.google.com"

print( "Δώστε μας το URL:" )
url = input()

#ΓΙΝΕΤΑΙ ΤΟ ΑΙΤΗΜΑ ΣΤΟ ΕΠΙΘΥΜΗΤΟ URL ΚΑΙ ΜΑΣ ΤΥΠΩΝΕΙ ΤΟΥΣ HEADERS

r = requests.get( url )
headers = r.headers
for key, value in headers.items():
    print( key ,": ",value )

#ΔΙΝΕΙ ΤΗΝ ΑΠΑΝΤΗΣΗ ΣΤΗΝ ΕΡΩΤΗΣΗ ΣΧΕΤΙΚΑ ΜΕ ΤΟ SERVER ΤΟΥ ΕΞΥΠΗΡΕΤΗΤΗ

Server = headers["Server"]
print( "\n\nΟ Server που χρησιμοποιεί ο εξυπηρετητής είναι ο: ",Server ,"\n")


#ΕΑΝ Η ΣΕΛΙΔΑ ΠΟΥ ΕΛΕΓΧΟΥΜΕ ΧΡΗΣΙΜΟΠΟΙΕΙ COOKIES ΜΑΣ ΤΥΠΩΝΕΙ ΤΟ ΑΝΤΙΣΤΟΙΧΟ ΜΗΝΥΜΑ,
#ΤΙΣ ΟΝΟΜΑΣΙΕΣ ΤΟΥΣ ΚΑΙ ΤΗΝ ΗΜΕΡΟΜΗΝΙΑ ΛΗΞΗΣ ΤΟΥ ΚΑΘΕΝΟΣ ΑΛΛΙΩΣ ΜΑΣ ΤΥΠΩΝΕΙ 
#ΑΡΝΗΤΙΚΟ ΜΗΝΥΜΑ

count = 0
name =[]

try : 
    cookies = headers["Set-Cookie"].split( "; " )
    print( "Η σελίδα χρησιμοποιεί cookies\n" )
    for cookie in cookies:
        name.append(cookie)
        check = cookie.find( "expires=" )
        check2 = cookie.find( "Expires=" )
        if check == 0 or check2==0:
            print("Το όνομα του cookie είναι ",*name[0:len(name)-1],\
                  "και λήγει στις",cookie[8:],"\n")
            name=[]
        count +=1
    

except :
    print( "Η σελίδα δεν χρησιμοποιεί cookies" )
