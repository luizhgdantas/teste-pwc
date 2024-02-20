import re

def processar_endereco(endereco):
    endereco = endereco.replace(",", "")

    match = re.match(r"(.*?)(\d+\s*\w*)$", endereco)
    
    if match:
        nome_rua = match.group(1).strip()
        numero_rua = match.group(2).strip()
        return nome_rua, numero_rua
    else:
        return None, None

enderecos = []

while True:
    endereco = input("Insira um endereço (ou digite 'sair' para encerrar): ")
    
    if endereco.lower() == 'sair':
        break
    
    enderecos.append(endereco)

for endereco in enderecos:
    nome, numero = processar_endereco(endereco)
    print(f"Entrada: {endereco} -> Saída: {{'{nome}', '{numero}'}}")
