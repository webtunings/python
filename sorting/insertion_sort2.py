#insertion sort
#sample - list
def insertionSort(sample):
#initial sample
 print("sample=",sample)

#iterate over all elements of list
 for i in range(1,len(sample)):
 #start comparing from the ith element
  j=i
#go up to 2nd element
#compare with previous element and swap it if required
  while (j!=0 and sample[j] < sample[j-1]):
   sample[j], sample[j-1] = sample[j-1], sample[j]
   j -= 1
 #done
 print("sorted sample=",sample)

sample1 = [1,2,3,4] 
insertionSort(sample1)
sample2 = [100,3,4,200,4,7,1000,1]
insertionSort(sample2)
sample3 = [2000,2,3000,3,44,55,22,11,10,14]
insertionSort(sample3)
sample4 = [1,2,400,-1,200,-90,12]
insertionSort(sample4)
