from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfCircle', methods=['GET', 'POST'])
def area_of_circle():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = 3.14159265359 * radius * radius
    return render_template('area_of_circle.html', area=area)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def area_of_triangle():
    area = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area = 0.5 * base * height
    return render_template('area_of_triangle.html', area=area)

@app.route('/contact')
def contact():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
