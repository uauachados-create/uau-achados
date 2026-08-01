import json
import requests
from datetime import datetime

# Seu ID de afiliado
TAG_MERCADO_LIVRE = "18735177"

# Os 4 nichos e as palavras-chave que o robô vai buscar sozinho
NICHOS = {
    "Tecnologia": "smart home alexa",
    "Casa": "utilidades domesticas eletroportateis",
    "Fitness": "equipamentos musculação",
    "Pets": "acessorios pet shop"
}

def buscar_produtos():
    produtos = []
    id_atual = 1
    
    for nicho, busca in NICHOS.items():
        # Acessa o sistema do Mercado Livre pedindo 50 produtos reais
        url = f"https://api.mercadolibre.com/sites/MLB/search?q={busca}&limit=50"
        
        try:
            resposta = requests.get(url)
            dados = resposta.json()
            
            for item in dados.get("results", []):
                # Pega a foto original e garante um formato médio confiável que não quebra
                imagem_real = item["thumbnail"].replace("http://", "https://").replace("-I.jpg", "-V.jpg")
                link_original = item["permalink"]
                
                # Adiciona sua tag de comissão automaticamente
                separador = "&" if "?" in link_original else "?"
                link_afiliado = f"{link_original}{separador}matt_tool={TAG_MERCADO_LIVRE}"
                
                produtos.append({
                    "id": id_atual,
                    "titulo": item["title"],
                    "preco": item["price"],
                    "imagem": imagem_real,
                    "origem": "Mercado Livre",
                    "nicho": nicho,
                    "link_vitrine": link_afiliado,
                    "atualizado_em": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                id_atual += 1
                
        except Exception as e:
            print(f"Erro ao buscar {nicho}: {e}")
            
    return produtos

# Executa e salva o JSON com os 200 produtos reais
vitrine = buscar_produtos()
with open("vitrine_produtos.json", "w", encoding="utf-8") as f:
    json.dump(vitrine, f, ensure_ascii=False, indent=4)
