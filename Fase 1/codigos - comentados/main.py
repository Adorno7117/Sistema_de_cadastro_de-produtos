#----------- IMPORTAÇÕES --------------
#importações servem para evitar a necessidade de reescrever o mesmo código várias vezes!!

#não eh tão importante decorar isso 
#obs:minha opinião

#importa acesso a variáveis e funções do interpretador Python - basicamente essecial
import sys


#importa o modulo pra criar interfaces graficas
from PyQt5 import QtWidgets


#importa o modulo pra caixas de alerta
from PyQt5.QtWidgets import QMessageBox


#importa o modulo pra emitir sinais personalizados
from PyQt5.QtCore import pyqtSignal



#importa o designer da tela de login
from ui_login import Ui_login  


#importa o designer da tela de principal
from ui_home import Ui_Form 


#importa o designer da tela de edição
from ui_editar import Ui_Editar 




#----------- FIM DAS IMPORTAÇÕES ----------------



#------------COMEÇO TELA DE LOGIN CODIGO-----------------

# Define a classe Login e suas subclasses. 
# Ui_login = o designer da tela
# Qwiget = interface
class Login(QtWidgets.QWidget, Ui_login):



    # Método de inicialização da Tela de login 
    #__init__ = ao a classe ser inicia vai acontecer isso, isso, etc. por exemplo.
    def __init__(self):
        super().__init__()

        # Configura a interface do usuário a partir do arquivo de UI
        # Resumindo apartir do arquivo do design
        self.setupUi(self)


        # Define o título da janela como Login Sistema
        #  O nomezinho q aparece em cima quando a janela de login abre.
        self.setWindowTitle("Login Sistema")  


        # Faz o botão de login executar o método open_system, q abre o sistema
        self.bnt_logar.clicked.connect(self.open_system)
        # Faz a mesma coisa mas ao apertar Enter
        self.lineEdit_2.returnPressed.connect(self.bnt_logar.click)
        self.lineEdit.returnPressed.connect(self.bnt_logar.click)



    # Método para abrir o sistema
    # Serve pra conceder acesso a tela principal!
    def open_system(self):

        # Verifica se o texto digitado na linha de senha e usuário é '123' e 'admin'
        if self.lineEdit_2.text() == '123' and  self.lineEdit.text() == 'admin':
            
            #se sim, exibe a tela principal e fecha a tela de login
            self.w = MainWindow()
            self.w.show()
            self.close()


        #se não,
        # Verifica se os campos de usuário ou senha estão vazios
        elif self.lineEdit_2.text() == '' or  self.lineEdit.text() == '':
            
            #se sim, exibe um alerta avisando para preencher os campos
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setText("Insira o Usuario ou a Senha.")
            msgBox.exec_()

        # Se tudo estiver preenchido mas n for a senha nem o usuario correto...    
        else:

            #exibe um alerta q o login esta invalido
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Aviso")
            msgBox.setText("Usuario ou Senha inválida.")
            msgBox.exec_()
#------------FIM TELA DE LOGIN CODIGO-----------------
            






#------------COMEÇO TELA DE EDIÇÃO CODIGO-----------------            

