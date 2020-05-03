from Processes import Processes
from Prints import Prints
from Main import Main
import os
import gc

class Load:
    def __init__():
        Main.__init__()
        try:
            responce = Main.start_Project()
            #print (responce)
            responce = Processes.project_Flag(responce)
            #print (responce)
            Choise = responce[0]
            #print (Choise)
            DST_PATH= responce[1].strip()+"\\"
            #print (DST_PATH)
        except:
            gc.collect()
            return Prints.warning()
            sys.exit()
            
        if Choise == "N1" or Choise == "O1" or Choise == "D1":
            if Choise == "N1":
                responce = Processes.construct_Project(DST_PATH)
                responce = Processes.project_Flag(responce)
                gc.collect()
                code = responce[0]
                print (code)
                msg = responce[1]+" -> "+responce[2]
                return code,msg
            
            elif Choise == "O1":
                #responce = Processes.Disply_Project(DST_PATH)
                responce = Processes.exist_Project(DST_PATH)
                responce = Processes.project_Flag(responce)
                gc.collect()
                code = responce[0]
                msg = responce[1]+" -> "+responce[2]
                return code,msg
            
            elif Choise == "D1":
                #responce = Processes.Disply_Project(DST_PATH)
                responce = Processes.remove_Project(DST_PATH)
                responce = Processes.project_Flag(responce)
                gc.collect()
                code = responce[0]
                msg = responce[1]+" -> "+responce[2]
                return code,msg
            
        else:
            gc.collect()
            code = responce[0]
            msg = responce[2].strip("> ")
            return code,msg

    def load_Project():
        gc.collect()
        for ROOT,D_NAME,F_NAME in os.walk(os.getcwd()):
            return ROOT,D_NAME,F_NAME


    def load_CWD(CWD):
        for ROOT,D_NAME,F_NAME in os.walk(CWD):
            return ROOT,D_NAME,F_NAME
            
    def load_List_FileDir(D_NAME,F_NAME):
        count = 0
        if D_NAME != []:
            for directory in D_NAME:
                count += 1
                print (str(count)+".) "+directory)
            
        if F_NAME != []:
            for file in F_NAME:
                count += 1
                print (str(count)+".) "+file)

    def load_Path_Match(ROOT):
        return Processes.path_Match(ROOT)
                
    def under_Maintenance():
        return Prints.under_Process()

    def load_FileDir():
        return Prints.load_FileDir()

    def load_Warning():
        return Prints.warning()

    def load_Pro_Pros():
        return Prints.load_Project()

    def load_FileRead(File):
        return Processes.file_Read(File)

    def load_Path():
        return Processes.os_Detect()
            

