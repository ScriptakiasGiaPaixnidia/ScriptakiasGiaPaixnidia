#python script :)
import platform
import datetime
print "                 CODED BY SCRIPTFORGAMES"
def stuffs():
    print "-T gia na deis thn wra"
    print "-H gia boitheia"
    print "-Y gia na deis to litourgiko su sistima"

print stuffs()
g = raw_input("ektelese mia entolh:")

def time():
    global today
    today = datetime.date.today()
    print today

def help():
    print "an den katalabes kati apla epikinonise mazi mu"

def systemoperation():
    print platform.system()
    


if g == "-T":
    print time()

if g == "-H":
    print help()

if g == "-Y":
    print systemoperation()

