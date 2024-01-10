# *args: objeleri tek tek elemanlarına ayırır. Tuple'a map eder.
numbers = [1, 2, 3, 4]
print(sum(numbers))

def sum_2(*args):
    res = 0
    print(type(args))
    print(args)
    print(len(args))
    for e in args:
        for j in e:
            res+= j
    return print(res)

sum_2([1,2])

# fonksiyona değişken sayıda keyword argument verebilmemizi sağlar. Dictionary'e map eder.

def student(**kwargs):
     for v in kwargs.values():
         print(v)

student(name="Jake", student_number="401")

def weird(*args, **kwargs):
    res = 0
    for e in args:
        res += e

    for k,v in kwargs.items():
        print(k, ":", v)
    return print(res)

weird(1,2,3, name="Merve", student_number= "210")

"""
args:
Değişken sayılı parametre vermenin bir yoludur. List/Tuple objelerini unpack yapar ancak dictionary gibi objeleri
unpack yapamaz.

*args:
Tuple gibi objeyi tek tek elemanlarına ayırmaya yarar.
Argüman olarak kodlayabiliriz aklımıza.

kwargs
Fonksiyona değişken sayıda keyword argument vermemizi sağlar.

**kwargs
Dictionary objesini unpack etmesini sağlar.
"""