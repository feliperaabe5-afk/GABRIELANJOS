"""
Site do Personal Trainer Gabriel Anjos Rosa — aplicação Flask.

Para rodar:
    pip install -r requirements.txt
    python app.py

Depois abra http://127.0.0.1:5000 no navegador.

Todos os dados (contato, preços, depoimentos) ficam neste arquivo,
em dicionários simples — edite os valores abaixo e o site atualiza.
"""

from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------------------
# DADOS DO PERSONAL TRAINER — edite aqui
# ---------------------------------------------------------------------------

WHATSAPP_NUMERO = "5541991646330"    # formato: 55 + DDD + número, só dígitos
DADOS_DE_EXEMPLO = False              # e-mail e whatsapp já são reais

TRAINER = {
    "nome": "Gabriel Anjos Rosa",
    "primeiro_nome": "Gabriel",
    "iniciais": "GA",
    "cidade": "Curitiba, PR",
    "instagram_handle": "gab_anjoss",
    "instagram_url": "https://www.instagram.com/gab_anjoss/",
    "whatsapp_url": f"https://wa.me/{WHATSAPP_NUMERO}",
    "whatsapp_exibicao": "(41) 9 9164-6330",
    "email": "contato@gabrielanjos.com",
    "dados_exemplo": DADOS_DE_EXEMPLO,
    "especialidades": [
        "Emagrecimento",
        "Hipertrofia",
        "Condicionamento",
        "Treino funcional",
        "Consultoria online",
    ],
}

METODO = [
    {
        "titulo": "Avaliação inicial",
        "texto": "Conversa sobre objetivo, rotina, histórico de treino e eventuais "
                 "restrições — presencial ou por chamada de vídeo.",
    },
    {
        "titulo": "Plano personalizado",
        "texto": "Programa de treino montado especificamente pra sua realidade: "
                 "frequência, equipamento disponível e nível técnico.",
    },
    {
        "titulo": "Execução acompanhada",
        "texto": "Feedback de execução, ajustes de carga e suporte direto — em "
                 "treino presencial ou por vídeo/mensagem no plano online.",
    },
    {
        "titulo": "Evolução e reavaliação",
        "texto": "Revisão periódica do plano com base na sua progressão, pra "
                 "garantir que o treino continue funcionando pro seu objetivo.",
    },
]

SERVICOS = [
    {
        "nome": "Consultoria Online",
        "preco": "Valor sob consulta",
        "destaque": False,
        "itens": [
            "Plano de treino personalizado",
            "Ajustes periódicos de carga",
            "Suporte por mensagem",
            "Atende qualquer cidade",
        ],
    },
    {
        "nome": "Presencial Curitiba",
        "preco": "Valor sob consulta",
        "destaque": True,
        "itens": [
            "Treino acompanhado ao vivo",
            "Correção de execução em tempo real",
            "Plano personalizado + progressão",
            "Horário combinado com o Gabriel",
        ],
    },
    {
        "nome": "Combo On + Off",
        "preco": "Valor sob consulta",
        "destaque": False,
        "itens": [
            "Treinos presenciais no mês",
            "Plano online nos demais dias",
            "Acompanhamento contínuo",
            "Ideal pra rotina mista",
        ],
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        trainer=TRAINER,
        metodo=METODO,
        servicos=SERVICOS,
        ano_atual=date.today().year,
    )


if __name__ == "__main__":
    app.run(debug=True)
