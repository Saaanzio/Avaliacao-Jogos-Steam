# Como rodar o projeto
1. Criar e ativar o ambiente virtual (Recomendado)
Criar um ambiente virtual (venv) para este projeto.

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Linux/macOS/WSL)
source venv/bin/activate

# Ative o ambiente virtual (Windows)
venv\Scripts\activate
2. Instalar as dependências
Com o ambiente virtual ativado, você precisará instalar as bibliotecas em requirements.txt.

pip install -r requirements.txt
2. Executar a aplicação
Para rodar a aplicação localmente e abrir a interface web, execute:

streamlit run Home.py
