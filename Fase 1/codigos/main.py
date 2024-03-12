import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox 
from ui_home import Ui_Form 
from ui_editar import Ui_Editar 
from PyQt5.QtCore import pyqtSignal 
from PyQt5 import QtCore


# janela de edição do produto
class EditWidget(QtWidgets.QWidget, Ui_Editar):
    produtoEditado = pyqtSignal(int, str, str, float, float, float, float, float)
    produtoExcluido = pyqtSignal()
    
    def __init__(self, parent=None, cod=None, nome=None, descricao=None, custoProduto=None, custoFixo=None, comissao=None, impostos=None, margemLucro=None):
        super(EditWidget, self,).__init__(parent)
        # interface
        self.setupUi(self)
        self.setWindowTitle("Edição de Produto") 

        #botões
        self.bt_editar.clicked.connect(self.edita)
        self.bt_excluir.clicked.connect(self.excluir)

        if cod is not None:
            self.input_codEdit.setValue(round(int(cod)))
            self.input_nomeEdit.setText(str(nome))
            self.input_descricaoEdit.setText(str(descricao))
        if custoProduto  or custoFixo or comissao or impostos or margemLucro is not None:
            self.input_CustoProdutoEdit.setValue(round(float(custoProduto)))
            self.input_custoFixoEdit.setValue(round(float(custoFixo)))
            self.input_comissaoEdit.setValue(round(float(comissao)))
            self.input_impostoEdit.setValue(round(float(impostos)))
            self.input_MargemLucroEdit.setValue(round(float(margemLucro)))


    

    def edita(self):
        novo_cod = self.input_codEdit.value()
        novo_nome = self.input_nomeEdit.text()
        nova_descricao = self.input_descricaoEdit.text()
        novo_custoProduto = self.input_CustoProdutoEdit.value()
        novo_custoFixo = self.input_custoFixoEdit.value()
        nova_comissao = self.input_comissaoEdit.value()
        novo_impostos = self.input_impostoEdit.value()
        nova_margemLucro = self.input_MargemLucroEdit.value()

        # Emitir um sinal contendo os novos dados do produto
        self.produtoEditado.emit(novo_cod, novo_nome, nova_descricao, novo_custoProduto, novo_custoFixo, nova_comissao, novo_impostos, nova_margemLucro)
        self.close()
        
        QMessageBox.warning(self, 'Aviso', 'Produto editado com sucesso!')
        
        return novo_cod, novo_nome, nova_descricao, novo_custoProduto, novo_custoFixo, nova_comissao, novo_impostos, nova_margemLucro
        
    def excluir(self):
        self.produtoExcluido.emit()
        QMessageBox.warning(self, 'Aviso', 'Produto excluído com sucesso!')

        self.close()

