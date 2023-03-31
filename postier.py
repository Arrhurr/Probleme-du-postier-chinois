#Def graphe eulerien : Un graphe connexe admet un parcours eulérien si et seulement si ses sommets sont tous de degré pair sauf au plus deux
import mygraph as mg
graphe = {"A":["B","C","D","E"],
          "B":["A","C","D","E"],
          "C":["A","B","E","F"],
          "D":["A","B"],
          "E":["A","B","C"],
          "F":["C"]}

g = mg.Graphe(graphe)




def comparer_Chemin(chem1,chem2):
    if chem1==chem2[::-1]:
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

def chemin_recursif(chemin,dep,nbMax):
    liste=None
    for i in dep.aretes:
        if not ifin(chemin,dep+i):
            chemin.append(dep+i)
            liste=chemin_recursif(chemin,i)
        elif i==dep.aretes[-1]:
            return None
    if len(chemin)==nbMax:
        return chemin
    if liste is not None:
        return chemin
        

def chemin_Eulerien(g):
    impair=[]
    for som in g.all_sommets():
        if len(g.aretes(som))%2==1:
            impair.append(g)
    if len(impair)>2:
        return []
    elif len(impair)>0 and len(impair)<=2:
        dep=impair[0]
    else:
        dep=g.all_sommets()[0]
    chemin=[]
    nb=len(g.all_aretes)
    chemin=chemin_recursif(chemin,dep,nb)
    return chemin

print(chemin_Eulerien(g))