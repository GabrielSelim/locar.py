from PyQt5 import uic, QtWidgets
# from classe_reserva import Reserva
# from classe_veiculo import Veiculo
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt, QSortFilterProxyModel
# from PyQt5.QtGui import QStandardItem, QStandardItemModel
import tela_consulta_veiculo
import pymysql.cursors
from contextlib import contextmanager


#   Função que inicia a conexão com o servidor e BD
@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='locacao',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    #   Tratamento de exceção (Má Conexão)
    try:
        yield conexao
    finally:
        conexao.close()  # encerra a conexão


def consulta(sql):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            resultado = cursor.fetchone()
            print(resultado)


#   Função de inserção de dados no BD
def cadastro(sql):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            conexao.commit()
            print('\033[1;32mInserido com SUCESSO!!!\033[m')


def chama_segunda_tela():
    tela_login.label_6.setText("")
    nome_usuario = tela_login.lineEdit.text()
    senha = tela_login.lineEdit_2.text()
    if nome_usuario == "gabriel123" and senha == "123456":
        tela_login.close()
        tela_inicial.show()
    else:
        tela_login.label_6.setText("Dados de login incorretos!")


def limpar_tela_login():
    tela_login.lineEdit.clear()
    tela_login.lineEdit_2.clear()


def sair():
    tela_cadastro_veiculo.close()
    tela_cadastrar_usuario.close()
    tela_cadastro_reserva.close()
    tela_alterar_reserva_1.close()
    tela_alterar_reserva_2.close()
    tela_cadastro_consulta_veicular.close()
    tela_inicial.close()
    tela_login.show()


def voltar_tela_inicial():
    tela_cadastro_veiculo.close()
    tela_cadastrar_usuario.close()
    tela_cadastro_reserva.close()
    tela_alterar_reserva_1.close()
    tela_alterar_reserva_2.close()
    tela_cadastro_consulta_veicular.close()
    tela_inicial.show()


def buscar_reserva():
    cpf_reserva = tela_alterar_reserva_1.lineEdit_5.text()
    if cpf_reserva == "01863625100":
        tela_alterar_reserva_1.close()
        tela_alterar_reserva_2.show()
    else:
        pass


def add_cliente():
    nome_cliente = tela_cadastrar_usuario.line_nome_cliente.text()
    email_cliente = tela_cadastrar_usuario.line_email_cliente.text()
    cpf_cliente = tela_cadastrar_usuario.line_cpf_cliente.text()
    cnh_cliente = tela_cadastrar_usuario.line_cnh_cliente.text()
    if nome_cliente == "" or email_cliente == "" or cpf_cliente == "" or cnh_cliente == "":
        print("Preencha todos os Campos")
    else:
        cadastro("INSERT INTO `cliente`(`id_cpf`, `nome`, `email`, `cnh`) VALUES ('{}','{}','{}','{}')".
                 format(cpf_cliente, nome_cliente, email_cliente, cnh_cliente))
        print("Adicionado ao BD")


def limpar_add_cliente():
    tela_cadastrar_usuario.line_nome_cliente.clear()
    tela_cadastrar_usuario.line_email_cliente.clear()
    tela_cadastrar_usuario.line_cpf_cliente.clear()
    tela_cadastrar_usuario.line_cnh_cliente.clear()


def chamar_cadastro_reserva():
    tela_inicial.close()
    tela_cadastro_reserva.show()


def chamar_cadastro_veiculo():
    tela_inicial.close()
    tela_cadastro_veiculo.show()


def chamar_cadastro_usuario():
    tela_inicial.close()
    tela_cadastrar_usuario.show()


def chamar_alterar_reserva_1():
    tela_inicial.close()
    tela_alterar_reserva_1.show()


def tela_consulta_carro():
    x = tela_consulta_veiculo.tela
    tela_inicial.close()
    x.show()


