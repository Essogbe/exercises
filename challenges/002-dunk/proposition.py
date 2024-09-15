with open("in.official.txt",'r') as f:
     N = f.readline()
     N=int(N.split()[0])
     parts=[]
     for i in range(N):
         h=int(f.readline().split('\n')[0])

         total = [f.readline().split('\n')[0] for j in range(h)]
         parts.append([k.split() for k in total])

def check(elem,trace):
    """
    Check if we  have  less than 2 occurences per player
    """
    for i in elem:
        if i not in trace:
            trace[i]=0
    return trace,all(trace[i]<2 for i in elem)

def fusion(elem,diff,actual_chain,results,players):

    if elem not in actual_chain :
        trace,checked =check(elem, players)
        if checked:
            trace[elem[0]] +=1
            trace[elem[1]] += 1
            actual_chain.append(elem)
            if elem[0]==actual_chain[0][1]:# Check if the last dunker is the first dunked
                results.append(actual_chain) #We get it!
            else:
                for i,j in enumerate(diff):
                        if j[1]==elem[0]:
                            #new_list=diff[:i]+diff[i+1:]
                            fusion(j,diff[:i]+diff[i+1:],actual_chain,results,players)
def make_video(liste):
    """
    Génère toutes les chaînes possibles pour chaque élément de la liste
    """
    resultats = []


    for i, element in enumerate(liste):
        #  nouvelle liste sans l'élément de départ
        nouvelle_liste =liste[:i]+liste[i+1:]
        players = {i: 0 for i in element }#initialization
        #récursion
        fusion(element, nouvelle_liste, [], resultats,players)

    return resultats

# Affichage des résultats
for i in parts:
    result =make_video(i)

    if result:
        print(len(max(result,key=len)))
    else:
        print(0)




