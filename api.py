from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    url = 'https://rickandmortyapi.com/api/character/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Extraer solo los campos 'type', 'species' e 'image' para todos los personajes
        characters = [{'name': character['name'], 'type': character['type'],
                       'species': character['species'], 'image': character['image']} for character in data['results']]
    else:
        characters = []

    return render_template('index.html', characters=characters)


if __name__ == '__main__':
    app.run(debug=True)
