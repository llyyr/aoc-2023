s=lambda l:l[-1]+s([*map(lambda x,y:y-x,l,l[1:])])if any(l)else 0;print(*(sum(s(l[::d])for l in[[*map(int,l.split())]for l in open('09.txt')])for d in(1,-1)))
