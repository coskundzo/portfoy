# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


# Geri bildirim formu işleme
@app.route('/feedback', methods=['POST'])
def feedback():
    email = request.form.get('email')
    text = request.form.get('text')
    
    # Burada geri bildirim verilerini işleyebilirsiniz
    # Örneğin, veritabanına kaydetmek veya e-posta göndermek
    print(f"Geri bildirim alındı:")
    print(f"E-mail: {email}")
    print(f"Mesaj: {text}")
    
    # Ana sayfaya geri dön ve başarı mesajı göster
    return render_template('index.html', feedback_success=True)


if __name__ == "__main__":
    app.run(debug=True)
