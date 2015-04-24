
def selectionSort(sample):
 print("sample=",sample)
 
 for i in range(len(sample)):
  print(sample)
  j = i+1
  minIndex = i
  while (j < len(sample)):
   if (sample[j] < sample[minIndex]):
    minIndex = j
   j+=1
  sample[i], sample[minIndex] = sample[minIndex], sample[i]
 
 print(sample)

sample1 = [14,19,65,99,909,13,303,67,43,88,77,66,999,72,21,23,57,35,1000,45, 15, 50, 72, 28, 2,200,1,100,-1000,2,29,32,3,1,44]
selectionSort(sample1)
