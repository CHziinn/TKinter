import tkinter as tk

janela = tk.Tk()
janela.title("Palestras")
janela.geometry("1200x600")
janela.config(bg="white")

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