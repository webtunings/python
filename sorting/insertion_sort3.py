def insertionSort(sample):
 print("sample=",sample)

 for i in range(1,len(sample)):
  value = sample[i]
  j=i
  while (j!=0 and value  < sample[j-1]):
   sample[j] = sample[j-1]
   j -= 1
  sample[j] = value
 print("sorted sample=",sample)

sample1 = [1,2,3,4] 
insertionSort(sample1)
sample2 = [100,3,4,200,4,7,1000,1]
insertionSort(sample2)
sample3 = [2000,2,3000,3,44,55,22,11,10,14]
insertionSort(sample3)
sample4 = [1,2,400,-1,200,-90,12]
insertionSort(sample4)
