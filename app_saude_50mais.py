import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Saúde 50+ | Treinos Seguros",
    page_icon="🏃‍♀️",
    layout="wide"
)

# Estilização básica
st.title("🏃‍♀️ Longevidade & Movimento 50+")
st.markdown("### Selecione suas condições articulares para filtrar apenas exercícios 100% seguros.")

# Barra lateral com anamnese rápida
st.sidebar.header("📋 Condições & Cuidados")
tem_condromalacia = st.sidebar.checkbox("Condromalácia Patelar", value=True)
tem_menisco = st.sidebar.checkbox("Menisco Rompido / Lesão Meniscal", value=True)
tem_artrose_quadril = st.sidebar.checkbox("Artrose no Quadril", value=True)

# Compilar condições selecionadas
restricoes_selecionadas = []
if tem_condromalacia:
    restricoes_selecionadas.append("condromalacia")
if tem_menisco:
    restricoes_selecionadas.append("menisco_rompido")
if tem_artrose_quadril:
    restricoes_selecionadas.append("artrose_quadril")

# Catálogo completo de exercícios
biblioteca = [
    {
        "nome": "Elevação Pélvica (Ponte)",
        "categoria": "Força & Glúteos",
        "material": "Esteira de EVA + Mini band leve",
        "prescricao": "3 séries de 10 a 12 repetições",
        "orientacao": "Deitada de barriga para cima, eleve o quadril acionando os glúteos. Mantenha os joelhos alinhados.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Exercício da Ostra (Clamshell)",
        "categoria": "Estabilidade de Quadril",
        "material": "Esteira de EVA + Bloco para apoiar a cabeça",
        "prescricao": "3 séries de 12 repetições por lado",
        "orientacao": "Deitada de lado, abra o joelho de cima mantendo calcanhares unidos. Ativa o glúteo médio sem pressão no menisco.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Elevação de Perna Reta (Straight Leg Raise)",
        "categoria": "Quadríceps Seguro",
        "material": "Esteira de EVA (+ Caneleira 0,5 a 1 kg opcional)",
        "prescricao": "3 séries de 10 repetições por perna (pausa de 3s no topo)",
        "orientacao": "Deitada de costas com perna estendida, contraia a coxa e eleve até a altura do outro joelho. Carga zero na patela.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Agachamento Isométrico Curto na Parede (Wall Sit)",
        "categoria": "Força de Pernas",
        "material": "Parede livre",
        "prescricao": "3 séries de 20 a 30 segundos",
        "orientacao": "Apoie as costas na parede e desça levemente (máximo 45°, nunca 90°). Mantém o músculo ativo sem atrito de dobra do joelho.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Remada Sentada",
        "categoria": "Tronco & Postura",
        "material": "Super Band + Esteira de EVA",
        "prescricao": "3 séries de 12 a 15 repetições",
        "orientacao": "Sentada na esteira, passe o elástico nos pés e puxe aproximando as escápulas. Fortalece costas sem impacto articular.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Flexão com Apoio de Joelhos",
        "categoria": "Membros Superiores",
        "material": "Barras de apoio para flexão + Esteira de EVA",
        "prescricao": "3 séries de 8 a 10 repetições",
        "orientacao": "As barras de apoio mantêm os punhos retos e neutros, evitando compressões articulares nas mãos e ombros.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Descompressão Suave na Barra",
        "categoria": "Descompressão",
        "material": "Barra de pendurar + Step de EVA para apoiar pés",
        "prescricao": "3 séries de 15 a 25 segundos",
        "orientacao": "Segure na barra e solte o peso mantendo as pontas dos pés no step para aliviar a pressão da lombar e anel pélvico.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Liberação Miofascial de Panturrilha e Glúteos",
        "categoria": "Recuperação",
        "material": "Rolo de liberação miofascial + Esteira",
        "prescricao": "3 a 5 minutos suaves antes/após o treino",
        "orientacao": "Role suavemente na musculatura carnosa. Atenção: nunca role em cima de ossos salientes ou direto na patela.",
        "tags_perigo": [],
        "contraindicacoes": []
    },
    {
        "nome": "Agachamento Livre Profundo",
        "categoria": "Pernas",
        "material": "Halteres 3 kg",
        "prescricao": "Não recomendado",
        "orientacao": "Flexão profunda sobrecarrega a cartilagem patelar.",
        "tags_perigo": ["flexao_joelho_acima_60"],
        "contraindicacoes": ["condromalacia", "menisco_rompido"]
    },
    {
        "nome": "Salto Pliométrico no Step",
        "categoria": "Cardio com Impacto",
        "material": "Step de EVA",
        "prescricao": "Não recomendado",
        "orientacao": "O impacto repetitivo gera impacto mecânico agressivo ao menisco e cartilagem.",
        "tags_perigo": ["impacto_alto"],
        "contraindicacoes": ["condromalacia", "menisco_rompido", "artrose_quadril"]
    },
    {
        "nome": "Torção Rápida no Círculo Giratório",
        "categoria": "Cintura Dinâmica",
        "material": "Círculo giratório",
        "prescricao": "Não recomendado",
        "orientacao": "Torções de quadril com pés fixos geram cisalhamento no menisco.",
        "tags_perigo": ["torcao_joelho"],
        "contraindicacoes": ["menisco_rompido", "artrose_quadril"]
    }
]

# Regras do filtro
tags_proibidas = set()
if "condromalacia" in restricoes_selecionadas:
    tags_proibidas.update(["flexao_joelho_acima_60", "impacto_alto"])
if "menisco_rompido" in restricoes_selecionadas:
    tags_proibidas.update(["torcao_joelho", "impacto_alto", "flexao_joelho_acima_60"])
if "artrose_quadril" in restricoes_selecionadas:
    tags_proibidas.update(["impacto_alto", "torcao_joelho"])

# Filtragem
aprovados = []
bloqueados = []

for ex in biblioteca:
    tem_contra = any(c in ex["contraindicacoes"] for c in restricoes_selecionadas)
    tem_perigo = any(t in tags_proibidas for t in ex["tags_perigo"])
    if not tem_contra and not tem_perigo:
        aprovados.append(ex)
    else:
        bloqueados.append(ex)

# Exibição dos cards
st.subheader(f"✅ Exercícios Recomendados e Seguros ({len(aprovados)})")
cols = st.columns(2)
for idx, ex in enumerate(aprovados):
    with cols[idx % 2]:
        with st.container(border=True):
            st.markdown(f"#### {ex['nome']}")
            st.caption(f"🎯 Foco: {ex['categoria']} | 🧰 Material: {ex['material']}")
            st.write(f"**Dose recomendada:** {ex['prescricao']}")
            st.info(f"💡 {ex['orientacao']}")

if bloqueados:
    with st.expander(f"⚠️ Ver exercícios bloqueados pelo filtro de segurança ({len(bloqueados)})"):
        for b in bloqueados:
            st.warning(f"❌ **{b['nome']}** — Motivo: {b['orientacao']}")
