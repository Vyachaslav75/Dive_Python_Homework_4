def kwd_only(**kwargs):
    res={}
    for key in kwargs:
        try:
            hash(kwargs[key])
            res[kwargs[key]]=key
        except:
            res[str(kwargs[key])]=key
    return res
        
        

print(kwd_only(a=1, c=[2, 3, 4], d={'w', '3', 'df'}))

