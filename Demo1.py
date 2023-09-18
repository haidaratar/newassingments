# l=[10,50,60,80,900,40]
#
# l1=[20,80,2,5,7]
#
# sum=0
#
# sum=l+l1
#
# #print(sum)
#
# emp_list=[]
#
#
# for i in sum:
#     if i not in emp_list:
#         emp_list.append(i)
#
#
#
#
#
# print(emp_list)
#
#
l=['2 Atar','1 Srini','10 Vani','7 Sunil']


def custom_key(item):
    words=item.split()
    
    num=int(words[0])
    return num


l1=sorted(l,key=custom_key)
print(l1)














