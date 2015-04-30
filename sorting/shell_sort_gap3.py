#shell sort
def shellSort(sample):
 print("sample=",sample)
 length = len(sample)
 gap = int(length/3)
 if (gap == 0):
  gap=1
 while(gap >= 1):
  i = gap
  while(i < length):
   value = sample[i]
   j = i
   while(j-gap >= 0 and value < sample[j - gap]):
    sample[j] = sample[j - gap]
    j -= gap
   sample[j] = value
   i+=1
  print("gap=",gap)
  gap = int(gap/3)
  print(sample)
 print("sorted sample=",sample)

sample1 = [37,22,18,50,2,3,1,29,69,5]
shellSort(sample1)
sample2 = [1,2,3,4,5,6,7,8,9]
shellSort(sample2)
sample3 = [9,8,7,6,5,4,3,2,1]
shellSort(sample3)
sample4 = [-100,-1000,200,1,500,3,-1459,-98700,3456,9]
shellSort(sample4)
sample5 = [6,5]
shellSort(sample5)
