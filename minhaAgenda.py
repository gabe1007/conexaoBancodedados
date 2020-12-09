from sqlite3 import *
from os import *

listaOpcoes = [1, 2, 3, 4, 5, 6]

# menu de opções 
def menuOpcao():
    opcao = 0
    
    while opcao not in listaOpcoes:
        try:
            print('Escolha a opcao desejada')
            print('1 - inserir novo registro')
            print('2 - Consultar Registros')
            print('3 - Atualizar registro')
            print('4 - Consultar registro por nome')
            print('5 - Deletar registro')
            print('6 - Sair')
            opcao = int(input(''))

            if opcao in listaOpcoes:
                return opcao
        
        except:
            print('Opcao invalida, tente novamente')
            


# Realiza a conexão com o banco de dados 
def conexãoBanco():
    caminho = 'C:/Users/shank/Documents/Python/Códigos Python/SQL/Agenda.db'
    try:
        conex = connect(caminho)
    except Error as ex:
        print(ex)
    
    return conex


# Realiza a inserção de um arquivo no banco de dados 
def inserirDado(conexao, sintaxe):
    try:
        conexBanco = conexao.cursor()
        conexBanco.execute(sintaxe)
        conexao.commit()
        print('Dados inseridos com sucesso')
    except Error as ex:
        print(ex)


# Realiza uma consulta sobre os dados inseridos no banco de dados 
def consultaGeral(conexao):
    sintaxe = 'SELECT * FROM contatos'
    conexBanco = conexao.cursor()
    conexBanco.execute(sintaxe)
    resultado = conexBanco.fetchall()
    return resultado


# Realiza uma consulta parcial no banco de dados 
def consultaParcial(conexao, nome):
    sintaxe = f"SELECT * FROM contatos WHERE nome LIKE '%{nome}%'"
    conexBanco = conexao.cursor()
    conexBanco.execute(sintaxe)
    resultado = conexBanco.fetchall()
    return resultado

    
# Atualiza os registros de um banco de dados 
def atualizarDados(conexao, sintaxe):
    try:
        conexaoBanco = conexao.cursor()
        conexaoBanco.execute(sintaxe)
        conexao.commit() 
        print('Dados Atualizado com sucesso')

    except Error as ex:
        print(ex)


#main
conexao = conexãoBanco()
escolha = menuOpcao()

while escolha != 6:
    if escolha == 1:
        nome = input('Digite o nome: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')
        sintaxe = (f"INSERT INTO contatos (nome, telefone, email) VALUES ('{nome}', '{telefone}', '{email}')")
        inserirDado(conexao, sintaxe)

    if escolha == 2:
        system('cls')
        dados = consultaGeral(conexao)
        for dado in dados:
            print(f'id: {dado[0]}, Nome: {dado[1]:_<15}, Telefone: {dado[2]:_<30}, Email: {dado[3]:_<30}')

    if escolha == 3:
        nome = input('Digite o nome da pessoa que você deseja atualizar o cadastro: ')
        dados = consultaParcial(conexao, nome)
        for dado in dados:
            print(f'id: {dado[0]}, Nome: {dado[1]:_<15}, Telefone: {dado[2]:_<30}, Email: {dado[3]:_<30}')
           
        idcontato = int(input('Digite o id do contato que será atualizado: '))

        opcao = int(input('Deseja atualizar o nome? 1 - SIM   2 - NÃO\n'))
        if opcao == 1:
            novoNome = input('Digite o nome que será cadastrado: ')
            sintaxe = f"UPDATE contatos SET nome = '{novoNome}' WHERE id={idcontato}"
            atualizarDados(conexao, sintaxe)
        else:
            pass

        opcao = int(input('Deseja atualizar o número de telefone? 1 - SIM   2 - NÃO\n'))
        if opcao == 1:
            novoNumero = input('Digite o número que será cadastrado: ')
            sintaxe = f"UPDATE contatos SET telefone = '{novoNumero}' WHERE id={idcontato}"
            atualizarDados(conexao, sintaxe)
        else:
            pass

        opcao = int(input('Deseja atualizar o endereço de email? 1 - SIM   2 - NÃO\n'))
        if opcao == 1:
            novoEmail = input('Digite o email será cadastrado: ')
            sintaxe = f"UPDATE contatos SET email = '{novoEmail}' WHERE id={idcontato}"
            atualizarDados(conexao, sintaxe)
        else:
            pass

    
    if escolha == 4:
        # Variável controle serve para imprimir a mensagem 'nome não existe caso seja == 0'
        controle = 0
        nome = input('Digite o nome da pessoa que você deseja consultar o cadastro: ')
        dados = consultaParcial(conexao, nome)
        for dado in dados:
            print(f'id: {dado[0]}, Nome: {dado[1]:_<15}, Telefone: {dado[2]:_<30}, Email: {dado[3]:_<30}')
            # Caso exista registros no banco é somado 1 na variável
            controle +=1
        if controle == 0:
            print('Nome não existe no banco')
        # Zera a variável controle, para entrar zerada na próxima iteração
        elif controle == 1:
            controle -= 1

    if escolha == 5:
        controle = 0
        nome = input('Digite o nome da pessoa que você deletar o cadastro: ')
        dados = consultaParcial(conexao, nome)
        for dado in dados:
            print(f'id: {dado[0]}, Nome: {dado[1]:_<15}, Telefone: {dado[2]:_<30}, Email: {dado[3]:_<30}')
            controle +=1
        if controle == 0:
            print('Nome não existe no banco')
        else:
            controle -= 1
            idcontato = int(input('Digite o id do contato que será deletadoS: '))
            sintaxe = f"DELETE FROM contatos WHERE id={idcontato}"
            atualizarDados(conexao, sintaxe) # Função para deletar e atualizar é a mesma
        

    system('pause')
    system('cls')
    escolha = menuOpcao()
