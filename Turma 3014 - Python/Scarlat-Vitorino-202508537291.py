from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1 style='color:red;font-size:50px;'>Olá, Mundo!</h1><img src='/static/imagem.png.png' style='max-width:200px;'>"

if __name__ == "__main__":
    app.run(debug=True)
    
    