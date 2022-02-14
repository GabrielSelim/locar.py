'''def veiculo_escolha():
    # Estas Listas serão substituidas pelo banco de dados que será implementado
    lista_sedan = {'Etius 1.5': 150, 'Corolla 1.8': 180, 'Sentra 2.0': 220, 'Fiesta 1.0': 140}
    lista_hatch = {'Etius 1.0': 120, 'Uno': 125, 'Focus 2.0': 220, 'Ford Ka': 140}
    lista_suv = {'Renegade 1.8': 230, 'Creta': 235, 'Corolla Cross': 270}
    lista_utilitarios = {'Strada 1.6': 190, 'Saveiro Robust': 180, 'Montana': 185}
    lista_caminhonete = {'S10 2.0': 250, 'Ranger 2.5': 285, 'Hilux': 330}
    lista_sportivo = {'Camaro': 550, 'Audi TT': 590, 'Mercedez 320i': 540}
    lista_moto = ['Indisponivel']
    lista_caminhao = ['Indisponivel']
    veiculo_escolhido = tela_cadastro_reserva.comboBox_3.currentText()

    if veiculo_escolhido == 'Sedan':
        tela_sedan = tela_cadastro_reserva.comboBox_3.addItems(list(lista_sedan.keys()))
        tela_cadastro_reserva.comboBox_3.show(tela_sedan)

    if veiculo_escolhido == 'Hatch':
        tela_cadastro_reserva.comboBox_3.addItems(list(lista_hatch.keys()))

    if veiculo_escolhido == 'SUV':
        tela_cadastro_reserva.comboBox_3.addItems(list(lista_suv))

    if veiculo_escolhido == 'Utilitário':
        tela_cadastro_reserva.comboBox_3.addItems(list(lista_utilitarios))

    if veiculo_escolhido == 'Caminhonete':
        tela_cadastro_reserva.comboBox_3.addItems(list(lista_caminhonete))

    if veiculo_escolhido == 'Moto':
        tela_cadastro_reserva.comboBox_3.addItems(list(lista_moto))

    if veiculo_escolhido == 'Caminhão':
        tela_cadastro_reserva.comboBox_3.addItems(list(lista_caminhao))

    if veiculo_escolhido == 'Sportivo':
        tela_cadastro_reserva.comboBox_3.addItems(list(lista_sportivo))'''



#tela_cadastro_reserva.comboBox_3.addItems({'Etius 1.5': 150, 'Corolla 1.8': 180, 'Sentra 2.0': 220, 'Fiesta 1.0': 140}.keys())



from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel

carros = ('Sedan', 'Hatch', 'SUV', 'Utilitário', 'Caminhonete', 'Cruze', 'Brasilia', 'Saveiro', 'Fusca', 'Hilux', 'Onix')
modelo = QStandardItemModel(len(carros), 1)
modelo.setHorizontalHeaderLabels(['Carros'])

for linha, carro in enumerate(carros):    # [(1, 'Gol'), (2,'Celta') ]
    elemento = QStandardItem(carro)
    modelo.setItem(linha, 0, elemento)

filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(0)
filtro.setFilterCaseSensitivity(Qt.CaseInsensitive)

app=QtWidgets.QApplication([])
tela=uic.loadUi("tela_consulta_veiculo.ui")
tela.tableView.setModel(filtro)
tela.tableView.horizontalHeader().setStyleSheet("font-size: 35px;color: rgb(50, 50, 255);")
tela.lineEdit.textChanged.connect(filtro.setFilterRegExp)



