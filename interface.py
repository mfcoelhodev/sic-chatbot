import customtkinter


janela = customtkinter.CTk()
janela.geometry("800x600")
janela.title("Sistema  de pergunda da Samsung")
customtkinter.set_appearance_mode("dark")


def clique():
    print("Enviar")



texto = customtkinter.CTkLabel(janela, text="Tire suas dúvidas", font=('arial bold', 30,))
texto.pack(padx=10, pady=40)

pergunta = customtkinter.CTkEntry(janela, placeholder_text= "Pergunta:", width=250, height=45)
pergunta.pack(padx=10, pady=10)


botao = customtkinter.CTkButton(janela, text="Enviar", command=clique,corner_radius=32, fg_color='#522fdf', width=20, height=20) 
botao.pack(padx=10, pady=10)

resposta = customtkinter.CTkEntry(janela, placeholder_text= "resposta:", width=250, height=45)
resposta.pack(padx=10, pady=10)


janela.mainloop()