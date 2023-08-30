l=['t','a','t',1,2,4,5,1,2]

emp_list=[]
dup_list=[]

for i in l:
    if i not in emp_list:
        emp_list.append(i)
        
    else:
        dup_list.append(i)



print(emp_list)
print(dup_list)
    
    
    
    
    