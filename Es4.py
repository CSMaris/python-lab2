def function(dict):
    newdict={}
    for (task,urgency) in dict.items():
        if urgency==True:
            newdict[task]=True
    return newdict

D={}
D["call John for AmI project organization"]=True
D["buy a new mouse"]=True
D["find a present for Angelina’s birthday"]=False
D["organize mega party (last week of April)"]=False
D["book summer holidays"]=False
D["whatsapp Mary for a coffee"]=False
newD=function(D)
print(newD)