# Define a classe edição e suas subclasses. 
# Ui_Editar = o designer da tela
# Qwiget = interface
class EditWidget(QtWidgets.QWidget, Ui_Editar):

    # Define os sinais produtoEditado e produtoExcluido q são enviados pra outras partes do programa
    # levam informações sobre o produto
    produtoEditado = pyqtSignal(int, str, float, float, float, float, float)
    produtoExcluido = pyqtSignal()
    

    # Método de inicialização da Tela de Edição, puxa os parametros da tela principal, se nenhum for fornecido eh definido como None
    def __init__(self, parent=None, cod=None, nome=None, custoProduto=None, custoFixo=None, comissao=None, impostos=None, margemLucro=None):
        super(EditWidget, self).__init__(parent)
        
        # Configura a interface do usuário
        self.setupUi(self)

        # Define o título da janela como Edição de Produto
        #  O nomezinho q aparece em cima quando a janela de edição abre.
        self.setWindowTitle("Edição de Produto") 
        


        #botões
        # Ao clicar ativa o metodo edita
        self.bt_editar.clicked.connect(self.edita)
        # Ao clicar ativa o metodo excluir
        self.bt_excluir.clicked.connect(self.excluir)


        # Preenche os campos com os valores recebidos
        # serve pra quando a janela de edição abrir os ja puxar os valores q estavam cadastrados no produto
        if cod is not None:
            self.input_codEdit.setValue(round(int(cod)))
            self.input_nomeEdit.setText(str(nome))
        if custoProduto  or custoFixo or comissao or impostos or margemLucro is not None:
            self.input_CustoProdutoEdit.setValue(round(float(custoProduto)))
            self.input_custoFixoEdit.setValue(round(float(custoFixo)))
            self.input_comissaoEdit.setValue(round(float(comissao)))
            self.input_impostoEdit.setValue(round(float(impostos)))
            self.input_MargemLucroEdit.setValue(round(float(margemLucro)))



    # Este eh o metodo q edita um porduto!
    def edita(self):

        # Obtém os novos valores dos campos de cod, nome, custo do produto, etc(atraves dos inputs no layout)
        novo_cod = self.input_codEdit.value()
        novo_nome = self.input_nomeEdit.text()
        novo_custoProduto = self.input_CustoProdutoEdit.value()
        novo_custoFixo = self.input_custoFixoEdit.value()
        nova_comissao = self.input_comissaoEdit.value()
        novo_impostos = self.input_impostoEdit.value()
        nova_margemLucro = self.input_MargemLucroEdit.value()

        # Emitir um sinal contendo os novos dados do produto
        '''Outros objetos podem se conectar a este sinal para receber 
        e processar esses dados atualizados do produto sempre que forem editados'''
        # resumindo faz a informação passar de um classe para outra sem ter um BD(banco de dados)
        self.produtoEditado.emit(novo_cod, novo_nome, novo_custoProduto, novo_custoFixo, nova_comissao, novo_impostos, nova_margemLucro)
        
        # Envia um aviso que o porduto foi cadastrado com sucesso
        QMessageBox.warning(self, 'Aviso', 'Produto editado com sucesso!')
        
        # reabilita a tela principal
        self.main_window.setEnabled(True)

        # Fecha a janela da edição
        self.close()

        # Retorna os novos valores
        return novo_cod, novo_nome, novo_custoProduto, novo_custoFixo, nova_comissao, novo_impostos, nova_margemLucro



    # este modulo envia um sinal para excluir um determinado produto na tela principal   
    def excluir(self):
        # Emite o sinal produtoExcluido
        self.produtoExcluido.emit()

        # Cria um Aviso q o produto foi excluido
        QMessageBox.warning(self, 'Aviso', 'Produto excluído com sucesso!')

        # reabilita a tela principal
        self.main_window.setEnabled(True)

        # Fecha a janela de edição
        self.close()
#------------FIM TELA DE EDIÇÃO CODIGO-----------------   
        









