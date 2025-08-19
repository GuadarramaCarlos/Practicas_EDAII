# practiaca.py
# Combinar
def Combinar(A, inicio, medio, fin):
    Izq=A[inicio:medio+1]
    Der=A[medio+1:fin+1]
    i,j,k=0,0,inicio
    
    print("     Funcion combinar: ","Lista izquierda:" ,Izq,"Lista derecha",Der)
    while (i < len(Izq) and j < len(Der)):
        if Izq[i] <= Der[j]:
            A[k] = Izq[i]
            print("         Se agrega ", Izq[i])
            i+=1
            
        else:
            A[k] = Der[j]
            print("         Se agrega ", Der[j])
            j+=1
            
        k+=1

    while i < len(Izq):
        print("             Elemento restante de izquierda ",Izq[i])
        A[k] = Izq[i]
        i += 1
        k += 1

    while j < len(Der):
        print("             Elemento restante de derecha ",Der[j])
        A[k] = Der[j]
        j += 1
        k += 1
def MergeSort(A,inicio,fin):
    if inicio < fin:
        medio=(inicio + fin)//2 
        print("Informacion Merge:Inicio ",inicio,"  fin",fin, "medio " ,medio," la subcadena ",A[inicio:fin])
        MergeSort(A,inicio,medio)
        MergeSort(A,medio+1,fin)
        Combinar(A,inicio,medio,fin)

ls=[15,7,3,1,6,64,90,13,4,76,89]
MergeSort(ls,0,len(ls)-1)
print(ls)