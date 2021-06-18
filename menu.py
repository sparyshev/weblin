#import psutil
import socket
import menu


class MainMenu():

    def setHostname():
        print("11111111111")
        #return socket.gethostname()
        #print("Hostname is :" + socket.gethostname())

    def setNetwork():
        currentNetSettings = 0

    def setDisks():
        currentDiskSettings = 0

    def setLogs():
        currentLogSettings = 0

    def setServices():
        currentServiceSettings = 0

    def getHostname():
        return socket.getfqdn()

    def router():
        answer = input("Input number of your option: ")
        if answer == 0:
            menu.MainMenu.setHostname()
        elif answer == 1:
            menu.MainMenu.setNetwork()
        elif answer == 2:
            menu.MainMenu.setDisks()
        elif answer == 3:
            menu.MainMenu.setLogs()
        elif answer == 4:
            menu.MainMenu.setServices()

    def consoleMenu():
        i = 1
        while i < 4:
            print("######################################################################")
            if i == 1:
                print("################ Server name: " + socket.getfqdn() + " #################")
            if i == 3:
                print("################ Select option:")
            i = i + 1
        num = 0
        options = ['Hostname','Network','Disks', 'Logs', 'Services']
        for i in options:
            print(str(num) + " " + i)
            num = num+1
        menu.MainMenu.router()

