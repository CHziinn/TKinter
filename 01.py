import tkinter as tk

janela = tk.Tk()

janela.title("Minha Janela")
janela.geometry("1200x600")

janela.config(bg="white")

logo = tk.PhotoImage(file='image 1.png')
label_logo = tk.Label(janela, image=logo, bg='white')
label_logo.pack(side='top', pady=20)

email_label = tk.Label(janela, text="Email", font=('Arial', 15), fg='black', bg='white')
email_label.pack(pady=20)
email_label.place(relx = 0.4, rely = 0.4, anchor = 'center')

email = tk.Entry(janela, font=('Arial', 20), fg='white', bg='gray')
email.pack(pady=20)
email.place(relx = 0.5, rely = 0.5, anchor = 'center')

senha_label = tk.Label(janela, text="Senha", font=('Arial', 15), fg='black', bg='white')
senha_label.pack(pady=20)
senha_label.place(relx = 0.4, rely = 0.6, anchor = 'center')

senha = tk.Entry(janela, font=('Arial', 20), fg='white', bg='gray')
senha.pack(pady=20)
senha.place(relx = 0.5, rely = 0.7, anchor = 'center')

acessar = tk.Button(janela, text="Acessar", font=('Arial', 15), fg='#3498db', bg='#2c3e50')
acessar.pack(pady=20)
acessar.place(relx = 0.5, rely = 0.8, anchor = 'center')

primeiro_acesso = tk.Button(janela, text="Primeiro Acesso", font=('Arial', 15), fg='navy', bg='cyan')
primeiro_acesso.pack(pady=20)
primeiro_acesso.place(relx = 0.5, rely = 0.9, anchor = 'center')

janela.mainloop()