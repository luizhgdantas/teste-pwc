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

exemplos = [
    "Miritiba 339",
    "Babaçu 500",
    "Cambuí 804B",
    "Rio Branco 23",
    "Quirino dos Santos 23 b",
    "4, Rue de la République",
    "100 Broadway Av",
    "Calle Sagasta, 26",
    "Calle 44 No 1991"
]

for exemplo in exemplos:
    nome, numero = processar_endereco(exemplo)
    print(f"Entrada: {exemplo} -> Saída: {{'{nome}', '{numero}'}}")
