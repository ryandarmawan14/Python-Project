'''
In this project, audio file are i'm used is using notification sound from windows
'''

def checker(TARGET,s=10,start="00:00",start_operation=False):
    import time
    import hashlib
    from urllib.request import urlopen, Request
    from datetime import datetime
    import winsound
    
    #if you using custom path location from sound fx, you cant put path on this variable
    wav = ''

    def mainkan(trgt,wav):
            winsound.PlaySound(r''+(str(wav)+str(trgt)), winsound.SND_ASYNC)
            time.sleep(5)
            winsound.PlaySound(None, winsound.SND_ASYNC)
    
    #trgt variable is file wav you put on wav path variable
    trgt='Windows Logon.wav'
    
    mainkan(trgt,wav)
    def execute(TARGET,s):

        #trgt variable is file wav you put on wav path variable
        trgt='Windows Exclamation.wav'

        mainkan(trgt,wav)
        url = Request(str(TARGET), headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(url).read()
        currentHash = hashlib.sha224(response).hexdigest()
        print("\n============================")
        print("CHECKER v1.2\n")
        print("PROGRAM DIMULAI...\n")
        print("URL TARGET = "+str(TARGET))
        print("\n============================\n")

        #trgt variable is file wav you put on wav path variable
        trgt='Windows Notify.wav'

        mainkan(trgt,wav)
        n=0
        flag=0
        now = datetime.now()
        last_time = now.strftime("%H:%M:%S")
        last_hash=0
        while True:
            try:
                response = urlopen(url).read()
                currentHash = hashlib.sha224(response).hexdigest()
                time.sleep(n)
                n=n+s
                response = urlopen(url).read()
                newHash = hashlib.sha224(response).hexdigest()
                if newHash == currentHash:
                    print("\n============================")
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Waktu Sekarang =", current_time)
                    print(str(n)+" detik jarak refresh")
                    print(str(currentHash)+" hash sebelum")
                    print(str(newHash)+" hash terbaru")
                    print("\nTIDAK ADA PERUBAHAN\n\nURL TARGET = "+str(TARGET))
                    print("\nPERUBAHAN SEBELUMNYA:")
                    if flag == 1:
                        print("Waktu Perubahan Terakhir = "+str(last_time))
                        print("Hash Perubahan Terakhir  = "+str(last_hash))
                    else:
                        print("TIDAK ADA")
                    print("\n============================\n")
                    if n>500:
                        n=0
                    else:
                        n=n
                    continue
                else:
                    last_hash = currentHash
                    print("\n============================")
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Waktu Sekarang =", current_time)
                    print(str(n)+" detik jarak refresh")
                    print(str(currentHash)+" hash sebelum")
                    print(str(newHash)+" hash terbaru")
                    print("\nADA PERUBAHAN\n\nURL TARGET = "+str(TARGET))
                    print("\nPERUBAHAN SEBELUMNYA:")
                    print("Waktu Perubahan Terakhir = "+str(last_time))
                    print("Hash Perubahan Terakhir  = "+str(last_hash))
                    print("============================\n")
                    last_time = current_time
                    last_hash = currentHash
                    
                    #trgt variable is file wav you put on wav path variable
                    trgt='Windows Ding.wav'

                    mainkan(trgt,wav)
                    n=0
                    flag=1
                    response = urlopen(url).read()
                    currentHash = hashlib.sha224(response).hexdigest()
                    time.sleep(30)
                    continue
            except Exception as e:
                #trgt variable is file wav you put on wav path variable
                trgt='Windows User Account Control.wav'
                
                print("\n============================")
                print("PROGRAM GAGAL, SHUTDOWN\n")

                #trgt variable is file wav you put on wav path variable
                trgt='Windows Hardware Remove.wav'
                
                mainkan(trgt,wav)
                print(e)
                print("\n============================\n")
                break
    def waiting(TARGET,s,start):
        now = datetime.now()
        time_get = now.strftime("%H:%M:%S")
        if (time_get[0:5])==(start[0:5]):
            print("TIMER SELESAI, MENYALAKAN SCRIPT")
            execute(TARGET,s)
        else:
            time.sleep(10)
            waiting(TARGET,s,start)
    if start_operation==True:
        print("MENUNGGU WAKTU PELUNCURAN "+str(start))
        waiting(TARGET,s,start)
    elif start_operation==False:
        execute(TARGET,s)
