from flask import Flask, jsonify
import pandas as pd

# Ler a planilha de dados
data = {
    "number": [1, 2, 3, 4, 5],
    "name": ["Mahesh", "Alex", "David", "John", "Chris"],
    "age": [25, 26, 27, 28, 29],
    "city": ["Bangalore", "London", "San Francisco", "Toronto", "Paris"],
    "country": ["India", "UK", "USA", "Canada", "France"]
}
df = pd.DataFrame(data)

# Inicializar o aplicativo Flask
app = Flask(__name__)

# Definir rota para retornar a planilha de dados
@app.route("/index")
def get_data():
    # Converter DataFrame para formato JSON e retornar
    return jsonify(df.to_dict(orient="records"))

# Executar o aplicativo Flask
if __name__ == "__main__":
    app.run(port=5000)
