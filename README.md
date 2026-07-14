# Site do Gabriel Anjos Rosa — Personal Trainer (Flask)

## Como rodar

```bash
pip install -r requirements.txt
python app.py
```

Depois abra **http://127.0.0.1:5000** no navegador.

## Estrutura

```
app.py                  → dados do site (contato, preços, depoimentos) + rota Flask
templates/index.html    → template HTML (Jinja2)
static/css/style.css    → todo o visual (cores, fontes, layout)
requirements.txt        → dependência (Flask)
```

## O que editar antes de publicar

Tudo fica no topo do `app.py`:

- `WHATSAPP_NUMERO` — número real (formato `55` + DDD + número, só dígitos)
- `TRAINER["email"]` — e-mail real
- `TRAINER["whatsapp_exibicao"]` — número formatado que aparece na tela
- `SERVICOS` — preços reais dos 3 planos
- `DEPOIMENTOS` — depoimentos reais de alunos
- Quando tudo estiver atualizado, mude `DADOS_DE_EXEMPLO = False`
  (isso remove o aviso de "*dados de exemplo" do rodapé)

Foto real: por enquanto a seção "Sobre" usa um monograma "GA" como espaço reservado.
Para trocar por uma foto, adicione a imagem em `static/img/` e ajuste o bloco
`.avatar-frame` em `templates/index.html`.

## Publicar online

Qualquer serviço que rode Flask funciona (Render, Railway, PythonAnywhere, etc.).
Em produção, troque `app.run(debug=True)` por um servidor WSGI como `gunicorn`:

```bash
pip install gunicorn
gunicorn app:app
```
