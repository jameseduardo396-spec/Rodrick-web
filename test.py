from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def verifier_age():
    age_url = request.args.get('age')
    if age_url is None:
        return "Veuillez ajouter votre âge à l'adresse (ex: ?age=20)"
    try:
        age = int(age_url)
        if age >= 18:
            return "Accès autorisé ! Bienvenue"
        else:
            return "Désolé, tu es trop jeune."
    except:
        return "L'âge doit être un nombre."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
