c1 , c2 , c3 , c4 = map(int,input().split())
unique = len(set([c1 , c2 , c3 , c4]))
no_ofcol = 4-unique
print(no_ofcol)
