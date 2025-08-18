print("Este codigo sera para probar el algoritmo de ordenamiento llamado bubble sort")
ls=[5,4,3,2,1]
count=1
cambio=1
print("La lista original es:",ls)
#print(ls)
while(cambio!=0):
    cambio=0;
    for i in range (len(ls)-1):
        if (ls[i]>ls[i+1]):
            ls[i],ls[i+1]=ls[i+1],ls[i]
            cambio=1
            count+=1
print("En total se hicieron " ,count , "cambios")
print("La lista ya ordenada es: ", ls)


