from PyQt5 import uic, QtWidgets


def opcao_selecionada():
    opcoes = tela.opcoes_combo_box.currentText()
    if opcoes == 'Cadastrar Veiculo':
        print('Selecionado')
    else:
        print('Nao Selecionado')


app = QtWidgets.QApplication([])
tela = uic.loadUi("tela_inicial.ui")

tela.opcoes_combo_box.addItems(['Cadastrar Pessoa'])
tela.pushButton.clicked.connect(opcao_selecionada)

tela.show()
app.exec()
