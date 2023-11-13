import tkinter as tk
from tkinter import *
import customtkinter as ct
from PIL import Image, ImageTk
import time
import os
import cProfile, random
import webbrowser

#from generate import conversa_com_chatbot

root = ct.CTk()
root.title("Assistente Virtual")
ct.set_appearance_mode("light") #dark
ct.set_default_color_theme=('#f6f2f3')
bgColor = "#f6f2f3"   #black
root.configure(fg_color=bgColor)
root.geometry("1000x650+500+100")

file_path = "imagename.txt"

if os.path.exists(file_path):
    pass
else:
    with open(file_path, "x") as f:
        pass

with open(file_path, "w") as img_src:
    image_list ='imagens\\avator.png'
    my_image = image_list
    print(my_image)
    img_src.write(f"{my_image}")

def abrir_link():
        link = 'https://www.samsung.com/br/'
        webbrowser.open(link)


class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.resizable(True, True)
        self.root.geometry("520x620+500+100")

        self.optionFram = Frame(root, bg="#f6f2f3") #black
        # All imagas for chatfram code

        manIconSrc2 = Image.open("imagens\\samsung_avatar-removebg-preview.png")
        manIconImage2 = ImageTk.PhotoImage(manIconSrc2.resize((40, 40)))
        submitIconSrc = Image.open("imagens\\enviar.png")
        submitIconImage = ImageTk.PhotoImage(submitIconSrc.resize((40, 40)))
        messageIconSrc = Image.open("imagens\\message.png")
        messageIconImage = ImageTk.PhotoImage(messageIconSrc.resize((40, 40)))
        chatIconSrc = Image.open("imagens\\samsung.png")
        chatIconImage = ImageTk.PhotoImage(chatIconSrc.resize((50, 60)))

        # All imagas for chatfram code ends here

        self.messageIcon = ct.CTkButton(self.optionFram, text="",image=messageIconImage, width=0, bg_color=bgColor, fg_color=bgColor)
        self.messageIcon.pack(side=RIGHT, anchor="nw", padx=5, pady=5)

        self.manIcon2 = ct.CTkButton(self.optionFram, text="",image=manIconImage2, height=1, width=1, bg_color=bgColor, fg_color=bgColor,
                                corner_radius=20)
        self.manIcon2.pack(side=LEFT, anchor="ne")

        self.username = ct.CTkLabel(self.optionFram, text="Fale com a SAM", font=("consolas", 20), text_color="#010100") #d8d8df
        self.username.pack(side=LEFT, padx=5, pady=7, anchor="ne")
        self.optionFram.pack(side=TOP, fill=X, anchor="n")

        self.canvas = tk.Canvas(root, bg="#f6f2f3", highlightthickness=0) #black

        self.label_frame = tk.Frame(self.canvas, bg="#f6f2f3") #black
        self.label_frame.pack(side="left", fill="both", expand=True) 

        self.scrollable_window = self.canvas.create_window((0, 0), window=self.label_frame, anchor="nw")

        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.label_frame.bind("<Configure>", self.configure_scroll_region)

        self.scrollbar = ct.CTkScrollbar(self.canvas, orientation="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.yview_moveto(1.0)

        self.scrollbar.pack(side="right", fill=Y)

        self.canvas.bind("<Configure>", self.resize_frame)
        self.canvas.pack(side=TOP, fill=BOTH)

        bgColorChatFram = "#7eabde" #080420
        self.chatFram = Frame(root, bg=bgColorChatFram)

        self.chatIcon = ct.CTkButton(self.chatFram, text="",image=chatIconImage, width=20, bg_color=bgColorChatFram, fg_color=bgColorChatFram)
        self.chatIcon.pack(side=LEFT, padx=5)
        self.chatIcon.configure(command=abrir_link)

        self.msgInput = ct.CTkEntry(self.chatFram, placeholder_text="Digite sua pergunta aqui ...", height=40, font=("consolas", 18))
        self.msgInput.pack(side=LEFT, pady=10, padx=0, fill=X, expand=True)

        self.submitBtn = ct.CTkButton(self.chatFram, text="", image=submitIconImage, bg_color=bgColorChatFram, fg_color=bgColorChatFram, height=40, width=20, hover_color=bgColorChatFram)
        self.submitBtn.pack(side=LEFT, padx=0, pady=8)
        self.submitBtn.configure(command=self.sendMessage)

        self.chatFram.pack(side=BOTTOM, fill=X, ipady=5)

        self.root.bind("<Return>", lambda event: self.sendMessage())

    def sendMessage(self):
        with open(file_path, "r") as f:
            self.imagename = f.read()
            print(self.imagename)

        self.message = (self.msgInput.get())
        self.msgInput.delete(0, END)
        user_image_src = Image.open(self.imagename)
        user_image = ImageTk.PhotoImage(user_image_src.resize((40, 40)))        
        bot_image_src = Image.open("imagens\\robot.png")
        bot_image = ImageTk.PhotoImage(bot_image_src.resize((40, 40)))
        if self.message != "":
            self.current_time = time.strftime("%H:%M")
            self.current_time_label = ct.CTkLabel(self.label_frame, text=self.current_time, font=("consolas", 12))
            self.current_time_label.pack(side=TOP, anchor="ne", pady=0, padx=45)

            self.user_frame = ct.CTkFrame(self.label_frame, fg_color="#f6f2f3") # borda do pergunta
            self.user_frame.pack(side=TOP, anchor="ne")
            self.user_label = ct.CTkLabel(self.user_frame, text=self.message, font=("Poppins", 15), fg_color="#95bbc9", corner_radius=4,wraplength=250) #419f5b
                                    
            self.user_label.pack(side=LEFT, anchor="nw", pady=1, ipadx=15, ipady=6, padx=10)
            self.user_image_label = ct.CTkLabel(self.user_frame, text="", image=user_image, fg_color="#f6f2f3") #borda pergunta do icone 
            self.user_image_label.pack(side=TOP, pady=13)
            self.root.update_idletasks()
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)
            try:
                #self.to_respond = conversa_com_chatbot(self.message)
                if self.to_respond:
                    self.current_time = time.strftime("%H:%M")
                    self.current_time_label = ct.CTkLabel(self.label_frame, text=self.current_time, font=("consolas", 12))
                    self.current_time_label.pack(side=TOP, anchor="nw", pady=0, padx=55)
                    self.bot_frame = ct.CTkFrame(self.label_frame, fg_color="#f6f2f3")#black
                    self.bot_frame.pack(side=TOP, anchor="nw", padx=10)
                    self.bot_response_label = ct.CTkLabel(self.bot_frame, text=self.to_respond, font=("Poppins", 14), fg_color="#444", corner_radius=6, wraplength=300)                
                    self.bot_response_label.pack(side=RIGHT, anchor="ne", padx=10, pady=1, ipady=8, ipadx=10)
                    self.bot_image_label = ct.CTkLabel(self.bot_frame, text="", image=bot_image, fg_color="#f6f2f3")#black
                    self.bot_image_label.pack(side=TOP, pady=13)
                    self.canvas.update_idletasks()
                    self.canvas.yview_moveto(1.0)

                if self.msgInput.get() :
                    print("Working")

                else:
                    pass
            except Exception:
                pass

    def configure_scroll_region(self, e):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        
    def resize_frame(self, e):
        self.canvas.itemconfigure(self.scrollable_window, width=e.width-30)
        
# AvatorPage(root)
ChatApp(root)

cProfile.run('root.mainloop()')