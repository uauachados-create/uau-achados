import json
from datetime import datetime

# ---------------------------------------------------------
# CONFIGURAÇÃO DAS SUAS TAGS DE AFILIADO
# ---------------------------------------------------------
TAG_AMAZON = "032018011983-20"
TAG_MERCADO_LIVRE = "18735177"

# ---------------------------------------------------------
# BASE DE DADOS AMPLIADA (20+ PRODUTOS DE VÁRIOS NICHOS)
# ---------------------------------------------------------
produtos_nichos = [
    # --- TECNOLOGIA E CASA INTELIGENTE ---
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
        "titulo": "Echo Dot 5ª Geração Caixa de Som Inteligente com Alexa",
        "preco_atual": 399.00,
        "imagem": "https://images.unsplash.com/photo-1543512214-318c7553f230?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO2"
    },
    {
        "id": 3,
        "titulo": "Tomada Inteligente Wi-Fi Medidor de Consumo de Energia",
        "preco_atual": 54.90,
        "imagem": "https://images.unsplash.com/photo-1558089687-f282ffcbc126?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo3"
    },
    {
        "id": 4,
        "titulo": "Fita LED RGB Wi-Fi Smart 5 Metros com Controle e Voz",
        "preco_atual": 79.90,
        "imagem": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo4"
    },
    {
        "id": 5,
        "titulo": "Suporte Veicular Magnético para Smartphone com Carregador",
        "preco_atual": 89.90,
        "imagem": "https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO5"
    },

    # --- FITNESS E SAÚDE ---
    {
        "id": 6,
        "titulo": "Creatina Monohidratada Pura 250g Suplemento Importado",
        "preco_atual": 89.90,
        "imagem": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO6"
    },
    {
        "id": 7,
        "titulo": "Whey Protein Concentrado 1kg Sabor Chocolate",
        "preco_atual": 99.90,
        "imagem": "https://images.unsplash.com/photo-1579722820308-d74e571900a0?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo7"
    },
    {
        "id": 8,
        "titulo": "Kit Faixas Elásticas Extensoras Super Band para Exercícios",
        "preco_atual": 49.90,
        "imagem": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO8"
    },
    {
        "id": 9,
        "titulo": "Garrafa Squeeze Motivacional 2 Litros com Alça",
        "preco_atual": 39.90,
        "imagem": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo9"
    },
    {
        "id": 10,
        "titulo": "Corda de Pular Profissional com Rolamento em Aço",
        "preco_atual": 34.90,
        "imagem": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO10"
    },

    # --- PET SHOP ---
    {
        "id": 11,
        "titulo": "Fonte Bebedouro Elétrica Automática para Gatos e Cães",
        "preco_atual": 99.90,
        "imagem": "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo11"
    },
    {
        "id": 12,
        "titulo": "Tapete Higiênico Super Absorvente para Cães 30 Unidades",
        "preco_atual": 59.90,
        "imagem": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO12"
    },
    {
        "id": 13,
        "titulo": "Brinquedo Interativo Comedouro Lento Pet Anti-Stress",
        "preco_atual": 45.00,
        "imagem": "https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo13"
    },
    {
        "id": 14,
        "titulo": "Escova Remove Pelos e Subpêlos Cães e Gatos Autolimpante",
        "preco_atual": 29.90,
        "imagem": "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO14"
    },

    # --- CASA, FERRAMENTAS E UTILIDADES ---
    {
        "id": 15,
        "titulo": "Parafusadeira e Furadeira a Bateria 12V com Maleta e Acessórios",
        "preco_atual": 199.90,
        "imagem": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO15"
    },
    {
        "id": 16,
        "titulo": "Aparador de Pelos Elétrico Corporal e Barba Skincare",
        "preco_atual": 119.90,
        "imagem": "https://images.unsplash.com/photo-1621607513511-96154d04655f?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo16"
    },
    {
        "id": 17,
        "titulo": "Robô Aspirador de Pó Inteligente Bivolt Varre e Passa Pano",
        "preco_atual": 349.00,
        "imagem": "https://images.unsplash.com/photo-1518640467707-6811f4a6ab73?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO17"
    },
    {
        "id": 18,
        "titulo": "Panela Elétrica de Arroz 10 Xícaras com Bandeja para Vapor",
        "preco_atual": 179.90,
        "imagem": "https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo18"
    },
    {
        "id": 19,
        "titulo": "Air Fryer Fritadeira Sem Óleo 4 Litros Digital Antiaderente",
        "preco_atual": 329.90,
        "imagem": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=500&auto=format&fit=crop&q=60",
        "origem": "Amazon",
        "link_original": "https://www.amazon.com.br/dp/EXEMPLO19"
    },
    {
        "id": 20,
        "titulo": "Mini Processador de Alimentos Elétrico USB Portátil 250ml",
        "preco_atual": 49.90,
        "imagem": "https://images.unsplash.com/photo-1594385208974-2e75f8d7bb48?w=500&auto=format&fit=crop&q=60",
        "origem": "Mercado Livre",
        "link_original": "https://www.mercadolivre.com.br/exemplo20"
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
        
    print("Vitrine atualizada com sucesso com 20+ produtos!")
