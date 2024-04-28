import os
import pandas as pd
import whisper
from spleeter.separator import Separator
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/separar')
def separarPista(nombreMusica):
 if __name__ == '__main__':

  musica = "https://github.com/joshDev27/APIPROC/firework.mp3"#ubicacion de la pista que queremos separar
  separator = Separator("spleeter:2stems")
  separator.separate_to_file(musica,"https://github.com/joshDev27/APIPROC/")#ubicacion donde se guardara los 2stesms
  return"pitas separadas"
 
if __name__ == '__main__':
    app.run(debug=True)
