from PyQt5 import uic, QtWidgets
from classe_reserva import Reserva
from classe_veiculo import Veiculo
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import tela_consulta_veicular


def chama_segunda_tela():
    tela_login.label_6.setText("")
    nome_usuario = tela_login.lineEdit.text()
    senha = tela_login.lineEdit_2.text()
    if nome_usuario == "gabriel123" and senha == "123456":
        tela_login.close()
        tela_inicial.show()
    else:
        tela_login.label_6.setText("Dados de login incorretos!")


def sair():
    tela_cadastro_veiculo.close()
    tela_cadastrar_usuario.close()
    tela_cadastro_reserva.close()
    tela_alterar_reserva_1.close()
    tela_alterar_reserva_2.close()
    #tela_inicial.close()
    tela_login.show()


def voltar_tela_inicial():
    tela_cadastro_veiculo.close()
    tela_cadastrar_usuario.close()
    tela_cadastro_reserva.close()
    tela_alterar_reserva_1.close()
    tela_alterar_reserva_2.close()
    tela_inicial.show()


def buscar_reserva():
    cpf_reserva = tela_alterar_reserva_1.lineEdit_5.text()
    if cpf_reserva == "01863625100":
        tela_alterar_reserva_1.close()
        tela_alterar_reserva_2.show()
    else:
        pass


Veiculo.valor_diaria = 300


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


def suported():
    tela_inicial.close()
    suporte.tela.show()


def reserva():
    forma_pagamento = tela_cadastro_reserva.comboBox.currentText()
    qtde_diaria = tela_cadastro_reserva.lineEdit_4.text()
    veiculo_escolhido = tela_cadastro_reserva.comboBox_2.currentText()
    cpf_cliente_reserva = tela_cadastro_reserva.lineEdit_5.text()
    valor_total = int(qtde_diaria) * Veiculo.valor_diaria
    tela_cadastro_reserva.label7_3.setText(f'R$ {valor_total:,.2f}')
    print(forma_pagamento, qtde_diaria, cpf_cliente_reserva, valor_total, veiculo_escolhido)


app = QtWidgets.QApplication([])

# Loads
tela_login = uic.loadUi("tela_login.ui")
tela_inicial = uic.loadUi("tela_inicial_nova.ui")
tela_cadastro_veiculo = uic.loadUi("tela_cadastrar_veiculo_nova.ui")
tela_cadastro_reserva = uic.loadUi("tela_reserva_nova.ui")
tela_alterar_reserva_1 = uic.loadUi("tela_alterar_reserva_nova.ui")
tela_alterar_reserva_2 = uic.loadUi("tela_alterar_reserva2_nova.ui")
tela_cadastrar_usuario = uic.loadUi("tela_cadastrar_cliente_nova.ui")

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

# Button Tela Inicial
tela_cadastro_veiculo.pushButton.clicked.connect(voltar_tela_inicial)
tela_cadastro_reserva.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_alterar_reserva_1.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_alterar_reserva_2.pushButton_4.clicked.connect(voltar_tela_inicial)
tela_cadastrar_usuario.pushButton_4.clicked.connect(voltar_tela_inicial)

# Button Opções
tela_inicial.pushButton_3.clicked.connect(chamar_cadastro_veiculo)
tela_inicial.pushButton_5.clicked.connect(chamar_cadastro_reserva)
tela_inicial.pushButton_4.clicked.connect(chamar_cadastro_usuario)

#tela_inicial.pushButton_7.clicked.connect(reserva)
tela_inicial.pushButton_11.clicked.connect(suported)
#tela_inicial.pushButton_9.clicked.connect(reserva)
#tela_inicial.pushButton_10.clicked.connect(reserva)
#tela_inicial.pushButton_12.clicked.connect(reserva)
tela_inicial.pushButton_13.clicked.connect(chamar_alterar_reserva_1)

# Button seleciona classe do veiculo na tela de reserva (botão SUBMIT)
tela_cadastro_reserva.pushButton_2.clicked.connect(reserva)

tela_login.show()
app.exec()
