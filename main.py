from PyQt5 import uic, QtWidgets
# from classe_reserva import Reserva
# from classe_veiculo import Veiculo
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt, QSortFilterProxyModel
# from PyQt5.QtGui import QIcon, QPixmap
# from PyQt5.QtCore import  pyqtSlot
# from PyQt5.QtPrintSupport import *
# import os,sys
# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
# import tela_consulta_veiculo
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
            return cursor.fetchone()


def pega_pega_dados(sql):
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()


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
    x = pega_pega_dados(f"SELECT acesso FROM usuario WHERE login = '{nome_usuario}' AND senha = '{senha}'")
    if x:
        tela_login.close()
        tela_inicial.show()
    else:
        tela_login.label_6.setText("Dados de login incorretos!")
        QMessageBox.information(QMessageBox(), "Alerta", "Dados inseridos não existentes")


def limpar_tela_login():
    tela_login.lineEdit.clear()
    tela_login.lineEdit_2.clear()


def sair():
    tela_cadastro_veiculo.close()
    tela_cadastrar_usuario.close()
    tela_cadastro_reserva.close()
    tela_alterar_reserva_1.close()
    tela_alterar_reserva_2.close()
    tela_cadastro_consulta_veicular_1.close()
    tela_cadastro_consulta_veicular_2.close()
    tela_inicial.close()
    tela_login.show()


def voltar_tela_inicial():
    tela_cadastro_veiculo.close()
    tela_cadastrar_usuario.close()
    tela_cadastro_reserva.close()
    tela_alterar_reserva_1.close()
    tela_alterar_reserva_2.close()
    tela_cadastro_consulta_veicular_1.close()
    tela_cadastro_consulta_veicular_2.close()
    tela_inicial.show()


def buscar_reserva():
    cpf_reserva = tela_alterar_reserva_1.lineEdit_5.text()
    if cpf_reserva == "":
        QMessageBox.information(QMessageBox(), "Erro", "Preencha todos os Campos Corretamente ou CPF não cadastrado")
    else:
        pega = pega_pega_dados(f"SELECT `data_retirada`, `data_devolucao`, `forma_pagamento`, `quantidade_diaria`, "
                               f"`fk_cliente_cpf`, `fk_id_veiculo`, `seguro_1`, `seguro_2`, `seguro_3`, `cadeira_bebe`,"
                               f"`bebe_conforto`, `condutor_extra` FROM `reserva` WHERE fk_cliente_cpf = {cpf_reserva}")
        for linha, dados in enumerate(pega):
            for x, values in enumerate(dados.items()):
                tela_alterar_reserva_1.close()
                tela_alterar_reserva_2.show()
                if x == 0:
                    tela_alterar_reserva_2.lineEdit.setText(str(values[1]))
                if x == 1:
                    tela_alterar_reserva_2.lineEdit_2.setText(str(values[1]))
                if x == 2:
                    tela_alterar_reserva_2.comboBox.setCurrentText(str(values[1]))

                if x == 3:
                    tela_alterar_reserva_2.lineEdit_4.setText(str(values[1]))

                if x == 4:
                    tela_alterar_reserva_2.label_4.setText(cpf_reserva)

                if x == 5:
                    tela_alterar_reserva_2.comboBox_2.setCurrentText(str(values[1]))

                if x == 6:
                    tela_alterar_reserva_2.comboBox_4.setCurrentText(str(values[1]))

                if x == 7:
                    tela_alterar_reserva_2.comboBox_3.setCurrentText(str(values[1]))

                if x == 8:
                    tela_alterar_reserva_2.comboBox_5.setCurrentText(str(values[1]))

                if x == 9:
                    tela_alterar_reserva_2.comboBox_6.setCurrentText(str(values[1]))

                if x == 10:
                    tela_alterar_reserva_2.comboBox_7.setCurrentText(str(values[1]))

                if x == 11:
                    tela_alterar_reserva_2.comboBox_8.setCurrentText(str(values[1]))


def limpar_buscar_reserva():
    tela_alterar_reserva_1.lineEdit_5.clear()


