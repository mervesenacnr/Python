"""
UNICODE sistemi ile ilgili bir başka kaçış dizisi de \.N adlı kaçış dizisidir.
UNICODE sisteminde her karakterin tek ve benzersiz bir kod konumu olduğu gibi, tek ve benzersiz bir de uzun adı vardır.
Örneğin ‘a’ harfinin UNICODE sistemindeki uzun adı şudur:
LATIN SMALL LETTER A
"""
import unicodedata
print(unicodedata.name('a'))
print(unicodedata.name('Ş'))
print("\N{LATIN SMALL LETTER A}")
print("\N{LATIN CAPITAL LETTER S WITH CEDILLA}")

