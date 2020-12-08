# Team KOCY -- William Yin, Liam Kronman, Jason Chan, Stella Oh
# SoftDev
# K14 -- Form and Function
# 2020-12-08


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template('login.html')


@app.route("/auth")
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    # Initialize username to "Nobody" in case the user does not submit a username
    username = "Nobody"
    # This handles the case where the user goes to the /auth route by typing it directly into their url
    try:
        # Don't change the value of username if the user did not submit anything
        if request.args["username"]:
            username = request.args["username"]
    except:
        # Do nothing if the user requested the page directly
        pass
    return render_template("response.html", username=username, method=request.method)



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