def alterar_dados_reserva_2():
    data_retirada = tela_alterar_reserva_2.lineEdit.text()
    data_devolucao = tela_alterar_reserva_2.lineEdit_2.text()
    forma_pagamento = tela_alterar_reserva_2.comboBox.currentText()
    qtde_diaria = tela_alterar_reserva_2.lineEdit_4.text()
    cpf_cliente_reserva = tela_alterar_reserva_2.label_4.text()
    valor_diaria = 300
    valor_total = int(qtde_diaria) * valor_diaria
    tela_alterar_reserva_2.label7_3.setText(f'R$ {valor_total:,.2f}')
    # serviços adicionais
    seguro_veicular_1 = tela_alterar_reserva_2.comboBox_4.currentText()
    seguro_veicular_2 = tela_alterar_reserva_2.comboBox_3.currentText()
    seguro_veicular_3 = tela_alterar_reserva_2.comboBox_5.currentText()
    cadeira_bebe = tela_alterar_reserva_2.comboBox_6.currentText()
    bebe_conforto = tela_alterar_reserva_2.comboBox_7.currentText()
    condutor_extra = tela_alterar_reserva_2.comboBox_8.currentText()

    if data_retirada == "" or data_devolucao == "" or qtde_diaria == "" or cpf_cliente_reserva == "":
        print("Preencha todos os Campos")
        QMessageBox.information(QMessageBox(), "Erro", "Preencha todos os Campos")
    else:
        cadastro(f"UPDATE `reserva` SET `data_retirada`='{data_retirada}',`data_devolucao`='{data_devolucao}',"
                 f"`forma_pagamento`='{forma_pagamento}', `quantidade_diaria`='{qtde_diaria}',`fk_id_veiculo`= {12200},"
                 f"`seguro_1`='{seguro_veicular_1}',`seguro_2`='{seguro_veicular_2}',`seguro_3`='{seguro_veicular_3}',"
                 f"`cadeira_bebe`='{cadeira_bebe}',`bebe_conforto`='{bebe_conforto}',"
                 f"`condutor_extra`='{condutor_extra}' WHERE fk_cliente_cpf = {cpf_cliente_reserva}")
        print("Adicionado ao BD")
        QMessageBox.information(QMessageBox(), "Cadastro de Reserva", "O cadastro ao BD foi alterado com sucesso")


def limpar_alterar_dados_reserva_2():
    tela_alterar_reserva_2.lineEdit.clear()
    tela_alterar_reserva_2.lineEdit_2.clear()
    tela_alterar_reserva_2.lineEdit_4.clear()
    tela_alterar_reserva_2.label_4.clear()


def add_cliente():
    nome_cliente = tela_cadastrar_usuario.line_nome_cliente.text()
    email_cliente = tela_cadastrar_usuario.line_email_cliente.text()
    cpf_cliente = tela_cadastrar_usuario.line_cpf_cliente.text()
    cnh_cliente = tela_cadastrar_usuario.line_cnh_cliente.text()
    if nome_cliente == "" or email_cliente == "" or cpf_cliente == "" or cnh_cliente == "":
        print("Preencha todos os Campos")
        QMessageBox.information(QMessageBox(), "Erro", "Preencha todos os Campos")

    else:
        cadastro("INSERT INTO `cliente`(`id_cpf`, `nome`, `email`, `cnh`) VALUES ('{}','{}','{}','{}')".
                 format(cpf_cliente, nome_cliente, email_cliente, cnh_cliente))
        print("Adicionado ao BD")
        QMessageBox.information(QMessageBox(), "Cadastro de Cliente", "O cadastro ao BD foi realizado com sucesso")


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
    x = tela_cadastro_consulta_veicular_1
    tela_inicial.close()
    x.show()


def add_veiculo():
    modelo = tela_cadastro_veiculo.comboBox_2.currentText()
    cor = tela_cadastro_veiculo.lineEdit_2.text()
    placa = tela_cadastro_veiculo.lineEdit_3.text()
    chassi = tela_cadastro_veiculo.lineEdit_4.text()
    ano = tela_cadastro_veiculo.lineEdit_5.text()
    status = tela_cadastro_veiculo.lineEdit_6.text()
    ar_condicionado = tela_cadastro_veiculo.comboBox_3.currentText()
    marca = tela_cadastro_veiculo.lineEdit_8.text()
    nome = tela_cadastro_veiculo.lineEdit_9.text()
    valor_pago = tela_cadastro_veiculo.lineEdit_91.text()
    km_rodados = tela_cadastro_veiculo.lineEdit_92.text()
    tipo_combustivel = tela_cadastro_veiculo.comboBox_4.currentText()
    preco_aluguel = tela_cadastro_veiculo.lineEdit_95.text()
    if cor == "" or placa == "" or chassi == "" or ano == "" or status == "" or marca == "" or nome == "" \
            or valor_pago == "" or km_rodados == "" or preco_aluguel == "":
        print("Preencha todos os Campos")
        QMessageBox.information(QMessageBox(), "Erro", "Preencha todos os Campos")
    else:
        cadastro(
            f"INSERT INTO veiculos VALUES ('{modelo}', '{cor}', '{placa}', '{chassi}', '{ano}', '{status}', "
            f"'{ar_condicionado}', '{marca}', '{nome}', '{valor_pago}', '{km_rodados}',"
            f"'{tipo_combustivel}','{preco_aluguel}', DEFAULT)")
        print("Adicionado ao BD")
        QMessageBox.information(QMessageBox(), "Cadastro de Veiculo", "O cadastro ao BD foi realizado com sucesso")


