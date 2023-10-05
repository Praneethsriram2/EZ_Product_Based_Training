def quick_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        pv=lst[0]
        left_lst=[i for i in lst if i<pv]
        '''the above line is:
            for i in lst:
                if i<pv:
                    left_lst.append(i)'''
        #left_lst=[i for i in lst[1:] if i<pv] ->u can also use thiz line
        #As the list already starts from first index u can use anyone of the above lines
        #for the above line all the elements less than pivot will be moved to left_list
        right_lst=[i for i in lst if i>pv]
        #for the above line all the elements greater than pivot will be moved to right_list
        return quick_sort(left_lst)+[pv]+quick_sort(right_lst)
lst=list(map(int,input().split()))
print(quick_sort(lst))