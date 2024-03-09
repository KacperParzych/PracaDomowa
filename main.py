# 5
p = 0
for liczba in range(1, 1000):
    a = []
    b = 0
    for zm in range(1, (liczba//2)+1):
        if liczba % zm == 0:
            a.append(zm)
    for zm2 in range(0, len(a)):
        b += a[zm2]
    if liczba == b:
        p += 1
print(p)
# 6
lista_liczb = [1, 2.5, 3, 4.2, 5]
for liczba2 in lista_liczb:
    kwadrat = liczba2 ** 2
    print(f"Liczba {liczba2} podniesiona do kwadratu wynosi: {kwadrat}")
# 7
lista = []
for licz in range(0, 10):
    l = int(input("Podaj liczbę: "))
    if l % 2 == 0:
        lista.append(l)
print(f"Parzyste liczby: {lista}")
# 8