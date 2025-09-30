from flask import Flask, render_template
from forms import Contact_forms

app = Flask(__name__)
app.secret_key = "development key"

@app.route('/', methods=['GET','POST']:
  def contact():
    form = ContactForm()
    if form.validate_on_submit():
      return render_template('idk.html')
      return render_template('idk.html', form=form)

@app.route('/success', methods=['GET','POST'])
 def success():
   return render_template('page.html')

app.run(host="0.0.0.0", port="8080")

    
    
