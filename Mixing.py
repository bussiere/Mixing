import itertools



data = {"categories":[{"category":"french"},{"category":"60fps"},{"category":"amateur"},{"category":"amateur-gay"},{"category":"arab"},{"category":"asian-gay"},{"category":"asian"},{"category":"babysitter"},{"category":"bareback-gay"},{"category":"bear-gay"},{"category":"behind-the-scenes"},{"category":"babe"},{"category":"big-dick-gay"},{"category":"bisexual"},{"category":"black-gay"},{"category":"ebony"},{"category":"blonde"},{"category":"blowjob-gay"},{"category":"bondage"},{"category":"handjob"},{"category":"brazilian"},{"category":"british"},{"category":"brunette"},{"category":"bukkake"},{"category":"cartoon"},{"category":"casting"},{"category":"celebrity"},{"category":"college"},{"category":"compilation"},{"category":"compilation-gay"},{"category":"cosplay"},{"category":"creampie-gay"},{"category":"cuckold"},{"category":"cumshot-gay"},{"category":"czech"},{"category":"daddy-gay"},{"category":"described-video"},{"category":"double-penetration"},{"category":"funny"},{"category":"cumshots"},{"category":"creampie"},{"category":"public"},{"category":"euro"},{"category":"euro-gay"},{"category":"exclusive"},{"category":"college-gay"},{"category":"feet"},{"category":"squirt"},{"category":"party"},{"category":"fetish"},{"category":"fetish-gay"},{"category":"fisting"},{"category":"gangbang"},{"category":"gay"},{"category":"german"},{"category":"pov"},{"category":"big-ass"},{"category":"big-tits"},{"category":"bbw"},{"category":"big-dick"},{"category":"group-gay"},{"category":"handjob-gay"},{"category":"hardcore"},{"category":"hentai"},{"category":"hunks-gay"},{"category":"indian"},{"category":"interracial"},{"category":"interracial-gay"},{"category":"italian"},{"category":"japanese"},{"category":"japanese-gay"},{"category":"jock-gay"},{"category":"korean"},{"category":"latina"},{"category":"latino-gay"},{"category":"lesbian"},{"category":"massage"},{"category":"massage-gay"},{"category":"masturbation"},{"category":"mature"},{"category":"mature-gay"},{"category":"solo-male-gay"},{"category":"threesome"},{"category":"milf"},{"category":"muscle-gay"},{"category":"music"},{"category":"old-young"},{"category":"panda-style"},{"category":"parody"},{"category":"orgy"},{"category":"small-tits"},{"category":"blowjob"},{"category":"pissing"},{"category":"pornstar"},{"category":"hd-porn"},{"category":"pornstar-gay"},{"category":"for-women"},{"category":"pov-gay"},{"category":"public-gay"},{"category":"pussy-licking"},{"category":"reality"},{"category":"reality-gay"},{"category":"vintage"},{"category":"rough-sex-gay"},{"category":"red-head"},{"category":"russian-1"},{"category":"school"},{"category":"toys"},{"category":"rough-sex"},{"category":"sfw"},{"category":"smoking"},{"category":"anal"},{"category":"solo-male"},{"category":"straight-guys-gay"},{"category":"striptease"},{"category":"teen"},{"category":"shemale"},{"category":"twink-gay"},{"category":"uncut-gay"},{"category":"uniforms"},{"category":"verified-amateurs"},{"category":"vintage-gay"},{"category":"vr"},{"category":"vr-gay"},{"category":"webcam-gay"},{"category":"webcam"}]}
liste = []

for d in data['categories'] :
    liste.append(d['category'])



lst2 = ["a", "b", "c","d"]
lst2 = liste
lst2 = sorted(lst2)
combs = []
lst = []
for data in lst2 :
    lst.append(":"+data+":")
deep = len(lst)+1
for i in range(1, 5):
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
        









