
def cardapio:







def reclamarpedido:

comanda=[]
garçom=[]
print(" Bem vindos ao restaurante Bartolomeu ")
print(" Escolha sua opção")
print("1- Cliente ; 2- Garçom")
aviso="INSIRA A OPÇAO "
escolha=(int(input(aviso)))
while escolha!=0:
    if escolha==1:
        nome=str(input("Qual é o seu nome para encontrarmos sua comanda ?"))
        if nome==comanda:
            print("encontrei sua comanda!",nome," Oque deseja ?")
            print("Oque deseja ?")
            print("1- Cardapio ;2-reclamar pedido ;3-gasto atual;4-Pedir conta")
        else:
            comanda=nome
            print("Bem vindo cliente !")
            print("Oque deseja ?")
            print("1- Cardapio ;2-reclamar pedido ;3-gasto atual;4-Pedir conta")
        clientepick=int(input("escolha :"))
        if clientepick==1:
            print("1-Comida ;2-bebidas ")

    if escolha==2:
        print("bem vindo garçom ")
        print(" O que deseja ?")
        print("1-Inserir pedido;2-retirar item;3-fechar conta do cliente ")




