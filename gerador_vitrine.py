import json
import requests
from datetime import datetime

TAG_MERCADO_LIVRE = "18735177"

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
    # Disfarce para o Mercado Livre não bloquear o robô
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    for nicho, busca in NICHOS.items():
        print(f"Buscando produtos de {nicho}...")
        url = f"https://api.mercadolibre.com/sites/MLB/search?q={busca}&limit=50"
        
        try:
            resposta = requests.get(url, headers=headers)
            if resposta.status_code == 200:
                dados = resposta.json()
                
                for item in dados.get("results", []):
                    imagem_real = item["thumbnail"].replace("http://", "https://").replace("-I.jpg", "-V.jpg")
                    link_original = item["permalink"]
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
            else:
                print(f"Erro na API do ML para {nicho}: Status {resposta.status_code}")
                
        except Exception as e:
            print(f"Erro de conexão em {nicho}: {e}")
            
    return produtos

vitrine = buscar_produtos()

# TRAVA DE SEGURANÇA: Só salva o arquivo se encontrou mais de 100 produtos
if len(vitrine) > 100:
    with open("vitrine_produtos.json", "w", encoding="utf-8") as f:
        json.dump(vitrine, f, ensure_ascii=False, indent=4)
    print(f"✨ SUCESSO! Vitrine salva com {len(vitrine)} produtos.")
else:
    print("⚠️ ERRO: O robô não conseguiu baixar os produtos. O arquivo não foi apagado para não quebrar o site.")
