from firebase import firebase

firebase = firebase.FirebaseApplication('https://flight-planer-crescentsat.firebaseio.com')


x = 1
while True:
    flightAlti = firebase.get('/flight', '/alti')
    flighttemp = firebase.get('/flight', '/temp')

    alti = str(flightAlti)
    temp = str(flighttemp)

    file = open("input_graph.txt", "a")
    file.write(alti + "," + temp+"\n")
    file.close()
    x += 1



