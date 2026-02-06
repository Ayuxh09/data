from flask import Flask, render_template, request, send_file
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']

    file_exists = os.path.isfile('data.csv')

    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(['Name', 'Email', 'Age'])

        writer.writerow([name, email, age])

    return "✅ Data saved successfully!"

@app.route('/download')
def download():
    return send_file('data.csv', as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