def limpa_tela_cadastro_veiculo():
    tela_cadastro_veiculo.lineEdit_2.clear()
    tela_cadastro_veiculo.lineEdit_3.clear()
    tela_cadastro_veiculo.lineEdit_4.clear()
    tela_cadastro_veiculo.lineEdit_5.clear()
    tela_cadastro_veiculo.lineEdit_6.clear()
    tela_cadastro_veiculo.lineEdit_8.clear()
    tela_cadastro_veiculo.lineEdit_9.clear()
    tela_cadastro_veiculo.lineEdit_91.clear()
    tela_cadastro_veiculo.lineEdit_92.clear()
    tela_cadastro_veiculo.lineEdit_95.clear()


def consulta_veiculo():
    texto_selecionado = tela_cadastro_consulta_veicular_1.comboBox_2.currentText()
    pega = pega_pega_dados(f"SELECT `id_veiculo`, `nome`, `preco_locacao`,  `modelo`, `cor`, `placa`,`ar_condicionado`,"
                           f" `marca`, `km_rodados`, `tipo_combustivel` FROM `veiculos`"
                           f"WHERE modelo = '{texto_selecionado}'")

    tela_cadastro_consulta_veicular_2.tableWidget.setRowCount(0)
    for linha, dados in enumerate(pega):
        tela_cadastro_consulta_veicular_2.tableWidget.insertRow(linha)
        for x, values in enumerate(dados.items()):
            tela_cadastro_consulta_veicular_2.tableWidget.setItem(linha, x, QTableWidgetItem(str(values[1])))


def consulta_veiculo_troca_tela():
    tela_cadastro_consulta_veicular_1.close()
    tela_cadastro_consulta_veicular_2.show()


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
        QMessageBox.information(QMessageBox(), "Erro", "Preencha todos os Campos")
    else:
        cadastro(f"INSERT INTO reserva VALUES (DEFAULT, '{data_retirada}', '{data_devolucao}', '{forma_pagamento}', "
                 f"'{qtde_diaria}', '{cpf_cliente_reserva}', '{12200}', '{seguro_veicular_1}', '{seguro_veicular_2}', "
                 f"'{seguro_veicular_3}', '{cadeira_bebe}', '{bebe_conforto}', '{condutor_extra}' )")
        print("Adicionado ao BD")
        QMessageBox.information(QMessageBox(), "Cadastro de Reserva", "O cadastro ao BD foi realizado com sucesso")


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
# tela_cadastro_consulta_veicular = tela_consulta_veiculo.tela
tela_cadastro_consulta_veicular_1 = uic.loadUi("tela_consulta_veiculo_modificada.ui")
tela_cadastro_consulta_veicular_2 = uic.loadUi("tela_consulta_veiculo_2.ui")

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
tela_cadastro_consulta_veicular_1.pushButton_5.clicked.connect(sair)
tela_cadastro_consulta_veicular_2.pushButton_5.clicked.connect(sair)

# Button Tela Inicial
tela_cadastro_veiculo.pushButton.clicked.connect(voltar_tela_inicial)
tela_cadastro_reserva.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_alterar_reserva_1.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_alterar_reserva_2.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_cadastrar_usuario.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_cadastro_consulta_veicular_1.botao_tela_inicial.clicked.connect(voltar_tela_inicial)
tela_cadastro_consulta_veicular_2.pushButton_4.clicked.connect(voltar_tela_inicial)

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

# Button (botão SUBMIT)
tela_cadastro_reserva.pushButton_2.clicked.connect(reserva)
tela_cadastro_veiculo.pushButton_2.clicked.connect(add_veiculo)
tela_cadastrar_usuario.pushButton_2.clicked.connect(add_cliente)
tela_cadastro_consulta_veicular_1.pushButton_2.clicked.connect(consulta_veiculo)

tela_cadastro_consulta_veicular_1.pushButton_2.clicked.connect(consulta_veiculo_troca_tela)
tela_alterar_reserva_2.pushButton_2.clicked.connect(alterar_dados_reserva_2)


# Button Submit limpa as telas
tela_cadastro_reserva.pushButton_2.clicked.connect(limpar_reserva)
tela_login.pushButton.clicked.connect(limpar_tela_login)
tela_cadastro_veiculo.pushButton_2.clicked.connect(limpa_tela_cadastro_veiculo)
tela_cadastrar_usuario.pushButton_2.clicked.connect(limpar_add_cliente)
tela_alterar_reserva_2.pushButton_2.clicked.connect(limpar_alterar_dados_reserva_2)
tela_alterar_reserva_1.pushButton_3.clicked.connect(limpar_buscar_reserva)

# tela_cadastro_veiculo.pushButton_2.clicked.connect(add_veiculo)

tela_login.show()
app.exec()
