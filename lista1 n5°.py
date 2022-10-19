import math


medida = float(input("digite quantos metros quadrados"))
litros = medida / 6
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)
preco_latas = latas * 80
preco_galoes = galoes * 25
combinacao = (litros // 18) * 80 + (math.ceil(((litros % 18) / 3.6)) * 25)


print("O preço só com latas é:", preco_latas)
print("O peço só com galões é:", preco_galoes)
print("O preço com a combinação é:", combinacao)