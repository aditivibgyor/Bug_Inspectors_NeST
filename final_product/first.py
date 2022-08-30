def convert_multiple(Msg1): 
  count=0
  start=0
  end=0
  length=len(Msg1)

  for i in range(0,length):
    count=count+1
    if Msg1[i]=='4' and Msg1[i+1]==':':
      start=i+2
    if Msg1[i]=='{' and Msg1[i+1]=='5':
      end=i-2
      break


  #Body of the message is stored in final variable

  final=Msg1[start:end]
  print(final)

  #variables to be used in conversion part 
  num_50_flag="-1"
  num_20="-1"
  num_23B="-1"
  num_32A="-1" #will only contain the Amount part
  num_50K_id="-1"
  num_50K_name="-1"
  num_50K_address="-1"
  num_50A_id="-1"
  num_50A_name="-1"
  num_50A_address1="-1"
  num_50A_address2="-1"
  num_50F_id="-1"
  num_50F_name="-1"
  num_50F_address1="-1"
  num_50F_address2="-1"
  num_59_id="-1"
  num_59_name="-1"
  debtor_id="-1"
  final_name="-1"
  final_id="-1"
  temp=0
  length=len(final)


  #variables being used in validation process
  num_33B_cur="-1"
  num_36="-1"
  num_32A_cur="-1"
  num_71G_cur="-1"
  num_71A="-1"
  num_71F="-1"


  #Extracrtion of various MT103 tags

  for i in range(0,length):
  #Extracrtion of TAG 20
    if final[i]==':' and final[i+1]=='2'  and final[i+2]=='0' and final[i+3]==':':
      num_20=final[i+4:i+20] 

  #Extracrtion of TAG 23B
    if final[i]==':' and final[i+1]=='2'  and final[i+2]=='3' and final[i+3]=='B' and final[i+4]==':':
      num_23B=final[i+5:i+9]

  #Extracrtion of TAG 71G
    if final[i]==':' and final[i+1]=='7'  and final[i+2]=='1' and final[i+3]=='G' and final[i+4]==':':
      num_71G_cur=final[i+5:i+8]

  #Extracrtion of TAG 71A
    if final[i]==':' and final[i+1]=='7'  and final[i+2]=='1' and final[i+3]=='A' and final[i+4]==':':
      num_71A=final[i+5:i+8]  

  #Extracrtion of TAG 71F
    if final[i]==':' and final[i+1]=='7'  and final[i+2]=='1' and final[i+3]=='F' and final[i+4]==':':
      num_71F=final[i+5:i+8]   

  #Extracrtion of TAG 33B
    if final[i]==':' and final[i+1]=='3'  and final[i+2]=='3' and final[i+3]=='B' and final[i+4]==':':
      num_33B_cur=final[i+5:i+8]

  #Extracrtion of TAG 36
    if final[i]==':' and final[i+1]=='3'  and final[i+2]=='6' and final[i+3]==':':
      for j in range(i+4,length):
        end=j
        break
      if end!=0:
        num_36=final[i+4:end]

  #Extracrtion of TAG 32A      
    if final[i]==':' and final[i+1]=='3'  and final[i+2]=='2' and final[i+3]=='A' and final[i+4]==':':
      for j in range(i+9,length):
        if(final[j]==','):
          end=j
          break
      num_32A=final[i+14:end]
      num_32A_cur=final[i+11:i+14]

  #Extracrtion of TAG 50K    
    if final[i]==':' and final[i+1]=='5'  and final[i+2]=='0' and final[i+3]=='K' and final[i+4]==':':
      num_50_flag="K"
      for j in range(i+6,length):
        if(final[j]=="\n"):
          end=j
          break
      temp=end
      num_50K_id=final[i+6:end]
      for j in range(temp+1,length):
        if(final[j]=="\n"):
          end=j
          break
      num_50K_name=final[temp+1:end]
      temp=end+1
      for j in range(temp,length):
        if final[j]==':':
          end=j
          break
      num_50K_address=final[temp:end-1]

  #Extracrtion of TAG 50A
    if final[i]==':' and final[i+1]=='5'  and final[i+2]=='0' and final[i+3]=='A' and final[i+4]==':':
      num_50_flag="A"
      for j in range(i+6,length):
        if final[j]=="\n":
          end=j
          break
      num_50A_id=final[i+6:end]
      temp=end+1
      for j in range(temp,length):
        if final[j]=="\n":
          end=j
          break
      num_50A_name=final[temp:end]
      temp=end+1
      for j in range(temp,length):
        if final[j]=="\n":
          end=j
          break
      num_50A_address1=final[temp:end]
      temp=end+1
      for j in range(temp,length):
        if final[j]=="\n":
          end=j
          break
      num_50A_address2=final[temp:end]

  #Extracrtion of TAG 50F    
    if final[i]==':' and final[i+1]=='5'  and final[i+2]=='0' and final[i+3]=='F' and final[i+4]==':':
      num_50_flag="F"
      for j in range(i+6,length):
        if final[j]=="\n":
          end=j
          break
      num_50F_id=final[i+6:end]
      temp=end+1
      for j in range(temp,length):
        if final[j]=="\n":
          end=j
          break
      num_50F_name=final[temp+2:end]
      temp=end+1
      for j in range(temp,length):
        if final[j]=="\n":
          end=j
          break
      num_50F_address1=final[temp+2:end]
      temp=end+1
      for j in range(temp,length):
        if final[j]=="\n":
          end=j
          break
      num_50F_address2=final[temp+2:end]

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

  #final debtor parameters for CBS verification
  if (num_50_flag=="K"):
    final_name=num_50K_name
  elif(num_50_flag=="A"):
    final_name=num_50A_name
  elif(num_50_flag=="F"):
    final_name=num_50F_name  


  if (num_50_flag=="K"):
    final_id=num_50K_id
  elif(num_50_flag=="A"):
    final_id=num_50A_id
  elif(num_50_flag=="F"):
    final_id=num_50F_id

  name=final_name
  amount=num_32A
  cur=num_32A_cur
  id=final_id
  ref_id=num_20



  print(num_20)
  print(num_23B)
  print(num_32A)
  print(num_50K_id)
  print(num_50K_name)
  print(num_50K_address)
  print(num_50A_id)
  print(num_50A_name)
  print(num_50A_address1)
  print(num_50A_address2)
  print(num_50F_id)
  print(num_50F_name)
  print(num_50F_address1)
  print(num_50F_address2)
  print(num_59_id)
  print(num_59_name)
  print("\nVERIFICATION VARIABLES FOR CBS\n")
  print(ref_id)
  print(name)
  print(id)
  print(amount)
  print(cur)



  #Validation Proccess
  #To check if input message is in SWIFT-MT message format

  print(num_32A_cur)
  print(num_33B_cur)
  print(num_36)
  print(num_71G_cur)
  print(num_71A)
  print(num_71F)

  #Checking MT 103 Network Validated Rules

  #Rule C-1
  if (num_32A_cur!=num_33B_cur) and (num_36=="-1"):
    print("Invalid MT format")
    print("(Error code(s): D75)")

  #Rule C-18
  if (num_71G_cur!=num_32A_cur) and (num_71G_cur!="-1") and (num_32A_cur!="-1"):
    print("Invalid MT format")
    print("(Error code(s): C02)")

  #Rule C-14
  if(num_71A=="OUR") and (num_71F!="-1"):
    print("Invalid MT format")
    print("(Error code(s): E13)")

  elif(num_71A=="SHA") and (num_71G_cur!="-1"):
    print("Invalid MT format")
    print("(Error code(s):D50)")

  elif(num_71A=="BEN") and (num_71F=="-1"):
    print("Invalid MT format")
    print(" (Error code(s): E15)")



  #MT to MX Conversion
  #Creation of XML File using string concatenation

  answer=""
  answer=answer+"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Document>\n<FIToFICstmrCdtTrf>\n<CdtTrfTxInf>\n<PmtId>\n<InstrId>"""+num_20+"""</InstrId>\n</PmtId>\n<PmtTpInf>\n<LclInstrm>\n<Prtry>"""+num_23B+"""</Prtry>\n</LclInstrm>\n</PmtTpInf>"""
  answer=answer+"""\n<IntrBkSttlmAmt>"""+num_32A+"""</IntrBkSttlmAmt>\n<Dbtr>\n<Nm>"""
  if num_50_flag=="K":
    answer=answer+num_50K_name+"""</Nm>\n<PstlAdr><AdrLine>"""+num_50K_address+"""</AdrLine>\n</PstlAdr>\n</Dbtr>"""
    debtor_id=num_50K_id
  if num_50_flag=="A":
    answer=answer+num_50A_name+"""</Nm>\n<PstlAdr>\n<AdrLine>"""+num_50A_address1+""" """+num_50A_address2+"""</AdrLine>"""+"""\n</PstlAdr>\n</Dbtr>"""
    debtor_id=num_50A_id
  answer=answer+"""\n<DbtrAcct>\n<Id>\n<Othr>\n<Id>/"""+debtor_id+"""</Id>\n</Othr>\n</Id>\n</DbtrAcct>\n<Cdtr>\n<Nm>"""+num_59_name+"""</Nm>\n</Cdtr>\n<CdtrAcct>\n<Id>\n<Othr>\n<Id>/"""+num_59_id+"""</Id>\n</Othr>\n</Id>\n</CdtrAcct>\n</CdtTrfTxInf>\n</FIToFICstmrCdtTrf>\n</Document>"""
  #print(answer)
  return answer,ref_id,name,id,amount,cur