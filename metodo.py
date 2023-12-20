def resta (n1,n2):
    print (n1-n2)
resta(3,4)
def operaciones(n1,n2,ope="+"):
    if (ope=="+"):
        print(f"la suma de los nros es = {n1+n2}")
    elif (ope=="-"):
        print(f"la resta de los nros es ={n1-n2}")
print( operaciones (5,6,"-"))                