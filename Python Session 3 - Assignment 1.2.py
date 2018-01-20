
# coding: utf-8

# In[9]:

def myfilter(a, b):
    c = iter(b)
    for a in c:
        if a is True:
            return (a)
        
List1 = [1, 2, 3, 4]
result = list(filter(lambda x: x % 2 == 0, List1))
print (result)

