from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/data')
def api_data():
    data = {
        "name": "Flask App",
        "version": "1.0.0",
        "features": ["Home", "About", "API", "Form"]
    }
    return jsonify(data)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('form.html', name=name)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

