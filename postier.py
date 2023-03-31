#Def graphe eulerien : Un graphe connexe admet un parcours eulérien si et seulement si ses sommets sont tous de degré pair sauf au plus deux
def comparer_Chemin(chem1,chem2):
    if chem1==chem2[::-1] or chem1==chem2:
        return True
    else:
        return False
    
def ifin(liste,arrete):
    existe=False
    i=0
    while i<len(liste) and not existe:
        if(comparer_Chemin(arrete,liste[i])):
            return True
        i+=1
    return False

def chemin_recursif(chemin,dep,nbMax,g):
    liste=None
    if len(chemin)==nbMax:
        return chemin
    for i in g.aretes(dep):
        if not ifin(chemin,dep+i):
            chemin.append(dep+i)
            liste=chemin_recursif(chemin,i,nbMax,g)
        elif i==g.aretes(dep)[-1]:
            return chemin
        

def chemin_Eulerien(g):
    impair=[]
    for som in g.all_sommets():
        if len(g.aretes(som))%2==1:
            impair.append(som)
    if len(impair)>2:
        return []
    elif len(impair)>0 and len(impair)<=2:
        dep=impair[0]
    else:
        dep=g.all_sommets()[0]
    chemin=[]
    nb=len(g.all_aretes())
    chemin=chemin_recursif(chemin,dep,nb,g)
    return chemin