import requests, time
from sys import getsizeof

def downloadsp(): # Get Download speed for regularly sized package
    t=time.time()
    r = requests.get('http://speedtest.ftp.otenet.gr/files/test100k.db')
    t=time.time()-t # Find time difference

    print("SIZE OF MESSAGE: "+str(len(r.content)/1000)+" kilobytes")
    print("TIME TO OBTAIN: "+str(t)+" seconds")

    speed = getsizeof(r.text)/t # The speed is the size/time (ex. kbps)
    print("\n ~"+str(round(speed/100))+"kbps") # Print the speed

    return speed/100 # Return the kbps speed from bytes

if __name__=="__main__":
    main()
