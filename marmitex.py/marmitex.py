import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# --- CONFIGURAÇÕES DE INSUMOS ---

# Quantidades de insumos (em gramas) para cada tamanho de marmita
INSUMOS_POR_TAMANHO = {
    "P": {"Arroz": 100, "Feijão": 50, "Carne": 25, "Salada": 10},
    "M": {"Arroz": 150, "Feijão": 75, "Carne": 40, "Salada": 15},
    "G": {"Arroz": 200, "Feijão": 100, "Carne": 60, "Salada": 20},
}

# Estoque inicial (em gramas ou unidades)
estoque = {
    "Arroz": 500000,
    "Feijão": 250000,
    "Carne": 150000,
    "Salada": 80000,
    "Bebida": 30000,        # unidades
    "Sobremesa": 20000     # unidades
}

# Controle de vendas e consumo
total_vendas = {"P": 0, "M": 0, "G": 0}
vendas_bebida = 0
vendas_sobremesa = 0
insumos_usados = {item: 0 for item in estoque}


# --- FUNÇÕES PRINCIPAIS ---

def calcular_marmitas_possiveis(tamanho):
    """Calcula quantas marmitas de determinado tamanho podem ser feitas"""
    quantidades = []
    for item in INSUMOS_POR_TAMANHO[tamanho]:
        por_marmita = INSUMOS_POR_TAMANHO[tamanho][item]
        quantidades.append(estoque[item] // por_marmita)
    return min(quantidades)


def atualizar_interface():
    """Atualiza os textos de estoque e relatório"""
    texto_estoque = "📦 Estoque Atual:\n"
    for item, qtd in estoque.items():
        unidade = "g" if item not in ["Bebida", "Sobremesa"] else "unid."
        texto_estoque += f" - {item}: {qtd} {unidade}\n"
    label_estoque.config(text=texto_estoque)

    texto_marmitas = (
        f"👉 Marmitas possíveis:\n"
        f"  P: {calcular_marmitas_possiveis('P')} | "
        f"M: {calcular_marmitas_possiveis('M')} | "
        f"G: {calcular_marmitas_possiveis('G')}"
    )
    label_marmitas.config(text=texto_marmitas)

    total_geral = sum(total_vendas.values())
    texto_relatorio = (
        f"📊 RELATÓRIO DE PRODUÇÃO\n"
        f"🍱 Marmitas vendidas: {total_geral} (P: {total_vendas['P']} | M: {total_vendas['M']} | G: {total_vendas['G']})\n"
        f"🥤 Bebidas vendidas: {vendas_bebida}\n"
        f"🍰 Sobremesas vendidas: {vendas_sobremesa}\n\n"
        f"Insumos usados:\n"
    )
    for item, qtd in insumos_usados.items():
        unidade = "g" if item not in ["Bebida", "Sobremesa"] else "unid."
        texto_relatorio += f" - {item}: {qtd} {unidade}\n"

    label_relatorio.config(text=texto_relatorio)


def vender_marmita():
    """Registra a venda de marmita com opcional de bebida e sobremesa"""
    global vendas_bebida, vendas_sobremesa

    tamanho = var_tamanho.get()
    incluir_bebida = var_bebida.get()
    incluir_sobremesa = var_sobremesa.get()

    if tamanho not in INSUMOS_POR_TAMANHO:
        messagebox.showwarning("Erro", "Selecione um tamanho de marmita (P, M ou G).")
        return

    # Verifica estoque suficiente
    marmitas_possiveis = calcular_marmitas_possiveis(tamanho)
    if marmitas_possiveis <= 0:
        messagebox.showwarning("Estoque insuficiente", f"Não há insumos suficientes para marmitas {tamanho}.")
        return

    if incluir_bebida and estoque["Bebida"] <= 0:
        messagebox.showwarning("Estoque insuficiente", "Sem bebidas disponíveis no estoque.")
        return

    if incluir_sobremesa and estoque["Sobremesa"] <= 0:
        messagebox.showwarning("Estoque insuficiente", "Sem sobremesas disponíveis no estoque.")
        return

    # Diminui insumos da marmita
    for item in INSUMOS_POR_TAMANHO[tamanho]:
        gasto = INSUMOS_POR_TAMANHO[tamanho][item]
        estoque[item] -= gasto
        insumos_usados[item] += gasto

    total_vendas[tamanho] += 1

    # Se houver bebida e/ou sobremesa
    if incluir_bebida:
        estoque["Bebida"] -= 1
        insumos_usados["Bebida"] += 1
        vendas_bebida += 1

    if incluir_sobremesa:
        estoque["Sobremesa"] -= 1
        insumos_usados["Sobremesa"] += 1
        vendas_sobremesa += 1

    atualizar_interface()
    msg = f"✅ Marmita {tamanho} feita com sucesso!"
    if incluir_bebida:
        msg += "\n+ Bebida incluída."
    if incluir_sobremesa:
        msg += "\n+ Sobremesa incluída."
    messagebox.showinfo("Venda registrada", msg)


def repor_insumo():
    """Permite repor insumos, bebidas ou sobremesas"""
    insumo = entry_insumo.get().capitalize()
    quantidade = entry_quantidade.get()

    if insumo not in estoque:
        messagebox.showerror("Erro", "Esse insumo não existe! Use: Arroz, Feijão, Carne, Salada, Bebida ou Sobremesa.")
        return

    if not quantidade.isdigit():
        messagebox.showerror("Erro", "Digite uma quantidade válida (apenas números).")
        return

    quantidade = int(quantidade)
    estoque[insumo] += quantidade

    entry_insumo.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)

    atualizar_interface()
    messagebox.showinfo("Reposição", f"✅ {quantidade} adicionados ao estoque de {insumo}.")


