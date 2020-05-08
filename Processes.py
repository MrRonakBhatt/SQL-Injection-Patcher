from Prints import Prints
import os,platform
import shutil
import sys
import gc

class Processes:
    def os_Detect():
        sys = platform.system()
        path = ""
        if sys == "Windows":
            path = "C:\\Users\\"+os.getlogin()+"\\Documents\\"
        elif sys == "Linux":
            path = "~\\Desktop\\"
        elif sys == "Darwin":
            path = "Tool Under Constructin for MAC."
        return path

    def project_Name():
        PNAME = input("Enter Your Project Name = ").upper()
        return PNAME
            
    def project_Flag(message):
        try:
            msg = message.split("-")
            return msg
        except:
            return Prints.warning()
            sys.exit()
        
    def construct_Project(DST_PATH):
        SRC_PATH = input ("Enter Your Source File or Directory Path = ").rstrip("\\")
        try:
            if os.path.exists(DST_PATH):
                shutil.rmtree(DST_PATH)
                code = shutil.copytree(SRC_PATH, DST_PATH)
                #print ("code = ",code)
                #SRC_PATH = SRC_PATH.split("\\")[-1]
                #print ("SRC_Path = ",SRC_PATH)
            if os.path.exists(code):
                os.chdir(DST_PATH)
                #print ("1-"+SRC_PATH+" - Success!!! File or Directory Successfully Copied...")
                return "1-"+SRC_PATH+" - Success!!! File or Directory Successfully Copied..."
        except:
            Prints.except_Const_Project()
            sys.exit()

    #def Disply_Project(DST_PATH):
        
    def exist_Project(DST_PATH):
        try:
            if os.path.exists(DST_PATH):
                os.chdir(DST_PATH)
                return "1-"+DST_PATH+" - Success!!! Project Open..."
        except:
            Prints.except_Exist_Project()
            sys.exit()

    def remove_Project(DST_PATH):
        try:
            if not os.path.exists(DST_PATH):
                return "1-"+DST_PATH+" - Success!!! Project deleted..."
                
        except:
            Prints.except_Remove_Project()
            sys.exit()
            
    def path_Match(ROOT):
        SLS_Count = ROOT.count("\\")
        return SLS_Count
    
    def file_Read(File):
        with open(File,"r+") as Read_File:
            file = Read_File.read()
            return file
