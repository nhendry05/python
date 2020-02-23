from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'
@app.route('/')
def visits():
    if 'key_name' in session:
        session['key_name'] = session.get('key_name') + 1
        print('key exists!')
    else:
        session['key_name'] = 1
        print("key 'key_name' does NOT exist")
    return render_template("index.html", key_name_on_template=session['key_name'])

@app.route('/increase_two', methods=['POST'])
def two():
    session['key_name'] = session.get('key_name') + 1
    return redirect("/")

@app.route('/destroy_session', methods=['POST'])
def clear():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)