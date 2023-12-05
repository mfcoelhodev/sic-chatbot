import tkinter as tk
from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
import time
import os
import cProfile 
import webbrowser

janela = ct.CTk()
janela.title("Assistente Virtual")
ct.set_appearance_mode("light") #dark
ct.set_default_color_theme=('#f6f2f3')
bgColor = "#f6f2f3"   #black
janela.configure(fg_color=bgColor)
janela.geometry("1000x650+500+100")

caminho_arquivo = "imagename.txt"

if os.path.exists(caminho_arquivo):
    pass
else:
    with open(caminho_arquivo, "x") as f:
        pass

with open(caminho_arquivo, "w") as img_src:
    lista_imagem ='imagens\\avator.png'
    minha_imagem = lista_imagem
    print(minha_imagem)
    img_src.write(f"{minha_imagem}")

def abrir_link():
        link = 'https://www.samsung.com/br/'
        webbrowser.open(link)


class ChatApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.resizable(True, True)
        self.janela.geometry("520x620+500+100")

        self.optionFram = Frame(janela, bg="#f6f2f3") 
        

        man_icone_sam = Image.open("Imagens/samsung_avatar-removebg-preview.png")
        man_imagem_sam = ImageTk.PhotoImage(man_icone_sam.resize((40, 40)))

        man_icone_enviar = Image.open("Imagens/enviar.png")
        man_imagem_enviar = ImageTk.PhotoImage(man_icone_enviar.resize((40, 40)))

        man_icone_mensagem = Image.open("imagens\\message.png")
        man_imagem_mensagem = ImageTk.PhotoImage(man_icone_mensagem.resize((40, 40)))

        man_icone_chat = Image.open("Imagens/samsung.png")
        man_imagem_chat = ImageTk.PhotoImage(man_icone_chat.resize((55, 55)))

       

        self.menIcone = ct.CTkButton(self.optionFram, text="",image=man_imagem_mensagem, width=0, bg_color=bgColor, fg_color=bgColor)
        self.menIcone.pack(side=RIGHT, anchor="nw", padx=5, pady=5)

        self.manIcone2 = ct.CTkButton(self.optionFram, text="",image=man_imagem_sam, height=1, width=1, bg_color=bgColor, fg_color=bgColor,
                                corner_radius=20)
        self.manIcone2.pack(side=LEFT, anchor="ne")

        self.nome_sam = ct.CTkLabel(self.optionFram, text="Fale com a SAM", font=("consolas", 20), text_color="#010100") 
        self.nome_sam.pack(side=LEFT, padx=5, pady=7, anchor="ne")
        self.optionFram.pack(side=TOP, fill=X, anchor="n")

        self.canvas = tk.Canvas(janela, bg="#f6f2f3", highlightthickness=0)  

        self.label_frame = tk.Frame(self.canvas, bg="#f6f2f3")   
        self.label_frame.pack(side="left", fill="both", expand=True)

        self.scrollable_window = self.canvas.create_window((0, 0), window=self.label_frame, anchor="nw")

        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.label_frame.bind("<Configure>", self.configure_scroll_region)

        self.barra_rolar = ct.CTkScrollbar(self.canvas, orientation="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.barra_rolar.set)
        self.canvas.yview_moveto(1.0)

        self.barra_rolar.pack(side="right", fill=Y)

        self.canvas.bind("<Configure>", self.resize_frame)
        self.canvas.pack(side=TOP, fill=BOTH)

        bgColorChatFram = "#a8c7fc"   
        self.chatFram = Frame(janela, bg=bgColorChatFram)
        ########   EU PAREI AQUI:  #######################


        self.chatIcone = ct.CTkButton(self.chatFram, text="",image=man_imagem_chat, width=20, bg_color=bgColorChatFram, fg_color=bgColorChatFram)
        self.chatIcone.pack(side=LEFT, padx=5)
        self.chatIcone.configure(command=abrir_link)
    
        
        self.msgInput = ct.CTkEntry(self.chatFram, placeholder_text="Digite aqui...", height=40, text_color="#010100", font=("consolas", 18))
        self.msgInput.pack(side=LEFT, pady=10, padx=0, fill=X, expand=True)

        self.enviarmsg = ct.CTkButton(self.chatFram, text="", image=man_imagem_enviar, bg_color=bgColorChatFram, fg_color=bgColorChatFram, height=40, width=20, hover_color=bgColorChatFram)
        self.enviarmsg.pack(side=LEFT, padx=0, pady=8)
        self.enviarmsg.configure(command=self.enviarMensagem)

        self.chatFram.pack(side=BOTTOM, fill=X, ipady=5)

        self.janela.bind("<Return>", lambda event: self.enviarMensagem())

    def enviarMensagem(self):
        with open(caminho_arquivo, "r") as f:
            self.imagename = f.read()
            print(self.imagename)

        self.message = self.msgInput.get()
        self.msgInput.delete(0, END)
        usuario_imagem_src = Image.open(self.imagename)
        usuario_imagem = ImageTk.PhotoImage(usuario_imagem_src.resize((40, 40)))        
        robo_imagem_src = Image.open("imagens\\robot.png")
        robo_imagem = ImageTk.PhotoImage(robo_imagem_src.resize((40, 40)))
        #PAREI AQUI !!!! (JONATAS)
        if self.message != "":
            self.current_time = time.strftime("%H:%M")
            self.current_time_label = ct.CTkLabel(self.label_frame, text=self.current_time, font=("consolas", 12))
            self.current_time_label.pack(side=TOP, anchor="ne", pady=0, padx=45)

            self.user_frame = ct.CTkFrame(self.label_frame, fg_color="#f6f2f3") 
            self.user_frame.pack(side=TOP, anchor="ne")
            self.user_label = ct.CTkLabel(self.user_frame, text=self.message, font=("Poppins", 15), fg_color="#419f5b", corner_radius=4,
                                    wraplength=250)
            self.user_label.pack(side=LEFT, anchor="nw", pady=1, ipadx=15, ipady=6, padx=10)
            self.user_image_label = ct.CTkLabel(self.user_frame, text="", image=usuario_imagem, fg_color="#f6f2f3") 
            self.user_image_label.pack(side=TOP, pady=13)
            self.janela.update_idletasks()
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)
            try:
               
                if self.to_respond:
                    self.current_time = time.strftime("%H:%M")
                    self.current_time_label = ct.CTkLabel(self.label_frame, text=self.current_time, font=("consolas", 12))
                    self.current_time_label.pack(side=TOP, anchor="nw", pady=0, padx=55)
                    self.bot_frame = ct.CTkFrame(self.label_frame, fg_color="#f6f2f3") 
                    self.bot_frame.pack(side=TOP, anchor="nw", padx=10)
                    self.bot_response_label = ct.CTkLabel(self.bot_frame, text=self.to_respond, font=("Poppins", 14), 
                                        fg_color="#444", corner_radius=6, wraplength=300)
                    self.bot_response_label.pack(side=RIGHT, anchor="ne", padx=10, pady=1, ipady=8, ipadx=10)
                    self.bot_image_label = ct.CTkLabel(self.bot_frame, text="", image=robo_imagem, fg_color="#f6f2f3") 
                    self.bot_image_label.pack(side=TOP, pady=13)
                    self.canvas.update_idletasks()
                    self.canvas.yview_moveto(1.0)

                if self.msgInput.get() :
                    print("Trabalhando")

                else:
                    pass
            except Exception:
                pass

    def configure_scroll_region(self, e):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
    def resize_frame(self, e):
        self.canvas.itemconfigure(self.scrollable_window, width=e.width-30)
        

ChatApp(janela)

cProfile.run("janela.mainloop()")