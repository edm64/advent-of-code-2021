#!/usr/bin/python3
with open("./inputs/input01",'r') as inputte:
    p=[int(l.strip()) for l in inputte]
print(len(['' for i in range(1,len(p)) if p[i-1]<p[i]]))
print(len(['' for i in range(3,len(p)) if sum(p[i-3:i])<sum(p[i-2:i+1])]))

