a = "chleb"
b = "bułki"
c = "pączki"
d = "marchew"
e = "seler"
f = "rukola"
lista_zakopow = {
    "piekarnia" : [a.capitalize(), b.capitalize(), c.capitalize()],
    "warzywniak" : [d.capitalize(), e.capitalize(), f.capitalize()]
}

for i in lista_zakopow:
    lista_sklepów = lista_zakopow[i]
    print(f"Idę do " + i.capitalize() + f", kupuję tu następujące rzeczy: {lista_sklepów}")