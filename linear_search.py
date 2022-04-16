# Linear searh
# WAP to search a element

def search(l,key):
    for i in l:
        if i == key:
            return True
    return False

l=[2,3,4,6,1,2,8,9,0]
key=9
print(search(l, key))

#  que : - swap an array

def swap_array(l):
    i=len(l)-1
    while i>=0:
        print(l[i])
        i -=1
    

l=[2,3,4,5,6,7,8,9]
# n=(len(l))
swap_array(l)