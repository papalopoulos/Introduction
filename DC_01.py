def arithmetic_arranger(problems,SN=False):
    
    import re
    
    up=[]
    operand=[]
    down=[]
    
    if len(problems)>5:
        return 'Error: Too many problems.'
       
    for pivot in problems:
        separate=tuple(pivot)
        
        if '*' in separate:
            return "Error: Operator must be '+' or '-'."
        elif '/' in separate:
            return "Error: Operator must be '+' or '-'."
    
    digit=re.search('[a-zA-Z]', str(problems))
    if digit:
       return 'Error: Numbers must only contain digits.'
   
    fourdig=re.split('\s',str(problems))
    for pivot1 in fourdig:
        ooo=''.join(re.findall("\d",pivot1))
        if len(ooo)>4:
            return 'Error: Numbers cannot be more than four digits.'
    
    for pivot2 in problems:
        val=pivot2.split()
        up.append(val[0])
        operand.append(val[1])
        down.append(val[2])
    
    sure0=tuple(problems) 
    pivotador=[]
    for pivot3 in sure0:
        ourg1=re.split('\s',str(pivot3))
        pivotador.append(ourg1)
        
    result=[]
    for pivot4 in pivotador:
        if '+' in pivot4:
            operation=int(pivot4[0])+int(pivot4[2])
            result.append(operation)
        elif '-' in pivot4:
            operation=int(pivot4[0])-int(pivot4[2])
            result.append(operation)
    
    maxlen=max(len(up),len(down)) 
    rte=zip(up,operand,down)
    dic=list(rte)
    priqui=[]
    for u, op, don in dic:
        priqui.append(str(op)+' '+str(don).rjust(max(len(u),len(don))))

    
    up1=''
    down1=''
    stripes=''
    resultado=''
    maxlen1=[]
    for r in up:
        up1+= ''+r.rjust(maxlen+7)
    
    for t in priqui:
        down1+=''+t.rjust(maxlen+7)
    
    for y in result:
        resultado+= ''+str(y).rjust(maxlen+7)
    
    for reti in pivotador:
        maxlen1+=str(max(len(reti[0]),len(reti[2])))
    
    for xd in maxlen1:
        ret=int(xd)
        sep=str('-'*(ret+2)).rjust(maxlen+7)
        stripes+=''+sep
    
    if SN:
        print(up1,'\n'+down1,'\n'+stripes,'\n'+resultado)
    else:
        print(up1,'\n'+down1,'\n'+stripes)