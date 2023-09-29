def generate_lists_of_lists(n):
    table_list=[]
    for num in range(n):
        row=[]
        for i in range(n):
            row.append(i)
        table_list.append(row)
    return table_list
print(generate_lists_of_lists(10))
'''the space complexity of the code will be o(n^2) due to
   in 2nd for loop n elements have in each row and in 1st for loop
   that row append n times.'''