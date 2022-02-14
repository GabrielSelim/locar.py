from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel


class Veiculo(QDialog):
    def __init__(self, *args, **argvs):
        super(Veiculo, self).__init__(*args, **argvs)
        self.tela_cadastro_veiculo = uic.loadUi("tela_cadastrar_veiculo_nova.ui")
        self.tela_cadastro_veiculo.pushButton_2.connect(self.add_veiculo)

    def add_veiculo(self):
        modelo = self.tela_cadastro_veiculo.lineEdit.text()
        cor = self.tela_cadastro_veiculo.lineEdit_2.text()
        placa = self.tela_cadastro_veiculo.lineEdit_3.text()
        chassi = self.tela_cadastro_veiculo.lineEdit_4.text()
        ano = self.tela_cadastro_veiculo.lineEdit_5.text()
        status = self.tela_cadastro_veiculo.lineEdit_6.text()
        ar_condicionado = self.tela_cadastro_veiculo.lineEdit_7.text()
        marca = self.tela_cadastro_veiculo.lineEdit_8.text()
        nome = self.tela_cadastro_veiculo.lineEdit_9.text()
        valor_pago = self.tela_cadastro_veiculo.lineEdit_91.text()
        km_rodados = self.tela_cadastro_veiculo.lineEdit_92.text()
        tipo_combustivel = self.tela_cadastro_veiculo.lineEdit_93.text()
        categoria = self.tela_cadastro_veiculo.lineEdit_95.text()
        if modelo == "" or cor == "" or placa == "" or chassi == "" or ano == "" or status == "" or ar_condicionado == "" or marca == "" or nome == "" or valor_pago == "" or km_rodados == "" or tipo_combustivel == ""  or categoria == "":
            QMessageBox.Information(QMessageBox(), " Opa Opa", "Preencha todos os Campos")
        else:
            print("Adicionado ao BD")
            QMessageBox.Information(QMessageBox(), " Opa Opa", "Dados Gravados com Sucesso")



Veiculo()
