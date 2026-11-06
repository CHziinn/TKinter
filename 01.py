import tkinter as tk

janela = tk.Tk()

janela.title("Minha Janela")
janela.geometry("1200x600")

janela.config(bg="blue")

texto = tk.Label(janela, text='Minha Janela', font=('Arial', 20), fg='white', bg='blue')
texto.pack(pady=20)

janela.mainloop()