# modelo_nutri.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# ==============================
# 1. Carregar os dados
# ==============================
# Substitua 'dados_nutri.csv' pelo nome do seu arquivo com os dados reais
# Certifique-se de que ele tem colunas de atributos e uma coluna de target (classe/resultado)

df = pd.read_csv('dados_nutri.csv')  # ou pd.read_excel('dados_nutri.xlsx')

# Exemplo:
# df.head()
# | idade | peso | altura | atividade | suplemento | objetivo |
# | 25    | 70   | 1.75   | moderada  | 1          | 0        |

# ==============================
# 2. Separar features e target
# ==============================
# Suponha que a última coluna seja a target (classe)
X = df.iloc[:, :-1]  # todas as colunas, menos a última
y = df.iloc[:, -1]   # última coluna

# ==============================
# 3. Dividir em treino e teste
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 4. Treinar o modelo
# ==============================
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# ==============================
# 5. Avaliar o modelo
# ==============================
y_pred = modelo.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Acurácia no conjunto de teste: {acc:.2f}")

# ==============================
# 6. Salvar o modelo em arquivo .pkl
# ==============================
joblib.dump(modelo, 'modelo_nutri.pkl')
print("Modelo salvo com sucesso em 'modelo_nutri.pkl'!")

# ==============================
# 7. Como carregar o modelo depois
# ==============================
# modelo_carregado = joblib.load('modelo_nutri.pkl')
# novos_resultados = modelo_carregado.predict(novos_dados)
