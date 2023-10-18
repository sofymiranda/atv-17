ano=int(input("ano de nascimento :"))
anoatual=int(input("ano atual: "))
idade=anoatual-ano
if idade < 18:
    print(f"ainda à se alistar, daqui a {18-idade} anos")
elif idade == 18:
    print(f"você tem {idade} agora é o momento de se alistar")
else:
    print(f"você já deveria ter se alistado a {idade-18} anos")
    