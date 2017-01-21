from flask import Flask, render_template, request
from forms import NameForm
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm(request.form)
    result_string = 'Fill out the form'
    if request.method == 'POST' and form.validate():
        result_string = 'hi ' + form.name.data
    return render_template('index.html', my_string=result_string, form=form)

app.secret_key = "Little bobby drop tables"

if __name__ == "__main__":
    app.run()
