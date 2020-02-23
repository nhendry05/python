from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/results', methods = ['POST'])
def results():
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    campusOnline_from_form = request.form['campusOnline']
    complete_from_form = request.form['complete']
    comment_from_form = request.form['comment']
    return render_template("results.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, campusOnline_on_template=campusOnline_from_form, complete_on_template =complete_from_form, comment_on_template=comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)