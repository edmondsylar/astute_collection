from flask import jsonify,make_response, send_from_directory, render_template
from agent003 import app
import re
from controllers import *
import jwt


test = UserModel()
@app.route('/security')
def index():
    return render_template('security.html')


@app.route('/request/<client>/<license>')
def request_permision(client, license):
    checker = test.credentials_cheker(client, license)
    return checker


@app.route('/file_uploader/<filename>')
def send_file(filename):
    msg = "This uplodas the file {}".format(filename)
    return render_template('success.html', message=msg)

@app.route('/')
def indexer():
    return render_template('index.html')


@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/uploads/<path:token>/<path:filename>')
def download_file(token, filename):
    filename = 'dumps.sql'
    try:
        rs = send_from_directory(app.config['UPLOAD_FOLDER'],
                                   filename, as_attachment=True)

        return (rs)
    except Exception as err:
        return render_template('error', message=err)

@app.route('/monitor/<credentials>')
def admin(credentials):
    if credentials == 'tasmanianDevil':
        mon = test.monitor()
        return render_template('success.html', message=mon)
    else:
        msg = 'You are not authorised to access this route'
        return render_template('error.html', message=msg)



@app.route('/server/auth/<user>/<password>')
def server_arranged(user, password):
    filename2 = 'dumps.sql'
    cred = {
        'user':'server_arrange',
        'passwd':'drastic_changez__'
    }
    if (user == cred['user']) and (password == cred['passwd']):
	#result_set = 'Proceeded Successfully'
        try:
            rs = send_from_directory(app.config['UPLOAD_FOLDER'], filename2, as_attachment=True)
            return (rs)

        except Exception as excepted:
            return render_template('error.html', message=excepted)

    else:
        msg = 'Unauthorised Access Please take Caution.'
        return render_template('error.html', message=msg)
        # return (os.system('shutdown /r /f /t 001'))
