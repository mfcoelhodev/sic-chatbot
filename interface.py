from customtkinter import *
import customtkinter


app = CTk()
app.title("Chatbot Samsung")
app.geometry("800x600")
customtkinter.set_appearance_mode("light")

texto = customtkinter.CTkLabel(master=app, text="Tire suas dúvidas", font=('Franklin Gothic Demi Cond', 25,), text_color=('#0100a2'))
texto.pack(padx=10, pady=40)
#007aff
pergunta = CTkTextbox(master=app, scrollbar_button_hover_color='#090f11', scrollbar_button_color="#090f11", corner_radius=20, border_color="#090f11", border_width=2)
pergunta.pack(padx=10, pady=5,)
#522fdf
#a4e0cd
#a4e0cd
def clique():
    print("Enviar")


botao = customtkinter.CTkButton(master=app, text="Enviar", command=clique,corner_radius=32, fg_color='#0100a2', width=40, height=40) 
botao.pack(padx=10, pady=10)


resposta = CTkTextbox(master=app, scrollbar_button_hover_color='#090f11', scrollbar_button_color="#090f11", corner_radius=20, border_color="#090f11", border_width=2)
resposta.pack(padx=10, pady=5,)




app.mainloop()
