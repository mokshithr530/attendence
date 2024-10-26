
ar= [("A", "P"), ("B", "A"), ("C", "P"), ("D", "A"), ("E", "P"), ("F", "P"), ("G", "A"), ("H", "P"), ("I", "P"), ("J", "P")]
for i in ar:
    for j in range(len(i)):
        pc=ar.count(i[j])
        ac=ar.count(i[j])
        if pc=="P":
            print(pc)
        elif ac=="A":
            print(ac)