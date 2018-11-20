import requests, time
from sys import getsizeof

def main():
    t=time.time()
    r = requests.get('http://speedtest.ftp.otenet.gr/files/test1Mb.db')
    t=time.time()-t

    print("SIZE OF MESSAGE: "+str(len(r.content)/1000)+" kilobytes")
    print("TIME TO OBTAIN: "+str(t)+" seconds")
    
    speed = getsizeof(r.text)/t
    print("\n ~"+str(round(speed/1000))+"kbps")

    return speed/1000

if __name__=="__main__":
    main()
