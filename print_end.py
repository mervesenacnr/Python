#print() fonksiyonun sep adlı özel bir parametresi bulunur. Bu parametre print() fonksiyonunda görünmese bile her zaman oradadır.

print("Bugün günlerden Salı", end="\n")
print("Bugün günlerden Salı", end=" ")
print("Bugün günlerden Salı", end=".")
print("Bugün günlerden Salı", end=".\n")

print("birinci satır\nikinci satır\nüçüncü satır")
print("birinci satır", "ikinci satır","üçüncü satır", end="\n")
print("birinci satır", "ikinci satır","üçüncü satır", sep="\n")


"""
print() fonksiyonunun end adlı özel bir parametresi daha bulunur. 
Tıpkı sep parametresi gibi, end parametresi de print() fonksiyonunda görünmese bile her zaman oradadır.
sep parametresi print() fonksiyonuna verilen parametreler birleştirilirken araya hangi karakterin gireceğini belirliyordu.
end parametresi ise bu parametrelerin sonuna neyin geleceğini belirler.
*end parametresi sadece bir karakter dizesi veya none olabilir.
"""

