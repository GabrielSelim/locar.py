from PyQt5 import uic, QtWidgets


def opcao_selecionada():
    opcoes = opcoes_select()
    for i in opcoes:

        if i == 'Cadastrar Veiculo':
            tela_login.close()
            tela_cadastro_veiculo.close()
            tela_alterar_reserva_1.close()
            tela_inicial.close()
            tela_cadastro_reserva.close()
            tela_alterar_reserva_2.close()
            tela_cadastro_veiculo.show()

        if i == 'Cadastrar Reserva':
            tela_login.close()
            tela_cadastro_veiculo.close()
            tela_alterar_reserva_1.close()
            tela_inicial.close()
            tela_cadastro_reserva.close()
            tela_alterar_reserva_2.close()
            tela_cadastro_reserva.show()

        if i == 'Consultar Reserva':
            tela_login.close()
            tela_cadastro_veiculo.close()
            tela_alterar_reserva_1.close()
            tela_inicial.close()
            tela_cadastro_reserva.close()
            tela_alterar_reserva_2.close()
            tela_alterar_reserva_1.show()

        if i == 'Consultar Veiculo':
            tela_login.close()
            tela_cadastro_veiculo.close()
            tela_alterar_reserva_1.close()
            tela_inicial.close()
            tela_cadastro_reserva.close()
            tela_alterar_reserva_2.close()
            print('Fazer tela')

        if i == 'Consultar Cliente':
            tela_login.close()
            tela_cadastro_veiculo.close()
            tela_alterar_reserva_1.close()
            tela_inicial.close()
            tela_cadastro_reserva.close()
            tela_alterar_reserva_2.close()
            print('Fazer tela')

        if i == 'Cadastrar Cliente':
            tela_login.close()
            tela_cadastro_veiculo.close()
            tela_alterar_reserva_1.close()
            tela_inicial.close()
            tela_cadastro_reserva.close()
            tela_alterar_reserva_2.close()
            print('Fazer tela')


def chama_segunda_tela():
    tela_login.label_6.setText("")
    nome_usuario = tela_login.lineEdit.text()
    senha = tela_login.lineEdit_2.text()
    if nome_usuario == "joao123" and senha == "123456":
        tela_login.close()
        tela_inicial.show()
    else:
        tela_login.label_6.setText("Dados de login incorretos!")


def buscar_reserva():
    cpf_reserva = tela_alterar_reserva_1.lineEdit_5.text()
    if cpf_reserva == "01863625100":
        tela_alterar_reserva_1.close()
        tela_alterar_reserva_2.show()
    else:
        pass



def opcoes_select():
    opcoes_tela_inicial = tela_inicial.opcoes_combo_box.currentText()
    opcoes_cadastro_veiculo = tela_cadastro_veiculo.opcoes_combo_box.currentText()
    opcoes_cadastro_reserva = tela_cadastro_reserva.opcoes_combo_box.currentText()
    opcoes_alterar_reserva = tela_alterar_reserva_1.opcoes_combo_box.currentText()
    opcoes_alterar_reserva1 = tela_alterar_reserva_2.opcoes_combo_box.currentText()
    lista_opcoes_selecionadas = [opcoes_tela_inicial, opcoes_cadastro_veiculo, opcoes_cadastro_reserva, opcoes_alterar_reserva, opcoes_alterar_reserva1]
    return list(lista_opcoes_selecionadas)


'''def fechar_select():
    for i in opcoes_select():
        if i == opcoes_tela_inicial:
            tela_inicial1 = uic.loadUi("tela_inicial.ui")
            return tela_inicial1

        if i == opcoes_cadastro_veiculo:
            tela_cadastro_veiculo1 = uic.loadUi("tela_cadastrar_veiculo.ui")
            return tela_cadastro_veiculo1

        if i == opcoes_cadastro_reserva:
            tela_cadastro_reserva1 = uic.loadUi("tela_reserva.ui")
            return tela_cadastro_reserva1

        if i == opcoes_alterar_reserva:
            tela_alterar_reserva_11 = uic.loadUi("tela_alterar_reserva.ui")
            return tela_alterar_reserva_11

        if i == opcoes_alterar_reserva1:
            tela_alterar_reserva_21= uic.loadUi("tela_alterar_reserva2.ui")
            return tela_alterar_reserva_21'''


app = QtWidgets.QApplication([])

# Loads
tela_login = uic.loadUi("tela_login.ui")
tela_inicial = uic.loadUi("tela_inicial.ui")
tela_cadastro_veiculo = uic.loadUi("tela_cadastrar_veiculo.ui")
tela_cadastro_reserva = uic.loadUi("tela_reserva.ui")
tela_alterar_reserva_1 = uic.loadUi("tela_alterar_reserva.ui")
tela_alterar_reserva_2 = uic.loadUi("tela_alterar_reserva2.ui")

# Button
tela_login.pushButton.clicked.connect(chama_segunda_tela)
buscar_opcoes_tela_inicial = tela_inicial.pushButton.clicked.connect(opcao_selecionada)
buscar_opcoes_cadastro_veiculo = tela_cadastro_veiculo.pushButton.clicked.connect(opcao_selecionada)
buscar_opcoes_cadastro_reserva = tela_cadastro_reserva.pushButton.clicked.connect(opcao_selecionada)
buscar_opcoes_alterar_reserva = tela_alterar_reserva_1.pushButton.clicked.connect(opcao_selecionada)
buscar_opcoes_alterar_reserva1 = tela_alterar_reserva_2.pushButton.clicked.connect(opcao_selecionada)


tela_alterar_reserva_1.pushButton_3.clicked.connect(buscar_reserva)


tela_login.show()
app.exec()
