print("Lista zakupów")
a = "chleb"
b = "bułki"
c = "pączki"
d = "marchew"
e = "sałata"
f = "rukola"
lista_zakopow = {
    "piekarnia" : [a.capitalize(), b.capitalize(), c.capitalize()],
    "warzywniak" : [d.capitalize(), e.capitalize(), f.capitalize()]
}

for i in lista_zakopow:
    lista_sklepów = lista_zakopow[i]
    print(f"Idę do " + i.capitalize() + f", kupuję tu następujące rzeczy: {lista_sklepów}")

produkty = len(lista_zakopow.get("piekarnia")+lista_zakopow.get("warzywniak"))
print(f"W sumie kupuję {produkty} produktów")  
