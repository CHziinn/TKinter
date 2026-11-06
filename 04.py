import tkinter as tk

janela = tk.Tk()
janela.title("Editar Consulta")
janela.geometry("1200x600")
janela.config(bg="white")

perfil = tk.PhotoImage(file='Menu - Top.png')
perfil_menor = perfil.subsample(2, 2)
perfil_label = tk.Label(janela, image=perfil_menor, bg='white')
perfil_label.pack(side='top', pady=5)
perfil_label.place(relx=0.2, rely=0.1, anchor='e')

voltar = tk.PhotoImage(file='Back.png')
voltar_label = tk.Label(janela, image=voltar, bg='white')
voltar_label.pack(side='top', pady=5)
voltar_label.place(relx=0.2, rely=0.18, anchor='e')

logo = tk.PhotoImage(file='image 1.png')
logo_menor = logo.subsample(4, 4)
logo_label = tk.Label(janela, image=logo_menor, bg='white')
logo_label.pack(side='top', pady=5)
logo_label.place(relx=0.9, rely=0.1, anchor='w')

texto_label = tk.Label(janela, text="Editar Consulta", font=('Arial', 20), fg="#79D5EC", bg='white')
texto_label.pack(side='top', pady=5)
texto_label.place(relx=0.5, rely=0.3, anchor='center')

nome_label = tk.Label(janela, text="Nome", font=('Arial', 15), fg='black', bg='white')
nome_label.pack(pady=20)
nome_label.place(relx = 0.35, rely = 0.45, anchor = 'center')

nome = tk.Entry(janela, text="Nome", font=('Arial', 15), fg='black', bg='white')
nome.pack(pady=20)
nome.place(relx = 0.35, rely = 0.5, anchor = 'center')

data_label = tk.Label(janela, text="Data", font=('Arial', 15), fg='black', bg='white')
data_label.pack(pady=20)
data_label.place(relx = 0.64, rely = 0.45, anchor = 'center')

data = tk.Entry(janela, text="Data", font=('Arial', 15), fg='black', bg='white')
data.pack(pady=20)
data.place(relx = 0.54, rely = 0.5, anchor = 'w')

rua = tk.Label(janela, text="Rua", font=('Arial', 15), fg='black', bg='white')
rua.pack(pady=20)
rua.place(relx = 0.5, rely = 0.55, anchor = 'center')

rua = tk.Entry(janela, text="Rua", font=('Arial', 15), fg='black', bg='white', width=50)
rua.pack(pady=20)
rua.place(relx = 0.5, rely = 0.6, anchor = 'center')

info_extra_label = tk.Label(janela, text="Informações Extras", font=('Arial', 15), fg='black', bg='white')
info_extra_label.pack(pady=20)
info_extra_label.place(relx = 0.5, rely = 0.66, anchor = 'center')

info_extra_label = tk.Entry(janela, text="Informações Extras", font=('Arial', 15), fg='black', bg='white', width=50)
info_extra_label.pack(pady=20)
info_extra_label.place(relx = 0.5, rely = 0.71, anchor = 'center')

dr_nome_label = tk.Label(janela, text="Nome do Doutor", font=('Arial', 15), fg='black', bg='white')
dr_nome_label.pack(pady=20)
dr_nome_label.place(relx = 0.5, rely = 0.77, anchor = 'center')

dr_nome_label = tk.Entry(janela, text="Nome do Doutor", font=('Arial', 15), fg='black', bg='white', width=50)
dr_nome_label.pack(pady=20)
dr_nome_label.place(relx = 0.5, rely = 0.82, anchor = 'center')

anexo = tk.Label(janela, text="Anexo", font=('Arial', 15), fg='black', bg='white')
anexo.pack(pady=20)
anexo.place(relx = 0.5, rely = 0.88, anchor = 'center')

editar = tk.Button(janela, text="Editar", font=('Arial', 15), fg='white', bg="#090909")
editar.pack(pady=20)
editar.place(relx = 0.5, rely = 0.94, anchor = 'center')

janela.mainloop()