import tkinter as tk

janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry("1200x600")
janela.config(bg="white")

perfil = tk.PhotoImage(file='Menu - Top.png')
perfil_label = tk.Label(janela, image=perfil, bg='white')
perfil_label.pack(side='top', pady=5)
perfil_label.place(relx=0.5, rely=0.1, anchor='e')

logo = tk.PhotoImage(file='image 1.png')
logo_menor = logo.subsample(2, 2)
logo_label = tk.Label(janela, image=logo_menor, bg='white')
logo_label.pack(side='top', pady=5)
logo_label.place(relx=0.7, rely=0.1, anchor='w')

menu = tk.PhotoImage(file='Menu- Center.png')
menu_menor = menu.subsample(2, 2)
menu_label = tk.Label(janela, image=menu_menor, bg='white')
menu_label.pack(side='top', pady=5)
menu_label.place(relx=0.5, rely=0.5, anchor='center')

texto_label = tk.Label(janela, text="Precisa de ajuda?", font=('Arial', 20), fg='black', bg='white')
texto_label.pack(side='bottom', pady=5)
texto_label.place(relx=0.5, rely=0.9, anchor='center')

janela.mainloop()