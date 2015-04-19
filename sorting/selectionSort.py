
def selectionSort(sample):
 print("sample=",sample)
 
 for i in range(len(sample)):
  j = i+1
  minIndex = i
  while (j < len(sample)):
   if (sample[j] < sample[minIndex]):
    minIndex = j
   j+=1
  sample[i], sample[minIndex] = sample[minIndex], sample[i]
 
 print(sample)

sample1 = [14, 45, 15, 50, 72, 28, 2]
selectionSort(sample1)
sample2 = [1,2,3,4,5,6,7,8]
selectionSort(sample2)
sample3 = [8,7,6,5,4,3,3,3,2,1]
selectionSort(sample3)
sample4 = [-1,40,-1000,300,400,100,-20]
selectionSort(sample4)
