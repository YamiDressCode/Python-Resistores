def IEC60062(entrada: str) -> list:
    n1,tolerancia = entrada.split()
    multiplicador = n1[-1]
    n1 = n1[:-1]
    x = 0
    Y = n1
    dicionario_cores = {'0':'Preta','1':'Marrom','2':'Vermelha','3':'Laranja','4':'Amarela','5':'Verde','6':'Azul' ,'7':'Violeta','8': 'Cinza','9': 'Branca'}
    cores = []
    if len(n1) >= 4:
        n1 = n1[:4]
    for i in range(len(n1)):
        if n1[i] in dicionario_cores:
            cores.append(dicionario_cores[n1[i]])
            if len(n1) <= 1:
                cores.append('Preta')
       
    multiplicadores = {'m':(-3),'-':-1,'K':3,'M':6,'G':9}
    for c in multiplicadores:
         x = (multiplicadores[multiplicador] - len(Y[2:]))
         if '.' in Y[2:]:
             x = (multiplicadores[multiplicador] - len(Y[3:]))
         D_multi = {-3 : 'Rosa', -2 :'Prata',-1 : 'Dourada',10 : 'Preta',1 : 'Marrom',2 : 'Vermelha',3 : 'Laranja', 4:'Amarela',5:'Verde',6:'Azul' ,7:'Violeta',8: 'Cinza',9: 'Branca'}
    if x in D_multi:
        cores.append(D_multi[x])
   
    D_tolerancia = {'20':'Nenhuma','10':'Prata','5':'Dourada','1':'Marrom','2':'Vermelha','0.05':'Laranja','0.02':'Amarela','0.5':'Verde','0.25':'Azul','0.1':'Violeta','0.01':'Cinza'}
    cores.append(D_tolerancia[tolerancia])
   
    return cores