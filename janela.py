import customtkinter


customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')
janela = customtkinter.CTk()
janela.geometry("500x300")
def clique():
    print("Fazer Login")
   
texto = customtkinter.CTkLabel(janela, text='Fazer Login')
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Seu e-mail')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='Sua senha', show='*')
senha.pack(padx=10, pady=10)

check_box = customtkinter.CTkCheckBox(janela, text='Lembrar Login')
check_box.pack(padx=10, pady=10)
    
butao = customtkinter.CTkButton(janela, text='Login', command=clique)
butao.pack(padx=10, pady=10)
janela.mainloop()