
# definition fonction
def chiffre(n):

    a=0
    S=str(n)
    for k in S:
        a=a+int(k)
        
    return(a)

def solve(n):
    return chiffre(n)

# code à éxecuter

assert solve(23)==5
