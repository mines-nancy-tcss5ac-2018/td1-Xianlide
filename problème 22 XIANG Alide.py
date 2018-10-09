
def sousfonction(i):
    score1=0
    for k in i[1:len(i)-1]:
        score1=score1 + (ord(k)-64)
    return(score1)
    
def prob22():
    f = open("p022_names.txt" , "r")
    L=[]
    for k in f:
        L=L+k.split(',')   
    Lb=sorted(L)
    score=0
    
    for k in range(len(Lb)):

        nom=Lb[k]
        score += (k+1)*sousfonction(nom)
        
    return score

def solve():
    return prob22()

assert(sousfonction('"COLIN"'))==53
            
            
            
        
    
    


    
