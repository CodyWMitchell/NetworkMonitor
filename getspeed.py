import requests, time
from sys import getsizeof

def downloadsp():
    t=time.time()
    r = requests.get('http://speedtest.ftp.otenet.gr/files/test100k.db')
    t=time.time()-t

    print("SIZE OF MESSAGE: "+str(len(r.content)/1000)+" kilobytes")
    print("TIME TO OBTAIN: "+str(t)+" seconds")

    speed = getsizeof(r.text)/t
    print("\n ~"+str(round(speed/100))+"kbps")

    return speed/100

if __name__=="__main__":
    main()
