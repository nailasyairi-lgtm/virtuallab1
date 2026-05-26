from flask import Flask, render_template

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Halaman simulasi menimbang
@app.route('/timbang')
def timbang():
    return render_template('timbang.html')

# Halaman simulasi titrasi
@app.route('/titrasi')
def titrasi():
    return render_template('titrasi.html')

if __name__ == '__main__':
    app.run(debug=True)
