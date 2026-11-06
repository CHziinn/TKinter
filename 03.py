import tkinter as tk

janela = tk.Tk()
janela.title("Palestras")
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
voltar_label.place(relx=0.1, rely=0.18, anchor='w')

logo = tk.PhotoImage(file='image 1.png')
logo_menor = logo.subsample(4, 4)
logo_label = tk.Label(janela, image=logo_menor, bg='white')
logo_label.pack(side='top', pady=5)
logo_label.place(relx=0.9, rely=0.1, anchor='w')

container_tabela = tk.Frame(janela, bg="#1e272e")
container_tabela.place(relx=0.5, rely=0.5, anchor="center")

categorias = ['Palestra', 'Data', 'Local', 'Valor', 'Duração']
colunas = 8

for index_coluna, cat in enumerate(categorias):
    label_cat = tk.Label(container_tabela, text=cat, font=("Arial", 14, "bold"), fg="#ffffff", bg="#53d7ec", width=15,)
    label_cat.grid(row=0, column=index_coluna, padx=10, pady=15)

    for index_linha in range(1, colunas + 1):
        texto_lorem = f"Lorem {index_linha}"

        label_dado = tk.Label(container_tabela, text=texto_lorem, font=("Arial", 12), fg="white", bg="#2c3e50", width=15, relief="solid", bd=1)
        label_dado.grid(row=index_linha, column=index_coluna, padx=5, pady=5)

janela.mainloop()