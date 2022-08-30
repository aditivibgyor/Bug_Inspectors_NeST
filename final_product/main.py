from first import convert_multiple
from second import mx_validate
from third import cbs

import os

#point the dir_path variable towards files with input

dir_path=r'C:\Users\Bug_Inspectors\Desktop\final_product\Input_Files'
count=1
for filename in os.listdir(dir_path):
    f = os.path.join(dir_path, filename)
    if os.path.isfile(f):
        with open(f, 'r') as file:
            data = file.read()
            mx_file,ref_id,name,id,amount,cur=convert_multiple(data)
            print("----------------------------------------------------------------------------")
            mx_validate(mx_file,f,count)
            err=cbs(name,amount,cur,id)
            if err==0:
                print("Transaction Successful")
            else:
                print("CBS failed")
            count=count+1  
