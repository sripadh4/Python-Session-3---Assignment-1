
# coding: utf-8

# In[63]:

def myreduce(a, b):
    c = iter(b)
    d = next(c)
    for e in c:
        d = a(d, e)
    return (d)
    
List1 = [1, 2, 3, 4]
Answer = myreduce(lambda x, y: x * y, List1)
print (Answer)