# confugurações relacionas a Janela principal            
class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        #paginas do sistema
        self.bt_homepg.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgHome))
        self.bt_cadastropg.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgCadastro))
        self.bt_listapg.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgLista))
        #ativaçaõ de outros botões
        self.bt_cadastrar.clicked.connect(self.cadastrarProduto)
        self.bt_logout.clicked.connect(self.logout)
        self.bt_limparCadastro.clicked.connect(self.limparCadastro)
        self.bt_limparUltimoCadastro.clicked.connect(self.limparUltimoCadastro)         
        self.treeWidget.itemClicked.connect(self.abrirEditar)


    #cadastro de produtos
    def cadastrarProduto(self):
        nome = str(self.input_nome.text())
        descricao = str(self.input_descricao.text())
        cod = int(self.input_cod.value())
        custoProduto = float(self.input_CustoProduto.value())
        custoFixo = float(self.input_custoFixo.value())
        comissao = float(self.input_comissao.value())
        impostos = float(self.input_imposto.value())
        margemLucro = float(self.input_MargemLucro.value())
        despesaTotal = (custoProduto + custoFixo + comissao + impostos) 
        precoVenda = despesaTotal * ((margemLucro/100)+1)
        if(precoVenda > despesaTotal *1.2 ):
            rentabilidade = str('Lucro Alto')
        elif((precoVenda <= despesaTotal *1.2) and (precoVenda > despesaTotal * 1.1)):
            rentabilidade = str('Lucro Médio')
        elif((precoVenda <= despesaTotal *1.1) and (precoVenda > despesaTotal * 1)):
            rentabilidade = str('Lucro Baixo')
        elif(precoVenda == despesaTotal):
            rentabilidade = str('Equilíbrio')
        else:
            rentabilidade = str('Prejuízo')


        if nome == "" or cod == 0 or custoProduto == 0 or margemLucro == 0:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos obrigatórios.')
            return
        else:
            QMessageBox.warning(self, 'Aviso', 'Produto cadastrado com sucesso!')

        item = [cod, nome, descricao, custoProduto, custoFixo, comissao, impostos, rentabilidade, precoVenda]
        self.adicionar_produto(item)


    
    def adicionar_produto(self, produto):
        item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item.setText(0, str(produto[0]))  # Codigo
        item.setText(1, str(produto[1]))  # Nome
        item.setText(2, str(produto[2]))  # Descrição
        item.setText(3, str(produto[3]))  # Custo do Produto
        item.setText(4, str(produto[4]))  # Custo Fixo
        item.setText(5, str(produto[5]))  # comissão
        item.setText(6, str(produto[6]))  # impostos
        item.setText(7, str(produto[7]))  # rentabilidade
        item.setText(8, str(produto[8]))  # preço Venda

    def abrirEditar(self):
        # Recuperar os dados do produto selecionado na árvore
        selected_item = self.treeWidget.currentItem()
        cod = selected_item.text(0)
        nome = selected_item.text(1)
        descricao = selected_item.text(2)
        custoProduto = selected_item.text(3)
        custoFixo = selected_item.text(4)
        comissao = selected_item.text(5)
        impostos = selected_item.text(6)
        margemLucro = selected_item.text(7)

        
        if all([cod, nome, descricao, custoProduto, custoFixo, comissao, impostos, margemLucro]):
            try:
                margemLucro = float(margemLucro)
            except ValueError:
                margemLucro = 0.0
        else:
            QMessageBox.warning(self, 'Aviso', 'Selecione um produto completo para editar.')
            return
        

        self.w = EditWidget(cod=cod, nome=nome, descricao=descricao, custoProduto=custoProduto, custoFixo=custoFixo, comissao=comissao, impostos=impostos, margemLucro=margemLucro)
        self.w.produtoEditado.connect(self.processarEdicao)
        self.w.produtoExcluido.connect(self.excluirProduto)
        self.w.produtoExcluido.connect(self.excluirProduto)
        self.w.show()



    def processarEdicao(self, novo_cod, novo_nome, nova_descricao,novo_custoProduto, novo_custoFixo, nova_comissao, novo_impostos, nova_margemLucro):
        selected_item = self.treeWidget.currentItem()
        selected_item.setText(0, str(novo_cod))
        selected_item.setText(1, novo_nome)
        selected_item.setText(2, nova_descricao)
        selected_item.setText(3, str(novo_custoProduto))
        selected_item.setText(4, str(novo_custoFixo))
        selected_item.setText(5, str(nova_comissao))
        selected_item.setText(6, str(novo_impostos))
        selected_item.setText(7, str(nova_margemLucro))



    def excluirProduto(self):
        selected_item = self.treeWidget.currentItem()

        if selected_item:
            index = self.treeWidget.indexOfTopLevelItem(selected_item)
            self.treeWidget.takeTopLevelItem(index)  



    def limparCadastro(self):
       self.treeWidget.clear()
    


    def limparUltimoCadastro(self):
        totalItens = self.treeWidget.topLevelItemCount()
        if (totalItens > 0):
            self.treeWidget.takeTopLevelItem(totalItens -1)
                    

    def logout(self):
        self.close()
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    principal = MainWindow()
    edit_ = EditWidget()
    principal.show()
    sys.exit(app.exec_())

