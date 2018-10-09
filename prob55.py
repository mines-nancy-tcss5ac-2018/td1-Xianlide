def prob55():
    #resolution du probleme
    c=0
    for k in range(10001):
        if islychrel(k)==True:
            c+=1
    return(c)


def solve1():
    return prob55()
    


def islychrel(i):
    #verifie si le nombre est un lychrel
    for k in range(50):
        if tpali(i+treverse(i))==True:
            return False
        else:
            i=i+treverse(i)

    return True


            
def treverse(i):
    #inverse le nombre 
    a=str(i)
    L=a[::-1]
    b=int(L)
    return(b)


    
def tpali(i):
    #vérifie si c'est i un palindrome
    L=list(str(i))
    L1=L[::-1]

    if L1==L:
        return True

    return False

assert(tpali(121))==True
assert(treverse(123))==321
assert(islychrel(47))==False
    
        
