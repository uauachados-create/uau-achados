import json
from datetime import datetime

# ---------------------------------------------------------
# CONFIGURAÇÃO DAS SUAS TAGS DE AFILIADO
# ---------------------------------------------------------
TAG_AMAZON = "032018011983-20"  # Sua tag oficial da Amazon configurada
TAG_MERCADO_LIVRE = "18735177"  # Seu ID de afiliado do Mercado Livre configurado

# ---------------------------------------------------------
# BASE DE DADOS DOS PRODUTOS DOS NICHOS RENTÁVEIS
# ---------------------------------------------------------
produtos_nichos = [
    {
        "id": 1,
        "titulo": "Lâmpada Inteligente Smart Wi-Fi Compatível com Alexa",
        "preco_atual": 69.90,
        "imagem": "https://images.unsplash.com/photo-1550985561-0c9e3884b219?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO1"
    },
    {
        "id": 2,
        "titulo": "Aparador de Pelos Elétrico Corporal e Barba Skincare",
        "preco_atual": 119.90,
        "imagem": "https://images.unsplash.com/photo-1621607513511-96154d04655f?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo2"
    },
    {
        "id": 3,
        "titulo": "Creatina Monohidratada Pura 250g Suplemento Fitness",
        "preco_atual": 89.90,
        "imagem": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO3"
    },
    {
        "id": 4,
        "titulo": "Fonte Bebedouro Elétrica Automática para Gatos e Cães Pet",
        "preco_atual": 99.90,
        "imagem": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo4"
    },
    {
        "id": 5,
        "titulo": "Parafusadeira e Furadeira a Bateria 12V com Maleta e Acessórios",
        "preco_atual": 199.90,
        "imagem": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO5"
    }
]

def processar_vitrine(produtos):
    produtos_processados = []
    
    for p in produtos:
        link_afiliado = p["link_original"]
        
        if p["origem"] == "Amazon":
            separador = "&" if "?" in link_afiliado else "?"
            link_afiliado = f"{link_afiliado}{separador}tag={TAG_AMAZON}"
        elif p["origem"] == "Mercado Livre":
            separador = "&" if "?" in link_afiliado else "?"
            link_afiliado = f"{link_afiliado}{separador}matt_tool={TAG_MERCADO_LIVRE}"
            
        produto_final = {
            "id": p["id"],
            "titulo": p["titulo"],
            "preco": p["preco_atual"],
            "imagem": p["imagem"],
            "origem": p["origem"],
            "link_vitrine": link_afiliado,
            "atualizado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        produtos_processados.append(produto_final)
        
    return produtos_processados

if __name__ == "__main__":
    vitrine_atualizada = processar_vitrine(produtos_nichos)
    
    with open("vitrine_produtos.json", "w", encoding="utf-8") as f:
        json.dump(vitrine_atualizada, f, ensure_ascii=False, indent=4)
        
    print("Robô executado e vitrine atualizada com sucesso com as novas tags!")