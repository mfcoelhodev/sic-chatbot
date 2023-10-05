import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x300")

def clique():
    print("Enviar")

texto = customtkinter.CTkLabel(janela, text="Tire suas dúvidas")
texto.pack(padx=10, pady=80)

pergunta = customtkinter.CTkEntry(janela, placeholder_text= "Pergunta:")
pergunta.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Enviar", command=clique) 
botao.pack(padx=10, pady=10)

janela.mainloop()