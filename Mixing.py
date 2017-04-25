import itertools

lst2 = ["a", "b", "c","d"]
lst2 = sorted(lst2)
combs = []
lst = []
for data in lst2 :
    lst.append(":"+data+":")

for i in range(1, len(lst)+1):
    els = [list(x) for x in itertools.combinations(lst, i)]
    combs.extend(els)


result = []
print(combs)

for data in combs :
    stre = ""
    for d in data :
        stre = stre + d
    stre = stre.replace("::",":")
    stre = stre[1:]   
    stre = stre[:-1]
    result.append(stre)
result = sorted(result)
print(result)
        









