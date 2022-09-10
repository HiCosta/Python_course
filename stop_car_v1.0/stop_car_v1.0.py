#cadastro de veiculos

input (str("Digite a placa do veículo de acordo com o modelo(AAA1111): "))
input (str("Digite o modelo do veiculo: "))
input (str("Digite a montadora do veiculo: "))
int (input("Digite o ano de modelo do veiculo: "))

print("-----------------------------")
print(f"Veiculo cadastrado !")
print("-----------------------------")


#definindo horario

hentrada = int(input("Digite a hora de entrada do veículo:  "))
minentrada = int(input("Digite os minutos de entrada do veículo:  "))

hsaida = int(input("Digite a hora de saída do veículo:  "))
minsaida = int(input("Digite os minutos de saída do veículo:  "))

hfinal = hsaida - hentrada
if minentrada > minsaida:
    minfinal = (minsaida + 60) - minentrada
    hfinal = 0
else:
    minfinal = minsaida - minentrada

print(f"O veículo ficou no estacionamento por {hfinal} horas e {minfinal} minutos.")
