import tkinter as tk
from tkinter import ttk, messagebox

# ==========================
# DADOS INICIAIS
# ==========================
estoque_insumos = {"Arroz": 2000, "Feijão": 1000, "Carne": 1000, "Salada": 500}
estoque_bebidas = {"Coca-Cola": 10, "Guaraná": 10, "Suco": 10, "Água com gás": 10}
estoque_sobremesas = {"Pudim": 10, "Brownie": 10, "Bolo no pote": 10}

preco_marmita = {"P": 10.0, "M": 13.0, "G": 16.0}
preco_bebidas = {"Coca-Cola": 5.0, "Guaraná": 4.5, "Suco": 4.0, "Água com gás": 3.0}
preco_sobremesas = {"Pudim": 4.0, "Brownie": 5.0, "Bolo no pote": 6.0}

custo_insumos = {"Arroz": 0.02, "Feijão": 0.03, "Carne": 0.10, "Salada": 0.04}
consumo_marmita = {"Arroz": 100, "Feijão": 50, "Carne": 25, "Salada": 10}
vendas_realizadas = []

# ==========================
# FUNÇÕES PRINCIPAIS
# ==========================
def calcular_custo_marmita(tamanho):
    multiplicador = {"P": 1, "M": 1.5, "G": 2}
    custo = 0
    for insumo, gramas in consumo_marmita.items():
        custo += (gramas * multiplicador[tamanho] / 100) * custo_insumos[insumo]
    return round(custo, 2)

def verificar_estoque_marmita(tamanho):
    multiplicador = {"P": 1, "M": 1.5, "G": 2}
    for insumo, gramas in consumo_marmita.items():
        if estoque_insumos[insumo] < gramas * multiplicador[tamanho]:
            return False
    return True

def atualizar_estoque_marmita(tamanho):
    multiplicador = {"P": 1, "M": 1.5, "G": 2}
    for insumo, gramas in consumo_marmita.items():
        estoque_insumos[insumo] -= gramas * multiplicador[tamanho]

def atualizar_estoque_bebida(bebida):
    estoque_bebidas[bebida] -= 1

def atualizar_estoque_sobremesa(sobremesa):
    estoque_sobremesas[sobremesa] -= 1

def fazer_venda():
    tamanho = combo_marmita.get()
    bebida = combo_bebidas.get()
    sobremesa = combo_sobremesas.get()

    if not tamanho or not bebida or not sobremesa:
        messagebox.showerror("Erro", "Selecione todos os itens da venda!")
        return

    if not verificar_estoque_marmita(tamanho):
        messagebox.showwarning("Atenção", "Estoque de insumos insuficiente!")
        return
    if estoque_bebidas[bebida] <= 0:
        messagebox.showwarning("Atenção", f"Estoque de {bebida} insuficiente!")
        return
    if estoque_sobremesas[sobremesa] <= 0:
        messagebox.showwarning("Atenção", f"Estoque de {sobremesa} insuficiente!")
        return

    atualizar_estoque_marmita(tamanho)
    atualizar_estoque_bebida(bebida)
    atualizar_estoque_sobremesa(sobremesa)

    valor_venda = preco_marmita[tamanho] + preco_bebidas[bebida] + preco_sobremesas[sobremesa]
    custo = calcular_custo_marmita(tamanho)
    lucro = round(valor_venda - custo, 2)

    vendas_realizadas.append({
        "Marmita": tamanho,
        "Bebida": bebida,
        "Sobremesa": sobremesa,
        "Valor": valor_venda,
        "Custo": custo,
        "Lucro": lucro
    })

    messagebox.showinfo("Venda Realizada", f"Marmita vendida!\nTotal: R$ {valor_venda:.2f}\nLucro: R$ {lucro:.2f}")

def mostrar_estoque():
    texto = "=== Estoque de Insumos ===\n"
    for insumo, qtd in estoque_insumos.items():
        texto += f"{insumo}: {qtd}g\n"
    texto += "\n=== Estoque de Bebidas ===\n"
    for bebida, qtd in estoque_bebidas.items():
        texto += f"{bebida}: {qtd} unidades\n"
    texto += "\n=== Estoque de Sobremesas ===\n"
    for sobremesa, qtd in estoque_sobremesas.items():
        texto += f"{sobremesa}: {qtd} unidades\n"
    text_estoque.delete(1.0, tk.END)
    text_estoque.insert(tk.END, texto)

def repor_estoque():
    item = entry_item.get()
    try:
        quantidade = float(entry_qtd.get())
    except:
        messagebox.showerror("Erro", "Digite uma quantidade válida!")
        return

    if item in estoque_insumos:
        estoque_insumos[item] += quantidade
    elif item in estoque_bebidas:
        estoque_bebidas[item] += int(quantidade)
    elif item in estoque_sobremesas:
        estoque_sobremesas[item] += int(quantidade)
    else:
        messagebox.showerror("Erro", "Item não encontrado!")
        return

    messagebox.showinfo("Sucesso", f"{item} reabastecido!")
    entry_item.delete(0, tk.END)
    entry_qtd.delete(0, tk.END)
    mostrar_estoque()

