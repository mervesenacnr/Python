"""
CLOSURE:
Outer fonksiyonu çağırdıktan sonra bile inner fonksiyonun outer fonksiyon scopuna erişim sağlar.
def outer():
    message = "I'm from the outside."

    def inner():
        print(message)
    return inner()

print(outer())
"""

def outer():
    msg = "this is outer function"
    def inner():
        print(msg)
    return inner()
outer()
"""
f: outer fonksiyon 
g: inner fonksiyon ;olmak üzere
f fonksiyonundaki objeye g fonksiyonundan ulaşabilmek için kullanılan bir kalıptır closer tekniği
* içteki fonksiyon dıştaki fonksiyonun scopeundaki verilere ulaşabiliyor
"""
