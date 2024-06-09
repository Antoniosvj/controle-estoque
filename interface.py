import tkinter as tk
from tkinter import ttk

class JanelaPrincipal:
    def __init__(self, win):

        #Componentes
        self.lblCodigo = tk.Label(win, text='Código do Produto:')
        self.lblNome = tk.Label(win, text='Nome:')
        self.lblQuantidade = tk.Label(win, text='Quantidade:')
        self.lblPrecoCompra = tk.Label(win, text='Preço de Compra:')
        self.lblPrecoVenda = tk.Label(win, text='Preço de Venda:')
        
        self.txtCodigo = tk.Entry(win, width=15)
        self.txtNome = tk.Entry(win, width=50)
        self.txtQuantidade = tk.Entry(win, width=15)
        self.txtPrecoCompra = tk.Entry(win, width=15)
        self.txtPrecoVenda = tk.Entry(win, width=15)
        
        self.btnSalvar = tk.Button(win, text='Salvar', padx=10)
        self.btnAtualizar = tk.Button(win, text='Atualizar', padx=10)
        self.btnExcluir = tk.Button(win, text='Excluir', bg='#ff1111', fg='#fff', padx=10)
        self.btnLimparTela = tk.Button(win, text='Limpar', padx=10)
        
        #Posição dos componentes na janela
        self.lblCodigo.place(x=50, y=30)
        self.txtCodigo.place(x=170, y=30)
        self.lblNome.place(x=50, y=80)
        self.txtNome.place(x=100, y=80)
        self.lblPrecoCompra.place(x=50, y=130)
        self.txtPrecoCompra.place(x=170, y=130)
        self.lblQuantidade.place(x=300, y=130)
        self.txtQuantidade.place(x=400, y=130)
        self.lblPrecoVenda.place(x=530, y=130)
        self.txtPrecoVenda.place(x=650, y=130)
        
        self.btnSalvar.place(x=330, y=30)
        self.btnAtualizar.place(x=445, y=30)
        self.btnExcluir.place(x=555, y=30)
        self.btnLimparTela.place(x=670, y=30)


win = tk.Tk()
win.title('Controle de Estoque')
win.geometry('820x600')

app = JanelaPrincipal(win)

win.mainloop()