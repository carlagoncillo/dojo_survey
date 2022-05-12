from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def counter():
    return render_template('index.html')
    
@app.route('/enter', methods=['POST'])
def results():
    session['name'] =  request.form['name']
    session['location'] =  request.form['location']
    session['language'] =  request.form['language']
    session['comment'] =  request.form['comment']
    return redirect('/submission')

@app.route('/submission')
def submission():
    return render_template('submission.html', dog=session['name'], cat=session['location'])

if __name__=="__main__": 
    app.run(debug=True)