# --- INTERFACE GRÁFICA ---

janela = tk.Tk()
janela.title("🍱 Controle de Marmitex + Bebidas + Sobremesas")
janela.geometry("900x700")

# Imagem de fundo
imagem_fundo = Image.open("fundo.jpg")
imagem_fundo = imagem_fundo.resize((900, 700))
bg = ImageTk.PhotoImage(imagem_fundo)
label_bg = tk.Label(janela, image=bg)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# Título
titulo = tk.Label(janela, text="🍱 Sistema Completo de Marmitex", font=("Arial", 22, "bold"), bg="#ffffff")
titulo.pack(pady=10)

# Estoque
label_estoque = tk.Label(janela, text="", font=("Arial", 13), bg="#ffffff", justify="left")
label_estoque.pack(pady=5)

# Quantidade de marmitas possíveis
label_marmitas = tk.Label(janela, text="", font=("Arial", 14, "bold"), bg="#ffffff")
label_marmitas.pack(pady=5)

# Seleção de tamanho
frame_tamanho = tk.Frame(janela, bg="#ffffff")
frame_tamanho.pack(pady=10)
tk.Label(frame_tamanho, text="Escolha o tamanho da marmita:", font=("Arial", 13, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=3)

var_tamanho = tk.StringVar(value="P")
tk.Radiobutton(frame_tamanho, text="Pequena (P)", variable=var_tamanho, value="P", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, padx=10)
tk.Radiobutton(frame_tamanho, text="Média (M)", variable=var_tamanho, value="M", font=("Arial", 12), bg="#ffffff").grid(row=1, column=1, padx=10)
tk.Radiobutton(frame_tamanho, text="Grande (G)", variable=var_tamanho, value="G", font=("Arial", 12), bg="#ffffff").grid(row=1, column=2, padx=10)

# Checkboxes para bebida e sobremesa
frame_extra = tk.Frame(janela, bg="#ffffff")
frame_extra.pack(pady=10)
var_bebida = tk.BooleanVar()
var_sobremesa = tk.BooleanVar()
tk.Checkbutton(frame_extra, text="Incluir Bebida 🥤", variable=var_bebida, font=("Arial", 12), bg="#ffffff").pack(side="left", padx=15)
tk.Checkbutton(frame_extra, text="Incluir Sobremesa 🍰", variable=var_sobremesa, font=("Arial", 12), bg="#ffffff").pack(side="left", padx=15)

# Botão de venda
btn_vender = tk.Button(janela, text="🍛 Fazer Marmita", font=("Arial", 14), bg="#4CAF50", fg="white", command=vender_marmita)
btn_vender.pack(pady=10)

# Frame de reposição
frame_repor = tk.Frame(janela, bg="#ffffff")
frame_repor.pack(pady=15)

tk.Label(frame_repor, text="Reposição de Estoque", font=("Arial", 14, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(frame_repor, text="Item:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, sticky="e", padx=5)
entry_insumo = tk.Entry(frame_repor, font=("Arial", 12))
entry_insumo.grid(row=1, column=1, padx=5)

tk.Label(frame_repor, text="Quantidade:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, sticky="e", padx=5)
entry_quantidade = tk.Entry(frame_repor, font=("Arial", 12))
entry_quantidade.grid(row=2, column=1, padx=5)

btn_repor = tk.Button(frame_repor, text="Repor Estoque", font=("Arial", 12), bg="#2196F3", fg="white", command=repor_insumo)
btn_repor.grid(row=3, column=0, columnspan=2, pady=10)

# Relatório
label_relatorio = tk.Label(janela, text="", font=("Arial", 12), bg="#ffffff", justify="left")
label_relatorio.pack(pady=10)

# Atualizar interface
atualizar_interface()

# Iniciar janela
janela.mainloop()
