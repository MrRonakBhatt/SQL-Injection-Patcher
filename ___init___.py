from Load import Load
import Test
import time
import os
import gc
class ___init___:
    def ___init___():
        return True
    
    def init_Start():
        responce = Load.__init__()
        gc.collect()
        return responce
    def init_Load_Pro():
        gc.collect()
        return Load.load_Project()
#try:
code,msg = ___init___.init_Start()
path = Load.load_Path()+"Sudarshana"
if code == "1" and not os.getcwd() == path:
    Load.load_Pro_Pros()
    print (msg)
    Load.load_FileDir()
    ROOT,D_NAME,F_NAME = ___init___.init_Load_Pro()
    count = 0
    if D_NAME != []:
        for directory in D_NAME:
            count += 1
            print (str(count)+".) "+directory)
        
    if F_NAME != []:
        for file in F_NAME:
            count += 1
            print (str(count)+".) "+file)
            
    while True:
        #code,msg = ___init___.init_Start()
        #Load.load_FileDir()
        cpath=Load.load_Project()
        print (cpath[0])
        Choise = input("What Do You Want To Do? ").upper()
        if Choise == 'E' or Choise == 'EXIT':
            break
            
        elif Choise == 'B' or Choise == 'Back':
            Choise = 'B'
            BASE = Load.load_Path_Match(ROOT)
            CWD = os.getcwd()
            CWD = Load.load_Path_Match(CWD)
            if BASE < CWD:
                os.chdir("..")
                NEW_ROOT,D_NAME,F_NAME = Load.load_CWD(os.getcwd())
                Load.load_List_FileDir(D_NAME,F_NAME)
            else:
                print ("You Alredy On Your Project Root.")
        elif Choise == 'L' or Choise == 'LIST':
            Choise = 'L'
            Load.load_FileDir()
            CWD = os.getcwd()
            NEW_ROOT,D_NAME,F_NAME = Load.load_CWD(CWD)
            Load.load_List_FileDir(D_NAME,F_NAME)

        elif Choise == 'A' or Choise == 'ALL':
            Choise = 'A'
            Load.under_Maintenance()
            FULL_PATH = os.getcwd()
            conf = input("You Select "+FULL_PATH+"? (Y/n)").upper()
            if conf == "Y" or conf == "YES" or conf == "":
                if os.path.isdir(FULL_PATH):
                    #try:
                    NEW_ROOT,D_NAME,F_NAME = Load.load_CWD(os.getcwd())
                        #Load.load_List_FileDir(D_NAME,F_NAME)
                        #FileDir = os.getcwd()+"\\"+F_NAME
                        #if os.path.exists(FileDir):
                    if F_NAME != []:
                        print ("entrr")
                        for file in F_NAME:
                            if file.lower().endswith(".php"):
                                FileDir = os.getcwd()+"\\"+file
                                print (FileDir)
                                Test.Analysis.file_Analysis(FileDir)
                                    
                    else:
                        print ("[ |------------------------------------------------------| ]")
                        print ("[ |    No file detected in this working Directory.       | ]")
                        print ("[ |    Using 'MANUAL' option chnage working directory.   | ]")
                        print ("[ |------------------------------------------------------| ]")
                        #
                    '''except:
                        print ("No")
                        Load.load_Warning()'''
                        
                elif os.path.isfile(FULL_PATH):
                    print (FULL_PATH,"is a file.")
                
        elif Choise == 'M' or Choise == 'MANUAL':
            Choise = 'M'
        
            FileDir = input("Eneter File or Drectory Name: ").replace("\\",'')
            FULL_PATH = os.getcwd()+"\\"+FileDir
            
            conf = input("You Select "+FileDir+"? (Y/n)").upper()
            if conf == "Y" or conf == "YES" or conf == "":
                print (FileDir)
                print (FULL_PATH+"\\"+FileDir)
                if os.path.isdir(FULL_PATH):
                    try:
                        os.chdir(FULL_PATH)
                        Load.load_FileDir()
                        NEW_ROOT,D_NAME,F_NAME = Load.load_CWD(os.getcwd())
                        Load.load_List_FileDir(D_NAME,F_NAME)
                    except:
                        Load.load_Warning()

                elif os.path.isfile(FULL_PATH):
                    if FULL_PATH.lower().endswith(".php"):
                        print (FileDir,"is a file.")
                        #Read = Load.load_FileRead(FileDir)
                        #print (Read)
                        #Read = Test.Analysis.load_FileRead(FileDir)
                        Test.Analysis.file_Analysis(FileDir)
                        #command = "start cmd /K echo "+Read
                        #os.system(command)
                        time.sleep(2)
                        Load.load_FileDir()
                        NEW_ROOT,D_NAME,F_NAME = Load.load_CWD(os.getcwd())
                        Load.load_List_FileDir(D_NAME,F_NAME)
                        
                    else:
                        print ("This tool accept '.PHP' file only.")
                else:
                    Load.load_Warning()
        else:
            Load.load_Warning()
else:
    Load.load_Pro_Pros()
    print (msg)


'''except:
    Load.load_Warning()'''
            
