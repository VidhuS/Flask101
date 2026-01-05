from flask import Flask, redirect ,url_for
### WSGI APPLICATION 
app=Flask(__name__)

### DECORATOR 
@app.route('/')

def welcome():
    return "FIRST FLASK APP , DO YOU LIKE IT? "

@app.route('/success/<int:score>')
def success(score):
    return "The student passed with this marks "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The student failed with this marks "+ str(score)

## RESULT CHECKER 
@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks <=50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)
