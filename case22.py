#甲队为a,b,c三人，乙队为x,y,z三人,a说他不和x比，c说他不和x,z比
for i in range (ord('x'), ord('z')+1):
    for j in range (ord('x') ,ord('z')+1):
        if i != j:
            for k in range (ord('x') ,ord('z')+1):
                if i != k and j !=k:
                    if i !=ord('x') and k!=ord('x') and k!=ord('z'):
                        print("a vs %s\t b vs %s\t c vs %s\t" % (chr(i),chr(j),chr(k))) 