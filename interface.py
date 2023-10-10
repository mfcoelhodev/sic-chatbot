from customtkinter import *
import customtkinter


app = CTk()
app.title("Chatbot Samsung")
app.geometry("800x600")
customtkinter.set_appearance_mode("dark")

texto = customtkinter.CTkLabel(master=app, text="Tire suas dúvidas", font=('Castellar', 25,), text_color=('#522fdf'))
texto.pack(padx=10, pady=40)

pergunta = CTkTextbox(master=app, scrollbar_button_hover_color='#522fdf', scrollbar_button_color="#a4e0cd", corner_radius=16, border_color="#a4e0cd", border_width=1)
pergunta.pack(padx=10, pady=5,)

def clique():
    print("Enviar")


botao = customtkinter.CTkButton(master=app, text="Enviar", command=clique,corner_radius=32, fg_color='#522fdf', width=20, height=20) 
botao.pack(padx=10, pady=10)


resposta = CTkTextbox(master=app, scrollbar_button_hover_color='#522fdf', scrollbar_button_color="#a4e0cd", corner_radius=16, border_color="#a4e0cd", border_width=1)
resposta.pack(padx=10, pady=5,)




app.mainloop()
