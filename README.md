# 🐼 Learn Pandas

Este repositório foi criado para **aprender e praticar os principais conceitos da biblioteca [pandas](https://pandas.pydata.org/)** em Python — desde a leitura de arquivos CSV até a manipulação, filtragem, agrupamento e exportação de dados.

As operações incluem:

- Leitura de arquivos CSV;
- Manipulação de colunas e índices;
- Criação de novas colunas com cálculos;
- Agrupamentos e tabelas dinâmicas;
- Filtragem de dados;
- Exportação de resultados modificados.

> 🇧🇷 Comentários no código estão escritos em **português e inglês**, facilitando o entendimento técnico e o aprendizado bilíngue.

---

## 📂 Estrutura do Projeto

```
learn-pandas/
├── .venv/                        # Ambiente virtual gerenciado pelo Poetry
├── data/
│   ├── origin/
│   │   └── dados.csv             # Arquivo de origem (dados de exemplo)
│   └── to_export/
│       └── dados_modificado.csv  # Arquivo gerado após as transformações
├── learn_pandas/
│   ├── __init__.py
│   └── index.py
├── tests/
│   └── __init__.py
├── poetry.lock                   # Controle de dependências
├── pyproject.toml                # Configuração do Poetry
├── README.md                     # Documentação do projeto
└── main.py                       # Script principal com exemplos e explicações
```

---

## ⚙️ Instalação

1. **Clone este repositório**

   ```bash
   git clone https://github.com/seu-usuario/learn-pandas.git
   cd learn-pandas

2. **Crie o ambiente virtual**

   ```bash
   poetry env use python

3. **Instale as dependências com Poetry**

   ```bash
   poetry install

4. **Execute o script**

   ```bash
   poetry run python learn_pandas\\index.py
   
   
