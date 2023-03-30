# coding: utf-8
""" 
Une classe Python pour creer et manipuler des graphes
"""


from sympy import false


class Graphe(object):

    def __init__(self, graphe_dict=None):
        """ initialise un objet graphe.
	    Si aucun dictionnaire n'est
	    créé ou donné, on en utilisera un 
	    vide
        """
        if graphe_dict == None:
            graphe_dict = dict()
        self._graphe_dict = graphe_dict

    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet"""
        return self._graphe_dict[sommet]

    def all_sommets(self):
        """ retourne tous les sommets du graphe """
        return list(self._graphe_dict)
            

    def all_aretes(self):
        """ retourne toutes les aretes du graphe """
        li=[]
        for i in (list(self._graphe_dict)):
            for j in(self._graphe_dict[i]):
                li.append([i,j])
        return li
    def add_sommet(self, sommet):
        """ Si le "sommet" n'set pas déjà présent
	dans le graphe, on rajoute au dictionnaire 
	une clé "sommet" avec une liste vide pour valeur. 
	Sinon on ne fait rien.
        """
        existe=False
        i=0
        lis=list(self._graphe_dict)
        max=len(list(self._graphe_dict))
        while not existe and i<max :
            if sommet==lis[i]:
                existe=True
            i+=1
        if not existe:
            self._graphe_dict[sommet]={}
        

    def add_arete(self, arete):
        """ l'arete est de  type set, tuple ou list;
            Entre deux sommets il peut y avoir plus
	    d'une arete (multi-graphe)
        """
        for i in arete:
            self.add_sommet(i)
        for i in arete:
            for j in arete:
                if i!=j:
                    if j not in self._graphe_dict[i]:
                        self._graphe_dict[i].append(j)
    def trouve_chaine(self, sommet_dep, sommet_arr, chain=None):
        if chain is None:
            chain=[sommet_dep]
        recherch=self.aretes(chain[-1])
        if sommet_arr in recherch :
            chain.append(sommet_arr)
            return chain
        else:
            i=0
            res=chain
            while i<len(recherch) and res[-1]!=sommet_arr:
                if recherch[i] != res[-1]:
                    res=self.trouve_chaine(recherch[i],sommet_arr,chain.append(recherch[i]))
                i=i+1;
            for i in range(len(res)):
                if res[i] not in chain:
                    chain.append(res[i])
            return chain
    def trouve_tous_chemins(self, sommet_dep, sommet_arr, chem=[],chain=None):
        if chain is None:
            chain=[]
        chain.append(sommet_dep)
        recherch=self.aretes(chain[-1])
        print("ok : ",chain)
        if sommet_dep == sommet_arr:
            ok=chain[:]
            chem.append(ok)
            print("bon : ",chain)
        for i in range(len(recherch)):
            if (recherch[i] not in chain):
                self.trouve_tous_chemins(recherch[i],sommet_arr,chem=chem,chain=chain[:])
        return chem
            
    def __list_aretes(self):
        """ Methode privée pour récupérer les aretes. 
	    Une arete est un ensemble (set)
            avec un (boucle) ou deux sommets.
        """
        li=[]
        for i in (list(self._graphe_dict)):
            for j in(self._graphe_dict[i]):
                li.append([i,j])
        return li
    
    def __iter__(self):
        self._iter_obj = iter(self._graphe_dict)
        return self._iter_obj

    def __next__(self):
        """ Pour itérer sur les sommets du graphe """
        return next(self._iter_obj)

    def __str__(self):
        res = "sommets: "
        for k in self._graphe_dict.keys():
            res += str(k) + " "
        res += "\naretes: "
        for arete in self.__list_aretes():
            res += str(arete) + " "
        return res


class Graphe2(Graphe):
    def sommet_degre(self, sommet):
        """ renvoie le degre du sommet """
        res=self.aretes(sommet)
        degre= len(res)
        return degre
    def trouve_sommet_isole(self):
        """ renvoie la liste des sommets isoles """
        isoles=[]
        for i in (self._graphe.dict):
            if self.sommet_degre(i)==0:
                isoles.append(i)  
        return isoles
    def Delta(self,list):
        """ le degre maximum """
        max=0
        j=0
        k=0
        for i in (list):
            if i>max:
                max=i
                j=k
            k=k+1
        return max,j
    def list_degres(self):
        """ calcule tous les degres et renvoie un
    tuple de degres decroissant
    """
        deg=[]
        maximum=[]
        val=0
        j=0
        degres=()
        for i in (self._graphe_dict):
            deg.append(self.sommet_degre(i))
        print(deg)
        for i in range(len(deg)):
            val,j=self.Delta(deg)
            print(j)
            maximum.append(val)
            deg[j]=0
        degres=(maximum[:])
        return degres
