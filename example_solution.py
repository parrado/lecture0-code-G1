nLoad=4

p=[0.0]*nLoad
#p=[None]*nLoad
#p=[]

for i in range(nLoad):
    p[i]=float(input(f'Ingrese potencia para carga {i+1} en vatios: '))
    #p.append(float(input(f'Ingrese potencia para carga {i+1} en vatios: ')))

#print(p)
vIn=170.0
iTotal=0.0
for j in range(len(p)):
    i=p[j]/vIn
    iTotal=iTotal+i

print(f'La corriente total es {iTotal} A')

maxI=20

if iTotal>=maxI:
    print('Se disparó el breaker!!!!')
else:
    print('Todo bien')

