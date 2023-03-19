from flask import Flask,render_template,request
import re
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/find",methods=["POST","GET"])

def find():
    l=[i for i in request.form.values()]
    regexp=l[0]
    test_string=l[1]
    k=re.findall(regexp,test_string)
    if len(k)==0:
        return render_template("display.html",msg="NO matching Found")
    return render_template("display.html",k=k)

if __name__=='__main__':
    app.run(debug=True)