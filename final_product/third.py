def cbs(name,amount,cur,id):
    # Example customer
    name1="AGENTES DE BOLSA FOO AGENCIA"
    account_balance1=1000000
    currency1="EUR"
    account_id1="12345678"
    error1_flag=0
    if(name!=name1):
        error1_flag=1
    if(account_balance1<int(amount)):
        error1_flag=1
    if(currency1!=cur):
        error1_flag=1
    if(account_id1!=id):
        error1_flag=1

    return error1_flag