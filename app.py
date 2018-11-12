from flask import Flask, render_template
from graduate_outcomes import get_total_dropped_out

app = Flask(__name__)
name = str(get_total_dropped_out())
print(name)

@app.route('/prison')
def prison_data():
    return render_template("show.html")

@app.route('/education')
def education_data():
    return render_template("show.html")

if __name__ == '__main__':
    app.run(debug=True)