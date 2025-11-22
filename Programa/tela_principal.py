from main import *  
from tkinter import *
import webbrowser

class Interface:
    def __init__(self, onibus, metro, trem, barco):
        self.onibus = onibus 
        self.metro = metro
        self.trem = trem
        self.barco = barco

    def iniciar(self):
        tela = Tk()
        tela.title("Sistema de Transporte Público")
        tela.configure(background="#D6D6D6", padx=20, pady=20, )
        tela.geometry("670x400")

        nome_programa = Label(tela, text="Sistema de Transporte Publico", bg="#D6D6D6")
        nome_programa.pack(anchor="center", side="top")

        creditos = Button(tela, text="DEV by: Carlos Henrique - Felipe de Almeida", bg="#CCCCCC", command=self.abrir_repositório, border=0)
        creditos.pack(anchor="se", side="bottom")

        # Frame à esquerda
        frame_esq = Frame(tela, width=290, height=260, bg="#D6D6D6")
        frame_esq.pack(side="left")

        # #
        # Fundo da seção principal do frame da esquerda
        back_sec_principal = Frame(frame_esq, width=290, height=130, bg="#ffffff")
        back_sec_principal.place(x=0, y=0)

        # ##
        # Nome da seção principal
        nome_sec = Label(back_sec_principal, text="Selecione o tipo de transporte", bg="#ffffff")
        nome_sec.place(x=10, y=0)

        # ##
        # Bloco da sessão prinipal
        bloco_sessao_primaria = Frame(back_sec_principal, width=290, height=254, padx=5, pady=5, border=0.5, bg="#ffffff")
        bloco_sessao_primaria.place(x=0, y=20)

        # ###
        # Formatação interna do bloco
        bloco_int = Frame(bloco_sessao_primaria, width=270, height=90, bg="#D6D6D6")
        bloco_int.place(x=5, y=5)

        # ####
        # Radio butons e labels relativas
        var_transporte = StringVar()
        radio_onibus = Radiobutton(bloco_int, text="Ônibus", bg="#D6D6D6", variable=var_transporte, value="onibus", activebackground="#D6D6D6")
        radio_onibus.place(x=5, y=5)
        tarifa_onibus = Label(bloco_int, text=f"Tarifa:    (Fixa) R${self.onibus.tarifa}", bg="#D6D6D6")
        tarifa_onibus.place(x=95, y=7)

        radio_metro = Radiobutton(bloco_int, text="Metrô", bg="#D6D6D6", variable=var_transporte, value="metro", activebackground="#D6D6D6")
        radio_metro.place(x=5, y=25)
        tarifa_metro = Label(bloco_int, text="Tarifa:    (base) + por distancia", bg="#D6D6D6")
        tarifa_metro.place(x=95, y=27)

        radio_trem = Radiobutton(bloco_int, text="Trem", bg="#D6D6D6", variable=var_transporte, value="trem", activebackground="#D6D6D6")
        radio_trem.place(x=5, y=45)
        tarifa_trem = Label(bloco_int, text="Tarifa:    Por zonas", bg="#D6D6D6")
        tarifa_trem.place(x=95, y=47)

        radio_barco = Radiobutton(bloco_int, text="Barco", bg="#D6D6D6", variable=var_transporte, value="barco", activebackground="#D6D6D6")
        radio_barco.place(x=5, y=65)
        tarifa_barco = Label(bloco_int, text="Tarifa:    Por trechos", bg="#D6D6D6")
        tarifa_barco.place(x=95, y=67)

        # #
        # Fundo da seção de notas
        bloco_sessao_notas = Frame(frame_esq, width=290, height=80, padx=15, pady=2, bg="#B8EBB8")
        bloco_sessao_notas.place(x=0, y=140)

        # ##
        # Titulo das notas
        titulo_notas = Label(bloco_sessao_notas, text="NOTA Os cálculos consideram:", bg="#B8EBB8")
        titulo_notas.place(x=0, y=0)

        # ##
        # Considerações
        c1 = Label(bloco_sessao_notas, text="° Horário de pico", bg="#B8EBB8")
        c1.place(x=0, y=20)

        # ##
        c1 = Label(bloco_sessao_notas, text="° Velocidade média do veículo", bg="#B8EBB8")
        c1.place(x=0, y=35)

        # ##
        c1 = Label(bloco_sessao_notas, text="° Tarifas especificas de cada transporte", bg="#B8EBB8")
        c1.place(x=0, y=50)

        # #
        # Botão para calcular a viagem
        calc_btn = Button(frame_esq, text="Calcular Viagem", width=15, height=1, bg="#A3A3A3", command=self.calcular)
        calc_btn.place(x=80, y=228)

        # Frame à direita
        frame_dir = Frame(tela, width=290, height=260, bg="#ffffff")
        frame_dir.pack(anchor="e", side="right")

        # #
        # Nome da sessão
        nome_sec = Label(frame_dir, text="Dados da Viagem", bg="#ffffff")
        nome_sec.place(x=10, y=0)

        # #
        # Fundo da sessão
        back_sec = Frame(frame_dir, width=290, height=150, border=1, bg="#ffffff")
        back_sec.place(x=0, y=20)

        # ##
        # Fromatação do fundo da sessão
        bloco_back = Frame(back_sec, width=265, height=137, bg="#D6D6D6")
        bloco_back.place(x=12, y=12)

        # ###
        # Labels de dados
        veiculo = "veiculo"
        tarifa = 0.0
        tempo_esp = "T minutos"
        tempo_via = "T horas"
        cheg_estim = "hh:mm"

        label_veiculo = Label(bloco_back, text="Veículo:", bg="#D6D6D6")
        label_veiculo.place(x=10, y=5)
        lbl_dado_veiculo = Label(bloco_back, text=f" {veiculo}", bg="#D6D6D6")
        lbl_dado_veiculo.place(x=150, y=5)

        label_tarifa = Label(bloco_back, text="Tarifa:", bg="#D6D6D6")
        label_tarifa.place(x=10, y=30)
        lbl_dado_tarifa = Label(bloco_back, text=f" {tarifa}", bg="#D6D6D6")
        lbl_dado_tarifa.place(x=150, y=30)

        label_tempEspera = Label(bloco_back, text="Tempo de espera:", bg="#D6D6D6")
        label_tempEspera.place(x=10, y=55)
        lbl_dado_tempEspera = Label(bloco_back, text=f" {tempo_esp}", bg="#D6D6D6")
        lbl_dado_tempEspera.place(x=150, y=55)

        label_tempViagem = Label(bloco_back, text="Tempo de viagem:", bg="#D6D6D6")
        label_tempViagem.place(x=10, y=80)
        lbl_dado_tempViagem = Label(bloco_back, text=f" {tempo_via}", bg="#D6D6D6")
        lbl_dado_tempViagem.place(x=150, y=80)

        label_chegEstimada = Label(bloco_back, text="Chegada estimada:", bg="#D6D6D6")
        label_chegEstimada.place(x=10, y=105)
        lbl_dado_chegEstimada = Label(bloco_back, text=f" {cheg_estim}", bg="#D6D6D6")
        lbl_dado_chegEstimada.place(x=150, y=105)

        # #
        # Fundo da subsessão
        back_sub = Frame(frame_dir, width=290, height=110, border=1,  bg="#ffffff")
        back_sub.place(x=0, y=165)

        # ##
        # Título da dubsessão
        nome_sub = Label(back_sub, text="Comparação rápida", bg="#ffffff")
        nome_sub.place(x=10, y=0)

        # ###
        # Formatação interna da subsessão
        bloco_sub = Frame(back_sub, width=265, height=60, background="#D6D6D6")
        bloco_sub.place(x=12, y=20)

        # ####
        # Botão de comparação
        compar_btn = Button(bloco_sub, width=20, height=1, text="Comparar Todas as Tarifas", command=self.comparar)
        compar_btn.place(x=60, y=18)

        tela.mainloop()

    def abrir_repositório():
        webbrowser.open_new("https://github.com/FG333k/Sistema_trasporte")

    def calcular():
        pass

    def comparar():
        pass

    def dados_viagem(self, var_transporte):
        if(var_transporte == "onibus"):
            pass



O1 = Onibus(45, 79, 2.5)
M1 = Metro("not", 4, 5)
T1 = Trem("not", 4, 5)
B1 = Barco("not", 4, 5)

run = Interface(O1, M1, T1, B1)
run.iniciar()