# ------------------- SET -----------------------
# set oluşturmak:
s = {1, 2, 3, 4}
print(s)

# boş set oluşturmak:
s = {}
type(s)

l = {2, 3, 4, 5}

# boş sete liste ekleme
s = set(l)
print(s)

message = "Merhaba, orda mısın?"
s = set(message)
print(s)

# Son örnekten de anlayacağımız üzere setler kümelerdir ve ekrana yadırdığı şey küme elemanlarıdır.
# Bu yüzden setler indexlenemez!

# boş listeye eleman ekleme:

s.add(6)
print(s)

# listeden eleman silme:

s.discard(6)
print(s)

# kümeler arası fark:
print("\n")

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8 }

print("s1 =", s1,"s2 =", s2)
print("s1 - s2 = ", s1.difference(s2))
print("s2 - s1 = ", s2.difference(s1))
print(s1 - s2)
print(s2 - s1)

# s1'in s2 den farkı ile s2'nin s1 den farkının birleşimi. (s1 \ s2) U (s2 \ s1) - > s1 U s2 - (s1 n s2)

print(s1.symmetric_difference(s2))

# kümelerin kesişimi:

print(s1.intersection(s2))

# kümelerin birleşimi:

print(s1.union(s2))

# s1 ∩ s2 = Ø olup olmadığını kontrol eder

print("Kümelerin kesişimi, boş küme ise True, değilse False: ", s1.isdisjoint(s2))

# alt küme sorgulama:

print("s1, s2'nin alt kümesi ise True, değilse False:", s1.issubset(s2))

# üst küme sorgulama:

print("s1, s2'nin alt kümesi ise True, değilse False:", s1.issuperset(s2))