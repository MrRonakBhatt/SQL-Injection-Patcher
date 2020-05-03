class Prints:
    def choise_Project():
        print ("1. Create New Project -> N")
        print ("2. Open Project -> O")
        print ("3. Delete Project -> D")
        print (" ")

    def except_Const_Project():
        print ("Failed!!! File or Directory is not copied...",end='')
        print ("May Be File or Directory is Alredy Exist...",end='')
        print ("please check and delete it. if exist.")
        print (" ")

    def load_Project():
        print ("")
        print ("Wait few second...",end='')
        print ("Your project is loading on work enviroment...")
        print ("Project loading process completed...")
        print ("File And Directory Listout Below")
        print ("[  \ ===============  |--|--|  =============== /  ]")
        print ("                      V  V  V                    ")

    def load_FileDir():
        print (" ")
        print ("|--------------------------------------------------|")
        print ("|   0. Listout -> ['L'] or ['List']                |")
        print ("|     It's listout file and directory.             |")
        print ("|                                                  |")
        print ("|  |-----<We Have Two Method For Analysis.>-----|  |")
        print ("|  |                                            |  |")
        print ("|  |  1. Autometed -> ['A'] or ['All']          |  |")
        print ("|  |     It's analyse all file in CWD           |  |")
        print ("|  |     CWD -> ('Currant Working Directory')   |  |")
        print ("|  |                                            |  |")
        print ("|  |  2. Menual -> ['M'] or ['MENUAL']          |  |")
        print ("|  |     It's analyse selected file.            |  |")
        print ("|  |                                            |  |")
        print ("|  |-----<-------------------------------->-----|  |")
        print ("|                                                  |")
        print ("|   <<. Back -> ['B'] or ['BACK']                  |")
        print ("|   X. Exit -> ['E'] or ['EXIT']                   |")
        print ("|--------------------------------------------------|")
        print (" ")

    def load_File():
        print ("We Load your File For anaysis")
               
    def under_Process():
        print ("Under Construction.")
        print (" ")

    def warning():
        print ("WARNING!!! DO NOT TRY ANY OUT OF BOUND INPUT")
