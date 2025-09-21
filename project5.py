def reverse_list(lst):
    reversed_lst=[]
    index=len(lst)-1
    while index >=0:
        reversed_lst.append(lst[index])
        index-=1
    return reverse_list
my_list=[1,2,3,4,5]    
reversed_my_lst=reverse_list(my_list)
print(reversed_my_lst)