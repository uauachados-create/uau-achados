import json
import urllib.request
import urllib.parse
from datetime import datetime

# Sua Tag de Afiliado
TAG_MERCADO_LIVRE = "18735177"

# Seus 5 nichos exatos
NICHOS = {
    "Casa Inteligente": "smart home alexa intelbras",
    "Beleza & Skincare": "skincare limpeza de pele",
    "Fitness & Office": "equipamento academia escritorio",
    "Pets": "acessorios pet shop",
    "Ferramentas": "kit ferramentas maleta"
}

def buscar_produtos():
    produtos = []
    id_atual = 1
    
    for nicho, busca in NICHOS.items():
        print(f"Buscando 50 produtos de {nicho}...")
        # Aqui está a mágica: limit=50 garante 50 produtos reais por nicho!
        url = f"https://api.mercadolibre.com/sites/MLB/search?q={urllib.parse.quote(busca)}&limit=50"
        
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                dados = json.loads(response.read().decode())
                
                for item in dados.get("results", []):
                    # Garante foto em alta resolução e link que não quebra
                    imagem_real = item["thumbnail"].replace("http://", "https://").replace("-I.jpg", "-V.jpg")
                    link_original = item["permalink"]
                    
                    # Coloca a sua comissão
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
            print(f"Erro em {nicho}: {e}")
            
    return produtos

# Salva o arquivo final gigante
vitrine = buscar_produtos()
with open("vitrine_produtos.json", "w", encoding="utf-8") as f:
    json.dump(vitrine, f, ensure_ascii=False, indent=2)

print(f"✨ SUCESSO! Vitrine gerada com {len(vitrine)} produtos.")