def mostrar_relatorio():
    total_vendas = sum(v["Valor"] for v in vendas_realizadas)
    total_custo = sum(v["Custo"] for v in vendas_realizadas)
    total_lucro = round(total_vendas - total_custo, 2)

    texto = f"=== Relatório de Vendas ===\n"
    texto += f"Vendas realizadas: {len(vendas_realizadas)}\n"
    texto += f"Faturamento total: R$ {total_vendas:.2f}\n"
    texto += f"Custo total dos insumos: R$ {total_custo:.2f}\n"
    texto += f"Lucro líquido: R$ {total_lucro:.2f}\n\n"
    texto += "Detalhes das vendas:\n"
    for v in vendas_realizadas:
        texto += f"Marmita: {v['Marmita']}, Bebida: {v['Bebida']}, Sobremesa: {v['Sobremesa']}, Valor: R$ {v['Valor']:.2f}, Lucro: R$ {v['Lucro']:.2f}\n"

    text_relatorio.delete(1.0, tk.END)
    text_relatorio.insert(tk.END, texto)

    with open("relatorio_vendas.txt", "w") as file:
        file.write(texto)

# ==========================
# INTERFACE GRÁFICA
# ==========================
root = tk.Tk()
root.title("🍱 Sistema de Marmitex")
root.geometry("1000x1000")
root.configure(bg="#f0f0f0")

frame_menu = tk.Frame(root, bg="#ffcc99")
frame_venda = tk.Frame(root, bg="#ccffcc")
frame_estoque = tk.Frame(root, bg="#99ccff")
frame_relatorio = tk.Frame(root, bg="#ff9999")

for frame in (frame_menu, frame_venda, frame_estoque, frame_relatorio):
    frame.grid(row=0, column=0, sticky='nsew')

def mostrar_frame(frame):
    frame.tkraise()

# ==========================
# MENU PRINCIPAL
# ==========================
tk.Label(frame_menu, text="🍴 Controle de Marmitex", font=("Arial", 28, "bold"), bg="#ffcc99").pack(pady=30)
tk.Button(frame_menu, text="🛒 Fazer Venda", font=("Arial", 16), width=20, bg="#99ff99",
          command=lambda: mostrar_frame(frame_venda)).pack(pady=15)
tk.Button(frame_menu, text="📦 Estoque / Reposição", font=("Arial", 16), width=20, bg="#99ccff",
          command=lambda: [mostrar_frame(frame_estoque), mostrar_estoque()]).pack(pady=15)
tk.Button(frame_menu, text="💰 Relatório / Lucro", font=("Arial", 16), width=20, bg="#ff9999",
          command=lambda: [mostrar_frame(frame_relatorio), mostrar_relatorio()]).pack(pady=15)
tk.Button(frame_menu, text="❌ Sair", font=("Arial", 16), width=20, bg="#cccccc", command=root.quit).pack(pady=15)

# ==========================
# TELA DE VENDAS
# ==========================
tk.Label(frame_venda, text="🛒 Realizar Venda", font=("Arial", 22, "bold"), bg="#ccffcc").pack(pady=15)
tk.Label(frame_venda, text="Tamanho da Marmita:", font=("Arial", 14), bg="#ccffcc").pack()
combo_marmita = ttk.Combobox(frame_venda, values=["P", "M", "G"], state="readonly", font=("Arial", 12))
combo_marmita.pack(pady=5)

tk.Label(frame_venda, text="Bebida:", font=("Arial", 14), bg="#ccffcc").pack()
combo_bebidas = ttk.Combobox(frame_venda, values=list(estoque_bebidas.keys()), state="readonly", font=("Arial", 12))
combo_bebidas.pack(pady=5)

tk.Label(frame_venda, text="Sobremesa:", font=("Arial", 14), bg="#ccffcc").pack()
combo_sobremesas = ttk.Combobox(frame_venda, values=list(estoque_sobremesas.keys()), state="readonly", font=("Arial", 12))
combo_sobremesas.pack(pady=5)

tk.Button(frame_venda, text="💳 Finalizar Venda", font=("Arial", 14), bg="#66ff66", command=fazer_venda).pack(pady=15)
tk.Button(frame_venda, text="⬅ Voltar ao Menu", font=("Arial", 14), bg="#cccccc", command=lambda: mostrar_frame(frame_menu)).pack(pady=10)

# ==========================
# TELA DE ESTOQUE
# ==========================
tk.Label(frame_estoque, text="📦 Estoque e Reposição", font=("Arial", 22, "bold"), bg="#99ccff").pack(pady=10)
text_estoque = tk.Text(frame_estoque, height=15, width=85, font=("Arial", 12))
text_estoque.pack(pady=5)

tk.Label(frame_estoque, text="Item para repor:", font=("Arial", 14), bg="#99ccff").pack()
entry_item = tk.Entry(frame_estoque, font=("Arial", 12))
entry_item.pack(pady=2)
tk.Label(frame_estoque, text="Quantidade:", font=("Arial", 14), bg="#99ccff").pack()
entry_qtd = tk.Entry(frame_estoque, font=("Arial", 12))
entry_qtd.pack(pady=2)
tk.Button(frame_estoque, text="Repor Estoque", font=("Arial", 14), bg="#66ccff", command=repor_estoque).pack(pady=5)
tk.Button(frame_estoque, text="⬅ Voltar ao Menu", font=("Arial", 14), bg="#cccccc", command=lambda: mostrar_frame(frame_menu)).pack(pady=10)

# ==========================
# TELA DE RELATÓRIO
# ==========================
tk.Label(frame_relatorio, text="💰 Relatório de Vendas", font=("Arial", 22, "bold"), bg="#ff9999").pack(pady=10)
text_relatorio = tk.Text(frame_relatorio, height=20, width=85, font=("Arial", 12))
text_relatorio.pack(pady=5)
tk.Button(frame_relatorio, text="⬅ Voltar ao Menu", font=("Arial", 14), bg="#cccccc", command=lambda: mostrar_frame(frame_menu)).pack(pady=10)

# ==========================
# INICIA APLICAÇÃO
# ==========================
mostrar_frame(frame_menu)
root.mainloop()
