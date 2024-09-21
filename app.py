# Importação
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eccomerce-python.db"

db = SQLAlchemy(app)

# Modelagem

# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route("/")
def hello_world():
  return "Hello World"

if __name__ == "__main__":
  app.run(debug=True)