def mx_validate(mx_file,error_file,count):
    error_flag=0
    my_template="""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Document>
    <FIToFICstmrCdtTrf>
    <CdtTrfTxInf>
    <PmtId>
    <InstrId>"""

    if (mx_file.find("<IntrBkSttlmAmt>")==-1) or (mx_file.find("</IntrBkSttlmAmt>")==-1):
        error_flag=1
        print(2)
    if(mx_file.find("""<Cdtr>\n<Nm>""")==-1) or (mx_file.find("</Cdtr>\n<CdtrAcct>")==-1):
        error_flag=1
        print(3)
    if(mx_file.find("""<Dbtr>\n<Nm>""")==-1) or (mx_file.find("</Nm>")==-1):
        error_flag=1
        print(4)
    if error_flag==1:
        print("Given MX file is Invalid")
        print("Error!!!")

        #Point the file1 variale to DLQ storage folder
        
        file1=open("C:\\Users\\Bug_Inspectors\\Desktop\\final_product\\DLQ\\file"+str(count)+".xml",'a')
        file1.write(mx_file)
    else:
        print("No error found")
        print("File verified successfully!!!")

        #Point the file1 variable to Output storage 
        file1=open("C:\\Users\\Bug_Inspectors\\Desktop\\final_product\\Output_Files\\file"+str(count)+".xml",'a')
        file1.write(mx_file)




