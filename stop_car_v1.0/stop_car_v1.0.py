#conexao com banco de dados

import mysql.connector

con = mysql.connector.connect(host = 'localhost', database = 'db_stcar', user = 'root', password = '@@Zekinha7')


#cadastro de veiculos

from multiprocessing.forkserver import read_signed


placa = input (str("Digite a placa do veículo de acordo com o modelo(AAA1111) ou modelo (AAA1A11): "))
modelo = input (str("Digite o modelo do veiculo: "))
montadora = input (str("Digite a montadora do veiculo: "))
ano = int (input("Digite o ano de modelo do veiculo: "))


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
    


print("---------------------------------------------------------------------------")
print(f"O veículo ficou no estacionamento por {hfinal} horas e {minfinal} minutos.")
print("---------------------------------------------------------------------------")


#definindo valores por tempo

print("-------------------------------------")
print("Lista de valores por tempo de servico")
print("-------------------------------------")

print("1 HORA ---------- R$10 REAIS\nMEIA HORA ---------- R$5 REAIS\n**Apos uma hora, a cada 15 MIN R$2,50")


if hfinal == 00:
    if minfinal >= 15 and minfinal < 30:
        valor =+ 2,50
    elif minfinal == 30:
        valor =+ 5
    elif minfinal >=30 and minfinal < 60:
        valor =+ 5
    elif minfinal < 15:
        valor =+ 2,50
elif hfinal > 0:
        if minfinal >= 15 and minfinal < 30:
            valor = (hfinal * 10) + 2,50
        elif minfinal == 30:
         valor = (hfinal * 10) + 5
        elif minfinal >=30 and minfinal < 60:
         valor = (hfinal * 10) + 5
        else:
            valor = hfinal * 10        
    
    
print("---------------------------------------------")
print(f"O valor total do servico e de: R${valor}")
print("---------------------------------------------")
  
    
#crud SQL
cursor = con.cursor()

comando = f"""INSERT INTO cadastro(placa, modelo, montadora, ano, hentrada, minentrada, hsaida, minsaida) 
VALUES ('{placa}', '{modelo}', '{montadora}', {ano}, {hentrada}, {minentrada}, {hsaida}, {minsaida})"""

cursor.execute(comando) 
con.commit()    #edita o banco de dados 


#fechando conexao com banco de dados

if con.is_connected():
    con.close()
    cursor.close()
    print("Conexao com banco de dados encerrada")

