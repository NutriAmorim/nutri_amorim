from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Carrega os dados (use seus dados reais depois)
data = load_iris()
X, y = data.data, data.target

# Treina o modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X, y)

# Salva o modelo em um arquivo .pkl
joblib.dump(modelo, 'modelo_nutri.pkl')
print("Modelo salvo com sucesso!")
