def Partition(A,first,last):
   """
   Partitions A[first:last] using as pivot
   the middle item x.  On return is (i,j,x):
   i > j, all items in A[i:last] are >= x,
   all items in A[first:j+1] are <= x.
   """
   x = A[(first+last)/2]
   i = first; j = last-1
   while i <= j:
      while A[i] < x: i = i+1
      while A[j] > x: j = j-1
      if i < j: A[i],A[j] = A[j],A[i]
      if i <= j: i = i+1; j = j-1
   return (i,j,x)

def CheckPartition(A,first,last,i,j,x):
   """
   Prints the result of the Partition
   in order to check the postconditions.
   """
   print 'i = %d, j = %d, x = %d' % (i,j,x)
   print 'A[%d:%d] =' % (first,j+1), \
      A[first:j+1], '<=', x
   print 'A[%d:%d] =' % (i,last), \
      A[i:last], '>=', x

def ItrQuickSort(A):
   """
   The iterative version of QuickSort
   uses a stack of indices in A.
   """
   S = []; S.insert(0,(0,len(A)))
   while S != []:
      if opt: print 'S =', S
      (first,last) = S.pop(0)
      (i,j,x) = Partition(A,first,last)
      if opt: CheckPartition(A,first,last,i,j,x)
      if i < last-1: S.insert(0,(i,last))
      if j > first: S.insert(0,(first,j+1))

def main():
   """
   Generates a random array of integers
   and applies quick sort.
   """
   a = input('Give lower bound : ')
   b = input('Give upper bound : ')
   n = input('How many numbers ? ')
   ans = raw_input('Trace ? (y/n) ')
   A = llista
   import copy
   B = copy.deepcopy(A)
   print 'A =', A
   QuickSort(A,0,n,ans=='y')
   print 'A =', A
   print 'Iteratively on same data'
   print 'A =', B
   ItrQuickSort(B,ans=='y')
   print 'A =', B

main()
