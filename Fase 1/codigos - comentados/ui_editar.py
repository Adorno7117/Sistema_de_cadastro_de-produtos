# -*- coding: utf-8 -*-
'''
DESIGNER TELA DE EDIÇÃO DE PRODUTO

ATENÇÃO!!



esta parte n é importante para se saber, eh apenas o desgner sendo transformado para linguegem python

n tem nada haver com o conteúdo q a gente aprendeu durante o curso ou necessario de saber algo daki


só precisa saber q eh o desgner sendo transformado para linguagem python




















'''


# Form implementation generated from reading ui file 'ui_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Editar(object):
    def setupUi(self, Editar):
        Editar.setObjectName("Editar")
        Editar.resize(664, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(Editar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Editar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.input_nomeEdit = QtWidgets.QLineEdit(Editar)
        self.input_nomeEdit.setObjectName("input_nomeEdit")
        self.horizontalLayout_4.addWidget(self.input_nomeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(Editar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.input_codEdit = QtWidgets.QSpinBox(Editar)
        self.input_codEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_codEdit.setMaximum(999999999)
        self.input_codEdit.setObjectName("input_codEdit")
        self.horizontalLayout_5.addWidget(self.input_codEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(Editar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.input_CustoProdutoEdit = QtWidgets.QDoubleSpinBox(Editar)
        self.input_CustoProdutoEdit.setMaximum(999999999999999.0)
        self.input_CustoProdutoEdit.setObjectName("input_CustoProdutoEdit")
        self.horizontalLayout_6.addWidget(self.input_CustoProdutoEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(Editar)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.input_custoFixoEdit = QtWidgets.QDoubleSpinBox(Editar)
        self.input_custoFixoEdit.setMaximum(99999999999.0)
        self.input_custoFixoEdit.setObjectName("input_custoFixoEdit")
        self.horizontalLayout_9.addWidget(self.input_custoFixoEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(Editar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.input_comissaoEdit = QtWidgets.QDoubleSpinBox(Editar)
        self.input_comissaoEdit.setMaximum(999999999999.0)
        self.input_comissaoEdit.setObjectName("input_comissaoEdit")
        self.horizontalLayout_8.addWidget(self.input_comissaoEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(Editar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.input_impostoEdit = QtWidgets.QDoubleSpinBox(Editar)
        self.input_impostoEdit.setMaximum(9999999999999.0)
        self.input_impostoEdit.setObjectName("input_impostoEdit")
        self.horizontalLayout_7.addWidget(self.input_impostoEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spin = QtWidgets.QLabel(Editar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spin.setFont(font)
        self.spin.setObjectName("spin")
        self.horizontalLayout_3.addWidget(self.spin)
        self.input_MargemLucroEdit = QtWidgets.QSpinBox(Editar)
        self.input_MargemLucroEdit.setMaximum(999999)
        self.input_MargemLucroEdit.setObjectName("input_MargemLucroEdit")
        self.horizontalLayout_3.addWidget(self.input_MargemLucroEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_excluir = QtWidgets.QPushButton(Editar)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_excluir.setFont(font)
        self.bt_excluir.setStyleSheet("QPushButton{\n"
"background-color:rgb(35, 41, 121);\n"
"color:rgb(255, 255, 255);\n"
"cursor: pointer;\n"
"}\n"
"QPushButton:hover {\n"
"    transform: scale(1.1);\n"
"}\n"
"QPushButton:active {\n"
"    transform: scale(0.9); \n"
"}")
        self.bt_excluir.setObjectName("bt_excluir")
        self.horizontalLayout.addWidget(self.bt_excluir)
        self.bt_editar = QtWidgets.QPushButton(Editar)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_editar.setFont(font)
        self.bt_editar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_editar.setStyleSheet("QPushButton{\n"
"background-color:rgb(35, 41, 121);\n"
"color:rgb(255, 255, 255);\n"
"cursor: pointer;\n"
"}\n"
"QPushButton:hover {\n"
"    transform: scale(1.1);\n"
"}\n"
"QPushButton:active {\n"
"    transform: scale(0.9); \n"
"}\n"
"")
        self.bt_editar.setObjectName("bt_editar")
        self.horizontalLayout.addWidget(self.bt_editar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Editar)
        QtCore.QMetaObject.connectSlotsByName(Editar)

    def retranslateUi(self, Editar):
        _translate = QtCore.QCoreApplication.translate
        Editar.setWindowTitle(_translate("Editar", "Form"))
        self.label_5.setText(_translate("Editar", "Nome *"))
        self.label_6.setText(_translate("Editar", "Código *"))
        self.label_7.setText(_translate("Editar", "Custo Produto *"))
        self.label_9.setText(_translate("Editar", "Custo Fixo"))
        self.label_4.setText(_translate("Editar", "Comissão"))
        self.label_3.setText(_translate("Editar", "Imposto"))
        self.spin.setText(_translate("Editar", "Margem Lucro *"))
        self.bt_excluir.setText(_translate("Editar", "Excluir"))
        self.bt_editar.setText(_translate("Editar", "Editar"))
