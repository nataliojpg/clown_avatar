from flask import Flask, render_template, request, send_file
from PIL import Image
import io


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar():
    ojos = request.form.get('ojos')
    ropa = request.form.get('ropa')
    gorro = request.form.get('gorro')
    fondo = request.form.get('fondo')
    boca = request.form.get('boca')

    
    base = Image.open("static/base.png").convert("RGBA")
    ojos_img = Image.open(f"static/ojos/{ojos}.png").convert("RGBA")
    ropa_img = Image.open(f"static/ropa/{ropa}.png").convert("RGBA")
    gorro_img = Image.open(f"static/gorro/{gorro}.png").convert("RGBA")
    fondo_img = Image.open(f"static/fondo/{fondo}.jpg").convert("RGBA")
    boca_img = Image.open(f"static/boca/{boca}.png").convert("RGBA")

    

    combinado = Image.alpha_composite(fondo_img, base)
    combinado = Image.alpha_composite(combinado, ojos_img)
    combinado = Image.alpha_composite(combinado, ropa_img)
    combinado = Image.alpha_composite(combinado, gorro_img)
    combinado = Image.alpha_composite(combinado, boca_img)



    img_io = io.BytesIO()
    combinado.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')
