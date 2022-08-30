#Extraction of tags for MT101
Msg2="""{1:F01FNBCUS44A1230000000000}{2:I101BOFAUS6SX123N2}{4:
:20:091117-DSNY0001
:28D:1/1
:50H:/12345-67891
WALT DISNEY COMPANY
MOUSE STREET 1
LOS ANGELES CA 
:30:091117
:21:WDC091117RPCUS
:32B:USD377250,
:50L:WALT DISNEY COMPANY LOS ANGELES CA
:57A:WFBIUS6S
:59:/26351-38947
RIVERS PAPER COMPANY
37498 STONE ROAD
SAN RAMON CA
:71A:OUR
-}"""

count=0
start=0
end=0
length=len(Msg2)

for i in range(0,length):
  count=count+1
  if Msg2[i]=='4' and Msg2[i+1]==':':
    start=i+2
  if Msg2[i]=='-' and Msg2[i+1]=='}':
    end=i-1
    break

#Body of the message is stored in final variable

final=Msg2[start:end+1]

print(final)    

#variables to be used in conversion part 
num_50_flag="-1"
num_20="-1"
num_28D="-1"
num_23B="CRED"
num_32B="-1" #will only contain the Amount part
num_50H_id="-1"
num_50H_name="-1"
num_50H_address="-1"
num_71A="-1"
num_59_id="-1"
num_59_name="-1"



temp=0
length=len(final)

#Extracrtion of various MT101 tags

for i in range(0,length):
#Extracrtion of TAG 20
  if final[i]==':' and final[i+1]=='2'  and final[i+2]=='0' and final[i+3]==':':
    num_20=final[i+4:i+19] 

#Extracrtion of TAG 28D
  if final[i]==':' and final[i+1]=='2'  and final[i+2]=='8' and final[i+3]=='D' and final[i+4]==':':
    num_28D=final[i+5:i+8]

#Extracrtion of TAG 32B      
  if final[i]==':' and final[i+1]=='3'  and final[i+2]=='2' and final[i+3]=='B' and final[i+4]==':':
    for j in range(i+5,length):
      if(final[j]==','):
        end=j
        break
    num_32B=final[i+8:end]
    


#Extracrtion of TAG 50H  
  if final[i]==':' and final[i+1]=='5'  and final[i+2]=='0' and final[i+3]=='H' and final[i+4]==':':
    num_50_flag="H"
    for j in range(i+6,length):
      if(final[j]=="\n"):
        end=j
        break
    temp=end
    num_50H_id=final[i+6:end]
    for j in range(temp+1,length):
      if(final[j]=="\n"):
        end=j
        break
    num_50H_name=final[temp+1:end]
    temp=end+1
    for j in range(temp,length):
      if final[j]==':':
        end=j
        break
    num_50H_address=final[temp:end-1]

#Extracrtion of TAG 59    
  if final[i]==':' and final[i+1]=='5'  and final[i+2]=='9' and final[i+3]==':':
    for j in range(i+5,length):
      if final[j]=="\n":
        end=j
        break
    temp=end+1
    num_59_id=final[i+5:end]
    for j in range(temp,length):
      if final[j]=="\n":
        end=j-1
        break
    num_59_name=final[temp:end+1]    

#Extracrtion of TAG 71A
  if final[i]==':' and final[i+1]=='7'  and final[i+2]=='1' and final[i+3]=='A' and final[i+4]==':':
    num_71A=final[i+5:i+9]    

print(num_20)
print(num_28D)
print(num_23B)
print(num_32B)
print(num_50H_id)
print(num_50H_name)
print(num_50H_address) 
print(num_71A)
print(num_59_id)
print(num_59_name)

#MT to MX Conversion
#Message type MT101 -> PACS.008
#Creation of XML File using string concatenation

answer=""
answer=answer+"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Document>\n<FIToFICstmrCdtTrf>\n<CdtTrfTxInf>\n<PmtId>\n<InstrId>"""+num_20+"""</InstrId>\n</PmtId>\n<PmtTpInf>\n<LclInstrm>\n<Prtry>"""+num_23B+"""</Prtry>\n</LclInstrm>\n</PmtTpInf>"""
answer=answer+"""\n<IntrBkSttlmAmt>"""+num_32B+"""</IntrBkSttlmAmt>\n<Dbtr>\n<Nm>"""

answer=answer+num_50H_name+"""</Nm>\n<PstlAdr><AdrLine>"""+num_50H_address+"""</AdrLine>\n</PstlAdr>\n</Dbtr>"""
answer=answer+"""\n<DbtrAcct>\n<Id>\n<Othr>\n<Id>/"""+num_50H_id+"""</Id>\n</Othr>\n</Id>\n</DbtrAcct>\n<Cdtr>\n<Nm>"""+num_59_name+"""</Nm>\n</Cdtr>\n<CdtrAcct>\n<Id>\n<Othr>\n<Id>/"""+num_59_id+"""</Id>\n</Othr>\n</Id>\n</CdtrAcct>\n</CdtTrfTxInf>\n</FIToFICstmrCdtTrf>\n</Document>"""

#final output stored in answer variable

print(answer)
