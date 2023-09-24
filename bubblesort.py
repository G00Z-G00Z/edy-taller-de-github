def bubbleSort(arr):
    n = len(arr)
    print("Miau!!!")
    print("1"*n)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            break
#No sé que cambiar asi que dejaré este comentario
#Buenas tardes :D. De aquí que vamos a comer o qué?
