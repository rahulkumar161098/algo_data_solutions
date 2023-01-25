'''Given an array of n input integers return the absoute difference between the maximum and minimum element of the array [constraints:- use Selections sorting]'''

'''def selection_sort(e_list, lent):
   for i in range(lent):
      f_index=i
      for j in range(i+1, lent):
         if(e_list[j]< e_list[f_index]):
            f_index=j
      (e_list[i], e_list[f_index])= (e_list[f_index], e_list[i])



e_list= [1,6,4,8,9,12,24,76,13,45,67,43]
lent= len(e_list)
print(lent)
selection_sort(e_list, lent)
print(e_list)
added= e_list[-1]-e_list[0]
print(added)'''


# insertion sort
'''def insertionSort(list1, lth):
   for step in range(1, lth):
      key=list1[step]
      j= step-1
      print('key',key)
      print('j value',j)
      while j>=0 and key< list1[j]:
         list1[j+1]= list1[j]
         j = j - 1
      list1[j + 1] = key

list1=[1,45,76,23,4,3,65,32,65,43,32]
lth= len(list1)
insertionSort(list1, lth)
print(list1)'''
   

print('revert test')

