from flask import Flask, render_template, request, url_for, redirect
import function, csv

app = Flask(__name__, )

def update():
    with open('database.csv', newline='') as file_in:
        reader = csv.DictReader(file_in)
        table = []
        for row in reader:
            table += [row]
        return table

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html', table=update())


@app.route("/insert", methods=['GET', 'POST'])
def insertlayout():
    if request.method == 'POST':
        name = request.form['name']
        nickname = request.form['nickname']
        age = request.form['age']   
        city = request.form['city']
        comics = request.form['comics']
        function.insert(name, nickname, age, city, comics)
        return redirect("/")
    return render_template("insert.html")


@app.route("/remove", methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        i = request.form['i']
        function.remove(int(i))
        return redirect("/")
    return render_template('remove.html')


@app.route("/alternate", methods=['GET', 'POST'])
def alternate():
    if request.method == 'POST':
        i = request.form['i']
        name = request.form['name']
        nickname = request.form['nickname']
        age = request.form['age']
        city = request.form['city']
        comics = request.form['comics']
        function.alternate(int(i), name, nickname, age, city, comics)
        return redirect("/")
    return render_template('alternate.html')

if __name__ == '__main__':
    app.run(debug=True)
