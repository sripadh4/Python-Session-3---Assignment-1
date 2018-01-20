# Python-Session-3---Assignment-1
Write own function for reduce and filter

def myreduce(a, b):
    c = iter(b)
    d = next(c)
    for e in c:
        d = a(d, e)
    return (d)
    
    def myfilter(a, b):
    c = iter(b)
    for a in c:
        if a is True:
            return (a)
