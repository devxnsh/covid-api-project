str1 = "this,is,a,string"
forker="This could be a string"
spacer=" "
def strtolist(str1, spacer):

    str1=str1.replace(spacer," ")
    
    pieces=str1.split()
    return pieces
if __name__=="__main__":
    k= strtolist(forker,spacer)
    print(k)