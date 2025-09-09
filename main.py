from flask import Flask
from controllers.uni_controller import uni_bp

app = Flask(__name__)

# Registrar el blueprint de bandas
app.register_blueprint(uni_bp)

if __name__ == "__main__":
    app.run(debug=True)
