#bubble sort

def bubbleSort(sample):
 print("sample=",sample)
 length = len(sample)
 for i in range(length-1):
  for j in range(length-i-1):
   if (sample[j] > sample[j+1]):
    sample[j], sample[j+1] = sample[j+1], sample[j]
 print("sorted=",sample)
 return sample

sample1 = [19, 2, 3, 15, 4, 10, 17, 1]
bubbleSort(sample1)
sample2 = [1, 2, 3, 4, 5, 6, 7, 8]
bubbleSort(sample2)
sample3 = [8, 7, 6, 5, 4, 3, 2, 1]
bubbleSort(sample3)
sample4 = [-1000,1000,-900,900,1,2,100,2000,45]
bubbleSort(sample4)

