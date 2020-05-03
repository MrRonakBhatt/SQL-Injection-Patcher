from Processes import Processes
from Prints import Prints
import os,platform,shutil
import sys
import gc

class Main:
    def __init__():
        gc.enable()
        gc.set_threshold(420,10,6)
        store = Processes.os_Detect()+"Sudarshana"
        try:
            if os.path.exists(store) == True:
                return store+" -> Directory Alredy Exist..."
            else:
                create = os.mkdir(store)
                return store+" -> Success!!! File is created..."
            
        except:
            return store+" -> Failed!!! File is not created..."
            sys.exit()

    def start_Project():
        gc.collect()
        Prints.choise_Project()
        Choise = input("What You Want To Do? (N/O/D)").upper()
        try:
            if Choise == "N" or Choise == "NEW":
                NEW = Main.new_Project()
                Choise = "N"+NEW
            elif Choise == "O" or Choise == "OPEN":
                OPEN = Main.open_Project()
                Choise = "O"+OPEN
            elif Choise == "D" or Choise == "DELETE":
                DELETE = Main.delete_Project()
                Choise = "D"+DELETE
            else:
                return Prints.warning()
            return Choise
        except:
            return Prints.warning()
            sys.exit()
            
    def new_Project():
        gc.collect()
        PNAME = input("Enter Your Project Name = ").upper()
        if PNAME != "":
            PNAME = Processes.os_Detect()+"Sudarshana\\"+PNAME
            try:
                if os.path.exists(PNAME) == True:
                    return "0-"+PNAME+" -> Project Is Already Created..."
                    sys.exit()
                else:
                    create = os.mkdir(PNAME)
                    #os.chdir(PNAME)
                    return "1-"+PNAME+" -> Success!!! Project is created..."
            
            except:
                return "0-"+PNAME+" -> Failed!!! Project is not created..."
                sys.exit()
                
    def list_Project():
        gc.collect()
        PNAME = Processes.os_Detect()+"Sudarshana\\"
        try:
            if os.path.exists(PNAME) == True:
                return "1-"+PNAME+" -> Success!!! Project path detected..."
            else:
                return "0-"+PNAME+" -> Project path is not avilable..."
            
        except:
            return "0-"+PNAME+" -> Failed!!! Project path is not Open..."
            sys.exit()

    def open_Project():
        gc.collect()
        PNAME = input("Enter Your Project Name = ").upper()
        if PNAME != "":
            PNAME = Processes.os_Detect()+"Sudarshana\\"+PNAME
            try:
                if os.path.exists(PNAME) == True:
                    return "1-"+PNAME+" -> Success!!! Project open in few second..."
                else:
                    return "0-"+PNAME+" -> Project is not avilable..."
            
            except:
                return "0-"+PNAME+" -> Failed!!! Project is not Open..."
                sys.exit()
                
    def delete_Project():
        gc.collect()
        PNAME = input("Enter Your Project Name = ").upper()
        if PNAME != "":
            PNAME = Processes.os_Detect()+"Sudarshana\\"+PNAME
            try:
                if os.path.exists(PNAME) == True:
                    os.chdir(Processes.os_Detect()+"Sudarshana\\")
                    Open = shutil.rmtree(PNAME)
                    return "1-"+PNAME+" -> Success!!! Project is deleted..."
                else:
                    return "0-"+PNAME+" -> Project is not avilable..."
            
            except:
               return "0-"+PNAME+" -> Failed!!! Project is not deleted..."
               sys.exit()
        
        
#Main.delete_Project()        
