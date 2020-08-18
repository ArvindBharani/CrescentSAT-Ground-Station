import datetime
uurl = 'https://pytest-23462.firebaseio.com/'


no_of_entites = 8
entites = {"1":"ALTITUDE", "2":"LONGITITUDE", "3":"LATITUDE", "4":"TEMPERATURE", "5":"HEADING",
           "6" : "PRESSURE", "7":"HUMIDITY", "8":"VELOCITY"}
mission_name=""


def line():
    print("")
    for i in range(0, 100, 1):
        print("=", end="")
    print("")


def get_entities():
    print("\t\t\t\tData uplink-cloud CLI console Setup")
    print(datetime.datetime.now())
    global mission_name
    mission_name = input("Enter the Mission Name...")



def push_data():
    global entites,no_of_entites,mission_name
    check = 1
    from firebase import firebase
    date = str(datetime.datetime.now().date())
    firebase = firebase.FirebaseApplication(uurl, None)
    print(entites)
    firebase.put(url=uurl, name="/" + mission_name+ "/Entites", data=no_of_entites)
    while(check!=0):
        print(datetime.datetime.now())

        data_a = {}
        for i in entites.keys():
            data_a[entites[i]] = input(entites[i]+" = ")
        timet = str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)
        recent={"date":date,"time":timet}
        firebase.put(url=uurl, name= "/"+mission_name+"/recent_log", data=recent)
        firebase.put(url=uurl, name="/"+mission_name+"/"+date+"/"+timet, data= data_a)
        check=int(input("Done.........\n99 to continue\n0-exit\n"))
        line()








line()
get_entities()
line()
push_data()


