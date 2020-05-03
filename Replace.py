import re
class Fix:
    def fix_Query(file, Vul_qry_data, Fix_qry_data):
        try:
            with open (file,"r+") as rd:
                data = rd.read()
                data=data.lower()
                print (data.rfind(Fix_qry_data))
                data = data.replace(Vul_qry_data, Fix_qry_data)
                print ("data = ",data)
                with open ("output.txt","w+") as wd:
                    wd.write(data)
                    print ("write file.")

                return "1"
        except:
            return "0"
