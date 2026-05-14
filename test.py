from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Le design de ton site (HTML/CSS)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Rodrick-web</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        input { padding: 10px; margin: 10px; border-radius: 5px; border: 1px solid #ccc; }
        button { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .result { margin-top: 20px; font-weight: bold; font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Vérificateur d'âge 🚀</h2>
        <form method="GET">
            <input type="number" name="age" placeholder="Entre ton âge" required>
            <br>
            <button type="submit">Vérifier</button>
        </form>
        
        {% if message %}
            <div class="result">{{ message }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    age_url = request.args.get('age')
    message = None
    
    if age_url:
        try:
            age = int(age_url)
            if age >= 18:
                message = "✅ Accès autorisé ! Bienvenue."
            else:
                message = "❌ Désolé, tu es trop jeune."
        except:
            message = "⚠️ Erreur : Entre un nombre valide."
            
    return render_template_string(HTML_TEMPLATE, message=message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