def add_veiculo():
    modelo = tela_cadastro_veiculo.lineEdit.text()
    cor = tela_cadastro_veiculo.lineEdit_2.text()
    placa = tela_cadastro_veiculo.lineEdit_3.text()
    chassi = tela_cadastro_veiculo.lineEdit_4.text()
    ano = tela_cadastro_veiculo.lineEdit_5.text()
    status = tela_cadastro_veiculo.lineEdit_6.text()
    ar_condicionado = tela_cadastro_veiculo.lineEdit_7.text()
    marca = tela_cadastro_veiculo.lineEdit_8.text()
    nome = tela_cadastro_veiculo.lineEdit_9.text()
    valor_pago = tela_cadastro_veiculo.lineEdit_91.text()
    km_rodados = tela_cadastro_veiculo.lineEdit_92.text()
    tipo_combustivel = tela_cadastro_veiculo.lineEdit_93.text()
    categoria = tela_cadastro_veiculo.lineEdit_95.text()
    print(modelo, cor, placa, chassi, ano, status, nome, valor_pago, km_rodados, tipo_combustivel, categoria, marca,
          ar_condicionado)
    if modelo == "" or cor == "" or placa == "" or chassi == "" or ano == "" or status == "" or \
            ar_condicionado == "" or marca == "" or nome == "" or valor_pago == "" or km_rodados == "" or \
            tipo_combustivel == "" or categoria == "":
        print("Preencha todos os Campos")
    else:
        cadastro(
            f"INSERT INTO veiculos VALUES ('{modelo}', '{cor}', '{placa}', '{chassi}', '{ano}', '{status}', "
            f"'{ar_condicionado}', '{marca}', '{nome}', '{valor_pago}', '{km_rodados}','{categoria}', DEFAULT)")
        print("Adicionado ao BD")


def limpa_tela_cadastro_veiculo():
    tela_cadastro_veiculo.lineEdit.clear()
    tela_cadastro_veiculo.lineEdit_2.clear()
    tela_cadastro_veiculo.lineEdit_3.clear()
    tela_cadastro_veiculo.lineEdit_4.clear()
    tela_cadastro_veiculo.lineEdit_5.clear()
    tela_cadastro_veiculo.lineEdit_6.clear()
    tela_cadastro_veiculo.lineEdit_7.clear()
    tela_cadastro_veiculo.lineEdit_8.clear()
    tela_cadastro_veiculo.lineEdit_9.clear()
    tela_cadastro_veiculo.lineEdit_91.clear()
    tela_cadastro_veiculo.lineEdit_92.clear()
    tela_cadastro_veiculo.lineEdit_93.clear()
    tela_cadastro_veiculo.lineEdit_95.clear()


def reserva():
    data_retirada = tela_cadastro_reserva.lineEdit.text()
    data_devolucao = tela_cadastro_reserva.lineEdit_2.text()
    forma_pagamento = tela_cadastro_reserva.comboBox.currentText()
    qtde_diaria = tela_cadastro_reserva.lineEdit_4.text()
    cpf_cliente_reserva = tela_cadastro_reserva.lineEdit_5.text()
    valor_diaria = 300
    valor_total = int(qtde_diaria) * valor_diaria
    tela_cadastro_reserva.label7_3.setText(f'R$ {valor_total:,.2f}')
    # serviços adicionais
    seguro_veicular_1 = tela_cadastro_reserva.comboBox_4.currentText()
    seguro_veicular_2 = tela_cadastro_reserva.comboBox_3.currentText()
    seguro_veicular_3 = tela_cadastro_reserva.comboBox_5.currentText()
    cadeira_bebe = tela_cadastro_reserva.comboBox_6.currentText()
    bebe_conforto = tela_cadastro_reserva.comboBox_7.currentText()
    condutor_extra = tela_cadastro_reserva.comboBox_8.currentText()

    if data_retirada == "" or data_devolucao == "" or qtde_diaria == "" or cpf_cliente_reserva == "":
        print("Preencha todos os Campos")
    else:
        cadastro(f"INSERT INTO reserva VALUES (DEFAULT, '{data_retirada}', '{data_devolucao}', '{forma_pagamento}', "
                 f"'{qtde_diaria}', '{cpf_cliente_reserva}', '{12200}', '{seguro_veicular_1}', '{seguro_veicular_2}', "
                 f"'{seguro_veicular_3}', '{cadeira_bebe}', '{bebe_conforto}', '{condutor_extra}' )")
        print("Adicionado ao BD")


