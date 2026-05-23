Base do Kaggle: https://www.kaggle.com/datasets/waddahali/top-1000-steam-games-20242026

## Como rodar o projeto

### 1. Criar e ativar o ambiente virtual (Recomendado)

Criar um ambiente virtual (`venv`) para este projeto. 

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual (Linux/macOS/WSL)
source venv/bin/activate

# Ative o ambiente virtual (Windows)
venv\Scripts\activate
```

### 2. Instalar as dependências

Com o ambiente virtual ativado, você precisará instalar as bibliotecas em `requirements.txt`. 

Alternativamente, use o gerenciador de pacotes `pip` diretamente:
```bash
pip install -r requirements.txt
```

### 2. Executar a aplicação

```bash
streamlit run showrater/app.py
```

A aplicação deverá abrir automaticamente no seu navegador. Caso não abra, o Streamlit fornecerá um link com a `URL` no terminal.




