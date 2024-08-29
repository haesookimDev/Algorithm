def solution(polynomial):
    answer = ''
    polynomial = polynomial.split(' ')
    x = 0
    c = 0
    for i in polynomial:
        if 'x' in i:
            if len(i)==1:
                x+=1
            else:
                x+=int(i[:-1])
        elif i.isdigit():
            c+=int(i)
    x=str(x)+'x'
    
    if x=='1x':
        x='x'
    if x=='0x':
        x='0'
    c=str(c)
            
    if c=='0' and x!='0':
        return x
    elif c!='0' and x=='0':
        return c
    elif c!='0' and x!='0':
        return x+' + '+c
    else:
        return 0