def limpar_reserva():
    tela_cadastro_reserva.lineEdit.clear()
    tela_cadastro_reserva.lineEdit_2.clear()
    tela_cadastro_reserva.lineEdit_4.clear()
    tela_cadastro_reserva.lineEdit_5.clear()


app = QtWidgets.QApplication([])

# Loads
tela_login = uic.loadUi("tela_login.ui")
tela_inicial = uic.loadUi("tela_inicial_nova.ui")
tela_cadastro_veiculo = uic.loadUi("tela_cadastrar_veiculo_nova.ui")
tela_cadastro_reserva = uic.loadUi("tela_reserva_nova.ui")
tela_alterar_reserva_1 = uic.loadUi("tela_alterar_reserva_nova.ui")
tela_alterar_reserva_2 = uic.loadUi("tela_alterar_reserva2_nova.ui")
tela_cadastrar_usuario = uic.loadUi("tela_cadastrar_cliente_nova.ui")
tela_cadastro_consulta_veicular = tela_consulta_veiculo.tela

# Button
tela_login.pushButton.clicked.connect(chama_segunda_tela)
tela_alterar_reserva_1.pushButton_3.clicked.connect(buscar_reserva)

# Button Sair
tela_inicial.pushButton_2.clicked.connect(sair)
tela_cadastro_veiculo.pushButton_3.clicked.connect(sair)
tela_cadastro_reserva.pushButton_5.clicked.connect(sair)
tela_alterar_reserva_1.pushButton_5.clicked.connect(sair)
tela_alterar_reserva_2.pushButton_5.clicked.connect(sair)
tela_cadastrar_usuario.pushButton_5.clicked.connect(sair)

tela_cadastro_consulta_veicular.pushButton_5.clicked.connect(sair)

# Button Tela Inicial
tela_cadastro_veiculo.pushButton.clicked.connect(voltar_tela_inicial)
tela_cadastro_reserva.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_alterar_reserva_1.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_alterar_reserva_2.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_cadastrar_usuario.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_cadastro_consulta_veicular.pushButton_4.clicked.connect(voltar_tela_inicial)

# Button Opções na Tela Inicial
tela_inicial.pushButton_3.clicked.connect(chamar_cadastro_veiculo)
tela_inicial.pushButton_5.clicked.connect(chamar_cadastro_reserva)
tela_inicial.pushButton_4.clicked.connect(chamar_cadastro_usuario)
tela_inicial.pushButton_4.clicked.connect(chamar_cadastro_usuario)

# tela_inicial.pushButton_7.clicked.connect(reserva)
tela_inicial.pushButton_11.clicked.connect(tela_consulta_carro)
# tela_inicial.pushButton_9.clicked.connect(reserva)
# tela_inicial.pushButton_10.clicked.connect(reserva)
# tela_inicial.pushButton_12.clicked.connect(reserva)
tela_inicial.pushButton_13.clicked.connect(chamar_alterar_reserva_1)

# Button seleciona classe do veiculo na tela de reserva (botão SUBMIT)
tela_cadastro_reserva.pushButton_2.clicked.connect(reserva)
tela_cadastro_veiculo.pushButton_2.clicked.connect(add_veiculo)
tela_cadastrar_usuario.pushButton_2.clicked.connect(add_cliente)


# Button Submit limpa as telas
tela_cadastro_reserva.pushButton_2.clicked.connect(limpar_reserva)
tela_login.pushButton.clicked.connect(limpar_tela_login)
tela_cadastro_veiculo.pushButton_2.clicked.connect(limpa_tela_cadastro_veiculo)
tela_cadastrar_usuario.pushButton_2.clicked.connect(limpar_add_cliente)

# tela_cadastro_veiculo.pushButton_2.clicked.connect(add_veiculo)

tela_login.show()
app.exec()
