from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    password = None

    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_upper = request.form.get('uppercase')
        use_numbers = request.form.get('numbers')
        use_symbols = request.form.get('symbols')

        characters = string.ascii_lowercase
        if use_upper:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)