#------------COMEÇO TELA PRINCIPAL CODIGO-----------------   
# confugurações relacionas a Janela principal            
class MainWindow(QtWidgets.QWidget, Ui_Form):
    

    # Método de inicialização da Tela Principal
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self) # Configura a interface definida em Ui_Form
        self.setWindowTitle("Sistema de Gerenciamento") # Define o título da janela principal




        # ----paginas do sistema----
        # Define as ações dos botões para alternar entre as páginas do sistema

        # pagina Home 
        self.bt_homepg.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgHome)) 

        # Pagina de Cadastro de produtos
        self.bt_cadastropg.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgCadastro))

        # Pagina de Lista de produtos
        self.bt_listapg.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pgLista))




        #---ativação de outros botões---
        # Define as ações dos botões para cada funcionalidade

        # Botão q aciona o modulo de cadastrar um produto
        self.bt_cadastrar.clicked.connect(self.cadastrarProduto)

        # Botão q aciona o modulo de deslogar do sistema
        self.bt_logout.clicked.connect(self.logout)

        # Botão q aciona o modulo de limpar todos os ultimos produtos cadastrados
        self.bt_limparCadastro.clicked.connect(self.limparCadastro)

        # Botão q aciona o modulo de limpar apenas o ultimo produto cadastrado
        self.bt_limparUltimoCadastro.clicked.connect(self.limparUltimoCadastro)  
        #-----------------


        # Aciona o modulo de abrir a janela de edição ao clicar em um produto
        self.treeWidget.itemClicked.connect(self.abrirEditar)


    # Método para cadastrar um novo produto
    def cadastrarProduto(self):

        # Coleta os dados do produto a ser cadastrado dos campos de entrada na interface
        nome = str(self.input_nome.text())
        cod = int(self.input_cod.value())
        custoProduto = float(self.input_CustoProduto.value())
        custoFixo = float(self.input_custoFixo.value())
        comissao = float(self.input_comissao.value())
        impostos = float(self.input_imposto.value())
        margemLucro = float(self.input_MargemLucro.value())


        # Calcula a rentabilidade e preço de venda do produto com base nos dados inseridos
        # Soma todos os gastos
        despesaTotal = (custoProduto + custoFixo + comissao + impostos) 
        #faz o preçoo de Venda ser tantos por cento maior q as Despesas
        precoVenda = despesaTotal * ((margemLucro/100)+1)

        # Calculo de Rentabilidade
        if(precoVenda > despesaTotal *1.2 ):
            rentabilidade = str('Lucro Alto') # se maior q 20%

        elif((precoVenda <= despesaTotal *1.2) and (precoVenda > despesaTotal * 1.1)):
            rentabilidade = str('Lucro Médio')# se menor/igual a 20% e maior q 10%

        elif((precoVenda <= despesaTotal *1.1) and (precoVenda > despesaTotal * 1)):
            rentabilidade = str('Lucro Baixo')# se menor/igual a 10% e maior q 0%


        elif(precoVenda == despesaTotal): # se preço de venda for igual as depesas
            rentabilidade = str('Equilíbrio')


        else:
            rentabilidade = str('Prejuízo')# se menor 0%



        # Se nenhum dos campos obrigatorios for preenchidos
        if nome == "" or cod == 0 or custoProduto == 0 or margemLucro == 0:

            # Exibe um erro q todos os dados obrigatorios devem ser cadastrados
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos obrigatórios.')

            # não retorna nada, para q nada seja cadastrado
            return
        

        else:
            #se Tudo estiver ok, envia um aviso q o produto foi cadastrado
            QMessageBox.warning(self, 'Aviso', 'Produto cadastrado com sucesso!')

        # cria um array e armazena todos os dados necessario dentro dele
        '''Um array é uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo, 
        acessíveis por meio de um índice. Eles são úteis para organizar e manipular conjuntos de 
        dados de forma eficiente em programação.'''
        item = [cod, nome, custoProduto, custoFixo, comissao, impostos, rentabilidade, precoVenda]

        # Acina o Modulo logo em seguida, q esse sim, add os dados na tabela
        self.adicionar_produto(item)


    # Modulo para add dados na tabela
    def adicionar_produto(self, produto):


        # Faz com q os itens sejam armazenados an tabela
        item = QtWidgets.QTreeWidgetItem(self.treeWidget)

        # Seta os itens da array em ordem um por um, e os transforma em texto/caracter
        item.setText(0, str(produto[0]))  # Codigo
        item.setText(1, str(produto[1]))  # Nome
        item.setText(2, str(produto[2]))  # Custo do Produto
        item.setText(3, str(produto[3]))  # Custo Fixo
        item.setText(4, str(produto[4]))  # comissão
        item.setText(5, str(produto[5]))  # impostos
        item.setText(6, str(produto[6]))  # rentabilidade
        item.setText(7, str(produto[7]))  # preço Venda



    # Método para abrir a janela de edição ao clicar em um produto
    def abrirEditar(self):

        # seleciona o item q foi clicado
        selected_item = self.treeWidget.currentItem()

        #recupera os textos de todos os itens
        cod = selected_item.text(0)
        nome = selected_item.text(1)
        custoProduto = selected_item.text(2)
        custoFixo = selected_item.text(3)
        comissao = selected_item.text(4)
        impostos = selected_item.text(5)
        margemLucro = selected_item.text(6)

        
        # Verifica se todos os campos do produto selecionado estão preenchidos
        if all([cod, nome, custoProduto, custoFixo, comissao, impostos, margemLucro]):
            try:

                # Tenta trazer o valor da Magem de lucro
                #OBS: a margem de lucro tava dando mtt erro por isto esta parte, quase sempre n vai consegir puxar
                margemLucro = float(margemLucro)

            except ValueError:
                # se não conseguir define como 0.0
                margemLucro = 0.0

        # serve pra Abrir a janela de edição com os dados do produto selecionado
        self.w = EditWidget(cod=cod, nome=nome, custoProduto=custoProduto, custoFixo=custoFixo, comissao=comissao, impostos=impostos, margemLucro=margemLucro)
        
        # conecta os Modulos da Class edição
        self.w.produtoEditado.connect(self.processarEdicao)
        self.w.produtoExcluido.connect(self.excluirProduto)
        
        # desabilita a tela principal enquanto a tela de edição estiver ativa
        self.setEnabled(False)
        # Abre a janela
        self.w.show()




    # Método para processar a edição de um produto
    # Agora sim salva os dados editados
    def processarEdicao(self, novo_cod, novo_nome, novo_custoProduto, novo_custoFixo, nova_comissao, novo_impostos, nova_margemLucro):
        
        # seleciona o item q foi clicado
        selected_item = self.treeWidget.currentItem()

        #seta novos valores para ele
        selected_item.setText(0, str(novo_cod))
        selected_item.setText(1, novo_nome)
        selected_item.setText(2, str(novo_custoProduto))
        selected_item.setText(3, str(novo_custoFixo))
        selected_item.setText(4, str(nova_comissao))
        selected_item.setText(5, str(novo_impostos))
        selected_item.setText(6, str(nova_margemLucro))


    # exclui o produto selecionado
    def excluirProduto(self):
        # seleciona o item q foi clicado
        selected_item = self.treeWidget.currentItem()

        if selected_item:
            # Obtém o índice do item selecionado
            index = self.treeWidget.indexOfTopLevelItem(selected_item)
            # Remove o item da tabela com o índice obtido
            self.treeWidget.takeTopLevelItem(index)  


    # modulo q limpa todos os produtos cadastrados
    def limparCadastro(self):
       self.treeWidget.clear()
    

    #modulo q limpa o ultimo produto cadastrado
    def limparUltimoCadastro(self):
        # soma quantos iten tem na tabela
        totalItens = self.treeWidget.topLevelItemCount()
        if (totalItens > 0):
            # se o numero de itens for maior q 0, exclui o ultimo item
            self.treeWidget.takeTopLevelItem(totalItens -1)
     
                   
    # modulo q fecha a janela principal e volta para de login (Desloga)
    def logout(self):
        self.w = Login()
        self.w.show()
        self.close()
    


# Verifica se este script está sendo executado como o programa principal.
if __name__ == "__main__":
    # Cria uma instância da aplicação Qt, necessária para executar programas PyQt. 
    #isso eh por conta de onde foi feito o deigner, neste caso no QT Designer
    app = QtWidgets.QApplication(sys.argv)

    # Cria uma instância das janelas
    principal = MainWindow()
    edit_ = EditWidget()
    login = Login() 


    # Exibe a janela de login.
    login.show()
    
    # Inicia o loop de eventos da aplicação e encerra o programa quando o loop é encerrado.
    sys.exit(app.exec_())

