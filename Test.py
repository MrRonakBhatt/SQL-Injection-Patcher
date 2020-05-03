import re
import Replace
import configparser

Config = configparser.ConfigParser()
Config.read("mysqli_doc.ini")
Sections = Config.sections()
Section = Sections[0]
Options = Config.options(Section)
dict1 = dict()
for option in Options:
    dict1[option] = Config.get(Section, option)

#print (dict1,"\n")

#File = "F:\\CyberAcharya\\Mascot Technology Solution\\Builder\\dev\\dev\\ck1_CP.php"
#File = "F:\\CyberAcharya\\product\\petchmanagement\\SQL_Patch\\o.php"
class Analysis:
    '''def load_FileRead(File):
        with open(File) as FR:
            file = FR.read()
            return file'''
        
    def file_Analysis(File):
        encode_list = ["utf-8","utf-16","utf-16-le","utf-32","windows-1250","windows-1252","iso-8859-1","iso-8859-15","latin-1"]
        encode = "None"
        while True:
            try :
                for e in encode_list:
                    tmp_fil = open(File,encoding = e)
                    if tmp_fil.read():
                        print ("encoding = ",e)
                        encode = e
                        break
                if encode != "None":
                    break        
                    
            except :
                break
            
        if encode != "None": 
            with open(File, encoding="utf8") as FR:
                data = FR.read()
                data = str(data)
                print ("")
                print ("=========================> | Your File data | <=========================")
                print (data)
                print ("=========================> | ============== | <=========================")
                linetmp = data.split("\n")

                Func_list = ["mysqli_query","mysqli_real_query"]
                Fun_con = 0
            
                for func in Func_list:
                    #print ("\n"+func)
                    for indx, tmp in enumerate(linetmp):
                        if re.search(func, tmp):
                            Fun_con += 1

                        
                #print (linetmp)
                #print (Func_list)
                Open_con = 0
                flag = 0
                while True:
                    if Open_con > Fun_con:
                        print ("=========================> | Your Final Deta | <=========================")
                        print (data)
                        print ("===============> | Fixing Process Complete Successfully | <==============")
                        break
                    
                    Open_con += 1
                    
                    for i,line in enumerate(linetmp):
                        #print ("test = ",line)
                        '''if not re.search("mysqli_real_query",line):
                            execute = 1
                        else:
                            execute = 0'''
                
                        if not (re.search("(^\/\/)",line)):
                            #print ("line = ",line)
                            line=line.lower()
                            Full = re.search("(select[\s]|[\S])(([\w+\,-]+|\*)|([\w+-]+|\*))[\s]from([\s][\w+-]+[\s])where([\s]([\w+\=\"\.\'\$]+)|([\w+\=\'\$-]+))*([^*]\;|[\s][^*]\;)",line)
                            Split = re.search("select[\s](([\w+\,-]+|\*)|([\w+-]+|\*))[\s]([^*]\.|[\s][^*]\.)",line)
                            End = re.search("select[\s](([\w+\,-]+|\*)|([\w+-]+|\*))[\s]from([^*]\.|[\s][^*]\.)",line)
                            Half = re.search("select[\s](([\w+\,-]+|\*)|([\w+-]+|\*))[\s]from([\s][\w+-]+)([^*]\.|[\s][^*]\.)",line)
                            Var = re.search("select[\s](([\w+\,-]+|\*)|([\w+-]+|\*))[\s]from([\s][\w+-]+[\s])where([^*]\.|[\s][^*]\.)",line)
                    
                        if Full:
                                print ("\n"+"Type-Full: Select query detected."+"\n")
                                print ("Query Statment: ",line.strip("\t"),"\n")
                                line = line.split(",")
                            
                                lin = list()
                                if len(line) > 2:
                                    for n,l in enumerate(line):
                                       if n > 0:
                                           print (l)
                                           lin.append(l)
                                    c = ","
                                    lin =  c.join(lin)      
                                    line[1] = lin
                            
                                query = str(line[1])
                                point = query.count("$")
                                Vars = list()
                        
                                if point > 0:
                                    print (point,"Injection point detected in above query","\n")
                                    stmnt = str(line[0]+","+line[1])
                                    #print (stmnt.strip("\t"))
                                    extract = re.findall(r"((\$\w*)\b)",stmnt)
                                    c = 0
                        
                                    for word in extract:
                                        Vars.insert(c,word[0])
                                        c += 1
                            
                                    print ("Total Points found = ",Vars,"\n")
                                    comment = "//"+stmnt
                                    print ("Vulnerable Query Commented =\n"+comment,"\n")
                                    query = re.sub('[\+\'\"\;\(\)\{\}]','',query)
                                    var = re.findall(r"\$\w+",query)
                                    print ("Injectable Points = ",    var,"\n")
                                    for j in var:
                                        query = query.replace(j,"?")
                            
                                    query = '"'+query+'");'
                                    print ("Fix query: ",query)
    
                                    line[1] = query
                                    prepare = line[0]

                                    if not prepare.replace("mysqli_query","mysqli_prepare"):
                                        line[0] = prepare.replace("mysqli_real_query","mysqli_prepare")
                                    else:
                                        line[0] = prepare.replace("mysqli_query","mysqli_prepare")
                                
                                    
                                    #print ("line[0] = ",line[0])
                                    #print ("line[1] = ",line[1])
                                    #print ("query = ",query)
                                    query = line[0]+", "+query
                                    print ("\nNew Query Statement= ",query,"\n")
                        
                                    s=""
                                    bind_var=""
                                    for j in var:
                                        s = s+"s"
                                        #print (j)
                                        bind_var = bind_var+", "+j
                                        bind = "mysqli_stmt_bind_param("+Vars[0]+","+"\""+s+"\""+bind_var+");"
                        
                                    #print ("bind = ",bind)
                                    Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                    '''if execute == 1:
                                        Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"

                                    else:'''
                                
                        
                                    Fix_qry_data = comment+"\n"+query+"\n"+bind+"\n"+Query_Exc+"\n"
                                    #print (linetmp)
                                    print ("\n"+"line[",i,"] = ",linetmp[i],"\n")
                                    print ("[  /----------\ < Type Full End > /----------\  ]")
                                    #print ("Fix_qry_data = ",Fix_qry_data)
                                    linetmp[i] = Fix_qry_data
                                    n="\n"
                                    #print (n,"linetmp = ",linetmp)
                                    Fix = n.join(linetmp)
                                    #print ("Data Fix = ",Fix)
                                    with open (File,"w+") as wd:
                                        wd.write(Fix)
                                        #print ("File Write")
                                    with open (File,"r+") as rd:
                                        data = rd.read()
                                        #print ("data = ",data,)
                                        linetmp = data.split("\n")
                                    
                                        for func in dict1:
                                            #print ("\n"+func)
                                            for indx, tmp in enumerate(linetmp):
                                                if not (re.search("(^\/\/)",tmp)):
                                                    #print ("tmp = ",tmp)
                                                    if re.search(func, tmp):
                                                        print (func)
                                                        print (dict1[func])
                                                        tmp = tmp.replace(func,dict1[func])
                                                        linetmp[indx] = tmp
                                                '''else:
                                                    print ("tmp = ",tmp)'''
                                        data = n.join(linetmp)
                                        #print("Data Fix = ",Fix_Data)
                                        with open (File,"w+") as wd:
                                            wd.write(data)
                                            #print ("final Write")
                                            break
                                        #print ("write file.")
    
                        elif Split:
                            print ("\n"+"Type-Split: Select query detected."+"\n")
                            j = 0
                            s = " "
                            n = "\n"
                            ln = 0
                            line_list = list()
                            
                            while True:
                    
                                #print (j,"Query Statment: ",str(linetmp[i+j]).strip("\t"))
                            
                                line_list.append(str(linetmp[i+j]).strip("\t").strip("\.").strip("\"\'"))
                                line = s.join(line_list)
                                print ("line = ",line)
                                if re.search("[^*]\;",linetmp[i+j]):
                                    break
                                j += 1
                     
                            line = line.split(",")
                        
                            lin = list()
                            if len(line) > 2:
                                for n,l in enumerate(line):
                                   if n > 0:
                                       print (l)
                                       lin.append(l)
                                       c = ","
                                lin =  c.join(lin)      
                                line[1] = lin
                        
                            query = str(line[1])
                            point = query.count("$")
                            Vars = list()
                        
                            if point > 0:
                                print (point,"Injection point detected in above query","\n")
                                stmnt = str(line[0]+","+line[1])
                                #print (stmnt.strip("\t"))
                                extract = re.findall(r"((\$\w*)\b)",stmnt)
                                c = 0
                        
                                for word in extract:
                                    Vars.insert(c,word[0])
                                    c += 1
                            
                                print ("Total Points found = ",Vars,"\n")
                                k = 0
                                comment = list()
                                
                                while True:
                                
                                    print (k,"Query Statment: ",str(linetmp[i+k]).strip("\t"))
                                    tmp_str = str("//"+str(linetmp[i+k]))
                                    linetmp[i+k] = "//"+str(linetmp[i+k])
                                    ln = i+k
                                    
                                    #print (tmp_str)
                                    #print (comment)
                                    comment.append(tmp_str)
                                    #print (comment)
                                
                                    
                                    
                                    if re.search("[^*]\;",linetmp[i+k]):
                                        break
                                    k += 1
                                comment = n.join(comment)
                                print ("Vulnerable Query Commented =\n"+comment,"\n")
                                query = re.sub('[\+\'\"\;\(\)\{\}]','',query)
                                var = re.findall(r"\$\w+",query)
                                print ("Injectable Points = ",    var,"\n")
                                for q in var:
                                    query = query.replace(q,"?")
                        
                                query = '"'+query+'");'
                                print ("Fix query: ",query)
    
                                line[1] = query
                                prepare = line[0]

                                if not prepare.replace("mysqli_query","mysqli_prepare"):
                                    line[0] = prepare.replace("mysqli_real_query","mysqli_prepare")
                                else:
                                    line[0] = prepare.replace("mysqli_query","mysqli_prepare")
                                
                                
                                #print ("line[0] = ",line[0])
                                #print ("line[1] = ",line[1])
                                #print ("query = ",query)
                                query = line[0]+", "+query
                                print ("\nNew Query Statement= ",query,"\n")
                            
                                s=""
                                bind_var=""
                                for j in var:
                                    s = s+"s"
                                    #print (j)
                                    bind_var = bind_var+", "+j
                                    bind = "mysqli_stmt_bind_param("+Vars[0]+","+"\""+s+"\""+bind_var+");"
                        
                                #print ("bind = ",bind)
                                Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #if execute == 1:
                                #Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #else:
                                
                        
                                Fix_qry_data = linetmp[ln]+"\n"+query+"\n"+bind+"\n"+Query_Exc+"\n"
                                #print (linetmp) 
                                print ("\n"+"line[",ln,"] = ",linetmp[ln],"\n")
                                print ("[  /----------\ < Type-Split End > /----------\  ]")
                                #print ("Fix_qry_data = ",Fix_qry_data)
                                linetmp[ln] = Fix_qry_data
                                    
                                #print (n,"linetmp = ",linetmp)
                                Fix = n.join(linetmp)
                                #print ("Data Fix = ",Fix)
                                with open (File,"w+") as wd:
                                    wd.write(Fix)
                                    #print ("File Write")
                                with open (File,"r+") as rd:
                                    data = rd.read()
                                    #print ("data = ",data,)
                                    linetmp = data.split("\n")
                                
                                    for func in dict1:
                                        #print ("\n"+func)
                                        for indx, tmp in enumerate(linetmp):
                                            if not (re.search("(^\/\/)",tmp)):
                                                #print ("tmp = ",tmp)
                                                if re.search(func, tmp):
                                                    print (func)
                                                    print (dict1[func])
                                                    tmp = tmp.replace(func,dict1[func])
                                                    linetmp[indx] = tmp
                                            #else:
                                            #    print ("tmp = ",tmp)
                                    data = n.join(linetmp)
                                    #print("Data Fix = ",Fix_Data)
                                    with open (File,"w+") as wd:
                                        #print ("data = ",data)
                                        wd.write(data)
                                        #print ("final Write")
                                        break

                        elif Half:
                            
                            print ("\n"+"Type-Half: Select query detected."+"\n")
                            j = 0
                            s = " "
                            n = "\n"
                            ln = 0
                            line_list = list()
                            while True:
                    
                                #print (j,"Query Statment: ",str(linetmp[i+j]).strip("\t"))
                            
                                line_list.append(str(linetmp[i+j]).strip("\t").strip("\.").strip("\"\'"))
                                line = s.join(line_list)
                                print ("line = ",line)
                                if re.search("[^*]\;",linetmp[i+j]):
                                    break
                                j += 1
                     
                            line = line.split(",")
                        
                            lin = list()
                            if len(line) > 2:
                                for n,l in enumerate(line):
                                   if n > 0:
                                       print (l)
                                       lin.append(l)
                                       c = ","
                                lin =  c.join(lin)      
                                line[1] = lin
                        
                            query = str(line[1])
                            point = query.count("$")
                            Vars = list()
                        
                            if point > 0:
                                print (point,"Injection point detected in above query","\n")
                                stmnt = str(line[0]+","+line[1])
                                #print (stmnt.strip("\t"))
                                extract = re.findall(r"((\$\w*)\b)",stmnt)
                                c = 0
                        
                                for word in extract:
                                    Vars.insert(c,word[0])
                                    c += 1
                            
                                print ("Total Points found = ",Vars,"\n")
                                k = 0
                                comment = list()
                                
                                while True:
                                
                                    print (k,"Query Statment: ",str(linetmp[i+k]).strip("\t"))
                                    tmp_str = str("//"+str(linetmp[i+k]))
                                    linetmp[i+k] = "//"+str(linetmp[i+k])
                                    ln = i+k
                                    
                                    #print (tmp_str)
                                    #print (comment)
                                    comment.append(tmp_str)
                                    #print (comment)
                                
                                    
                                    
                                    if re.search("[^*]\;",linetmp[i+k]):
                                        break
                                    k += 1
                                comment = n.join(comment)
                                print ("Vulnerable Query Commented =\n"+comment,"\n")
                                query = re.sub('[\+\'\"\;\(\)\{\}]','',query)
                                var = re.findall(r"\$\w+",query)
                                print ("Injectable Points = ",    var,"\n")
                                for q in var:
                                    query = query.replace(q,"?")
                        
                                query = '"'+query+'");'
                                print ("Fix query: ",query)
        
                                line[1] = query
                                prepare = line[0]

                                if not prepare.replace("mysqli_query","mysqli_prepare"):
                                    line[0] = prepare.replace("mysqli_real_query","mysqli_prepare")
                                else:
                                    line[0] = prepare.replace("mysqli_query","mysqli_prepare")
                                
                                
                                #print ("line[0] = ",line[0])
                                #print ("line[1] = ",line[1])
                                #print ("query = ",query)
                                query = line[0]+", "+query
                                print ("\nNew Query Statement= ",query,"\n")
                        
                                s=""
                                bind_var=""
                                for j in var:
                                    s = s+"s"
                                    #print (j)
                                    bind_var = bind_var+", "+j
                                    bind = "mysqli_stmt_bind_param("+Vars[0]+","+"\""+s+"\""+bind_var+");"
                    
                                #print ("bind = ",bind)
                                Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #if execute == 1:
                                #Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #else:
                                
                        
                                Fix_qry_data = linetmp[ln]+"\n"+query+"\n"+bind+"\n"+Query_Exc+"\n"
                                #print (linetmp) 
                                print ("\n"+"line[",ln,"] = ",linetmp[ln],"\n")
                                print ("[  /----------\ < Type-End End > /----------\  ]")
                                #print ("Fix_qry_data = ",Fix_qry_data)
                                linetmp[ln] = Fix_qry_data
                                
                                #print (n,"linetmp = ",linetmp)
                                Fix = n.join(linetmp)
                                #print ("Data Fix = ",Fix)
                                with open (File,"w+") as wd:
                                    wd.write(Fix)
                                    #print ("File Write")
                                with open (File,"r+") as rd:
                                    data = rd.read()
                                    #print ("data = ",data,)
                                    linetmp = data.split("\n")
                            
                                    for func in dict1:
                                        #print ("\n"+func)
                                        for indx, tmp in enumerate(linetmp):
                                            if not (re.search("(^\/\/)",tmp)):
                                                #print ("tmp = ",tmp)
                                                if re.search(func, tmp):
                                                    print (func)
                                                    print (dict1[func])
                                                    tmp = tmp.replace(func,dict1[func])
                                                    linetmp[indx] = tmp
                                            #else:
                                                #print ("tmp = ",tmp)
                                    data = n.join(linetmp)
                                    #print("Data Fix = ",Fix_Data)
                                    with open (File,"w+") as wd:
                                        #print ("data = ",data)
                                        wd.write(data)
                                        #print ("final Write")
                                        break
                            
                                                       
                        #print (Split)
                        elif End:
                            print ("\n"+"Type-End: Setect query detected.")
                            j = 0
                            s = " "
                            n = "\n"
                            ln = 0
                            line_list = list()
                            while True:
                    
                                #print (j,"Query Statment: ",str(linetmp[i+j]).strip("\t"))
                            
                                line_list.append(str(linetmp[i+j]).strip("\t").strip("\.").strip("\"\'"))
                                line = s.join(line_list)
                                print ("line = ",line)
                                if re.search("[^*]\;",linetmp[i+j]):
                                    break
                                j += 1
                     
                            line = line.split(",")
                        
                            lin = list()
                            if len(line) > 2:
                                for n,l in enumerate(line):
                                   if n > 0:
                                       print (l)
                                       lin.append(l)
                                       c = ","
                                lin =  c.join(lin)      
                                line[1] = lin
                            
                            query = str(line[1])
                            point = query.count("$")
                            Vars = list()
                        
                            if point > 0:
                                print (point,"Injection point detected in above query","\n")
                                stmnt = str(line[0]+","+line[1])
                                #print (stmnt.strip("\t"))
                                extract = re.findall(r"((\$\w*)\b)",stmnt)
                                c = 0
                        
                                for word in extract:
                                    Vars.insert(c,word[0])
                                    c += 1
                            
                                print ("Total Points found = ",Vars,"\n")
                                k = 0
                                comment = list()
                                
                                while True:
                                    
                                    print (k,"Query Statment: ",str(linetmp[i+k]).strip("\t"))
                                    tmp_str = str("//"+str(linetmp[i+k]))
                                    linetmp[i+k] = "//"+str(linetmp[i+k])
                                    ln = i+k
                                    
                                    #print (tmp_str)
                                    #print (comment)
                                    comment.append(tmp_str)
                                    #print (comment)
                                
                                    
                                    
                                    if re.search("[^*]\;",linetmp[i+k]):
                                        break
                                    k += 1
                                comment = n.join(comment)
                                print ("Vulnerable Query Commented =\n"+comment,"\n")
                                query = re.sub('[\+\'\"\;\(\)\{\}]','',query)
                                var = re.findall(r"\$\w+",query)
                                print ("Injectable Points = ",    var,"\n")
                                for q in var:
                                    query = query.replace(q,"?")
                        
                                query = '"'+query+'");'
                                print ("Fix query: ",query)
    
                                line[1] = query
                                prepare = line[0]
    
                                if not prepare.replace("mysqli_query","mysqli_prepare"):
                                    line[0] = prepare.replace("mysqli_real_query","mysqli_prepare")
                                else:
                                    line[0] = prepare.replace("mysqli_query","mysqli_prepare")
                                
                                
                                #print ("line[0] = ",line[0])
                                #print ("line[1] = ",line[1])
                                #print ("query = ",query)
                                query = line[0]+", "+query
                                print ("\nNew Query Statement= ",query,"\n")
                        
                                s=""
                                bind_var=""
                                for j in var:
                                    s = s+"s"
                                    #print (j)
                                    bind_var = bind_var+", "+j
                                    bind = "mysqli_stmt_bind_param("+Vars[0]+","+"\""+s+"\""+bind_var+");"
                    
                                #print ("bind = ",bind)
                                Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #if execute == 1:
                                #Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #else:
                                
                        
                                Fix_qry_data = linetmp[ln]+"\n"+query+"\n"+bind+"\n"+Query_Exc+"\n"
                                #print (linetmp) 
                                print ("\n"+"line[",ln,"] = ",linetmp[ln],"\n")
                                print ("[  /----------\ < Type-End End > /----------\  ]")
                                #print ("Fix_qry_data = ",Fix_qry_data)
                                linetmp[ln] = Fix_qry_data
                                
                                #print (n,"linetmp = ",linetmp)
                                Fix = n.join(linetmp)
                                #print ("Data Fix = ",Fix)
                                with open (File,"w+") as wd:
                                    wd.write(Fix)
                                    #print ("File Write")
                                with open (File,"r+") as rd:
                                    data = rd.read()
                                    #print ("data = ",data,)
                                    linetmp = data.split("\n")
                                
                                    for func in dict1:
                                        #print ("\n"+func)
                                        for indx, tmp in enumerate(linetmp):
                                            if not (re.search("(^\/\/)",tmp)):
                                                #print ("tmp = ",tmp)
                                                if re.search(func, tmp):
                                                    print (func)
                                                    print (dict1[func])
                                                    tmp = tmp.replace(func,dict1[func])
                                                    linetmp[indx] = tmp
                                            #else:
                                            #    print ("tmp = ",tmp)
                                    data = n.join(linetmp)
                                    #print("Data Fix = ",Fix_Data)
                                    with open (File,"w+") as wd:
                                        #print ("data = ",data)
                                        wd.write(data)
                                        #print ("final Write")
                                        break

                        elif Var:
                            print ("\n"+"Type-Variable: Select query detected.")
                            j = 0
                            s = " "
                            n = "\n"
                            ln = 0
                            line_list = list()
                            while True:
                        
                                #print (j,"Query Statment: ",str(linetmp[i+j]).strip("\t"))
                            
                                line_list.append(str(linetmp[i+j]).strip("\t").strip("\.").strip("\"\'"))
                                line = s.join(line_list)
                                print ("line = ",line)
                                if re.search("[^*]\;",linetmp[i+j]):
                                    break
                                j += 1
                     
                            line = line.split(",")
                        
                            lin = list()
                            if len(line) > 2:
                                for n,l in enumerate(line):
                                   if n > 0:
                                       print (l)
                                       lin.append(l)
                                       c = ","
                                lin =  c.join(lin)      
                                line[1] = lin
                            
                            query = str(line[1])
                            point = query.count("$")
                            Vars = list()
                        
                            if point > 0:
                                print (point,"Injection point detected in above query","\n")
                                stmnt = str(line[0]+","+line[1])
                                #print (stmnt.strip("\t"))
                                extract = re.findall(r"((\$\w*)\b)",stmnt)
                                c = 0
                        
                                for word in extract:
                                    Vars.insert(c,word[0])
                                    c += 1
                            
                                print ("Total Points found = ",Vars,"\n")
                                k = 0
                                comment = list()
                                
                                while True:
                                    
                                    print (k,"Query Statment: ",str(linetmp[i+k]).strip("\t"))
                                    tmp_str = str("//"+str(linetmp[i+k]))
                                    linetmp[i+k] = "//"+str(linetmp[i+k])
                                    ln = i+k
                                    
                                    #print (tmp_str)
                                    #print (comment)
                                    comment.append(tmp_str)
                                    #print (comment)
                                
                                    
                                    
                                    if re.search("[^*]\;",linetmp[i+k]):
                                        break
                                    k += 1
                                comment = n.join(comment)
                                print ("Vulnerable Query Commented =\n"+comment,"\n")
                                query = re.sub('[\+\'\"\;\(\)\{\}]','',query)
                                var = re.findall(r"\$\w+",query)
                                print ("Injectable Points = ",    var,"\n")
                                for q in var:
                                    query = query.replace(q,"?")
                        
                                query = '"'+query+'");'
                                print ("Fix query: ",query)
    
                                line[1] = query
                                prepare = line[0]

                                if not prepare.replace("mysqli_query","mysqli_prepare"):
                                    line[0] = prepare.replace("mysqli_real_query","mysqli_prepare")
                                else:
                                    line[0] = prepare.replace("mysqli_query","mysqli_prepare")
                                
                                
                                #print ("line[0] = ",line[0])
                                #print ("line[1] = ",line[1])
                                #print ("query = ",query)
                                query = line[0]+", "+query
                                print ("\nNew Query Statement= ",query,"\n")
                        
                                s=""
                                bind_var=""
                                for j in var:
                                    s = s+"s"
                                    #print (j)
                                    bind_var = bind_var+", "+j
                                    bind = "mysqli_stmt_bind_param("+Vars[0]+","+"\""+s+"\""+bind_var+");"
                    
                                #print ("bind = ",bind)
                                Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #if execute == 1:
                                #Query_Exc = "mysqli_stmt_execute("+Vars[0]+");"
                                #else:
                                
                        
                                Fix_qry_data = linetmp[ln]+"\n"+query+"\n"+bind+"\n"+Query_Exc+"\n"
                                #print (linetmp) 
                                print ("\n"+"line[",ln,"] = ",linetmp[ln],"\n")
                                print ("[  /----------\ < Type-Variable End > /----------\  ]")
                                #print ("Fix_qry_data = ",Fix_qry_data)
                                linetmp[ln] = Fix_qry_data
                                
                                #print (n,"linetmp = ",linetmp)
                                Fix = n.join(linetmp)
                                #print ("Data Fix = ",Fix)
                                with open (File,"w+") as wd:
                                    wd.write(Fix)
                                    #print ("File Write")
                                with open (File,"r+") as rd:
                                    data = rd.read()
                                    #print ("data = ",data,)
                                    linetmp = data.split("\n")
                                
                                    for func in dict1:
                                        #print ("\n"+func)
                                        for indx, tmp in enumerate(linetmp):
                                            if not (re.search("(^\/\/)",tmp)):
                                                #print ("tmp = ",tmp)
                                                if re.search(func, tmp):
                                                    print (func)
                                                    print (dict1[func])
                                                    tmp = tmp.replace(func,dict1[func])
                                                    linetmp[indx] = tmp
                                            #else:
                                            #    print ("tmp = ",tmp)
                                    data = n.join(linetmp)
                                    #print("Data Fix = ",Fix_Data)
                                    with open (File,"w+") as wd:
                                        #print ("data = ",data)
                                        wd.write(data)
                                        #print ("final Write")
                                        break


        else :
            print ("Encoding Not Detected.")
            
#Read = Analysis.load_FileRead(File)
#Analysis.file_Analysis(File)
