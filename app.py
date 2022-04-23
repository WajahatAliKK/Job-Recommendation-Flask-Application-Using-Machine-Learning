from flask import Flask, redirect, url_for, render_template, request, flash
from database import *
import re, pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
user = []
df = pd.read_csv("Questions.csv")
df = df.sample(10)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/forgetpassword")
def forgetpassword():
    return render_template("forgetpassword.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        passw = request.form['pass']
        date = request.form['date']
        role = request.form['optradio']
        insertParticipant(email, fname, lname, phone, passw, date, role)

    return render_template("login.html")


@app.route("/index", methods=['GET', 'POST'])
def index():
    global user
    global jobs
    if request.method == 'POST':
        if 'OS_Percentage' in request.form:
            df = [request.form['OS_Percentage'], request.form['Algo_Percentage'],
                  request.form['Programming_Percentage'], request.form['SE_Percentage'], request.form['CN_Percentage'],
                  request.form['ES_Percentage'], request.form['CA_Percentage'], request.form['Math_Percentage'],
                  request.form['CS_Percentage'], request.form['LQ_Rating'], request.form['CS_Rating'],
                  request.form['RW_Skills'], request.form['TT'], request.form['SLC'], request.form['EC'],
                  request.form['MCS'], request.form['Introvert']]
            for i in range(0, len(df)):
                df[i] = int(df[i])
            jobs = getJobs()
            df = np.reshape(df, (-1, 17))
            loaded_model = pickle.load(open('RFC.sav', 'rb'))
            predicted = loaded_model.predict(df)
            predicted = str(predicted)
            addskill(user[0][0], predicted)
            form = validateprofile(user[0][0])
            return render_template("user-panel/index.html", job=jobs, user=user, form=form)

        elif 'jtitle' in request.form:
            raw_html = request.form['Desc']
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', raw_html)
            print(cleantext)
            jobPost(request.form['jtitle'], request.form['jloc'], request.form['exp'], request.form['ddate'],
                    request.form['sf'], request.form['st'], request.form['Designation'], request.form['Statement'],
                    request.form['Quiz'], cleantext, user[0][1])
            Pjobs = Posted_Jobs(user[0][1])
            print(Pjobs)
            if Pjobs:
                return render_template("index.html", job=Pjobs, user=user)
            else:
                return render_template("index.html", user=user)
        else:
            email = request.form['email']
            passw = request.form['pass']
            user = validate(email, passw)
            if user:
                Pjobs = Posted_Jobs(user[0][1])
                jobs = getJobs()
                if user[0][7] == "company":
                    if Pjobs:
                        return render_template("index.html", job=Pjobs, user=user)
                    else:
                        return render_template("index.html", user=user)
                else:
                    form = validateprofile(user[0][0])
                    return render_template("user-panel/index.html", job=jobs, user=user, form=form)
            else:
                flash('Invalid Credentials')
                return redirect(url_for("home"))
    else:
        if user:
            if user[0][7] == "company":
                jobs = Posted_Jobs(user[0][1])
                return render_template("index.html", job=jobs, user=user)
            else:
                jobs = getJobs()
                form = validateprofile(user[0][0])
                return render_template("user-panel/index.html", job=jobs, user=user, form=form)
        else:
            return render_template("index.html")


@app.route("/c_signup", methods=['GET', 'POST'])
def c_signup():
    if request.method == 'POST':
        global email
        email = request.form['email']
    return render_template("c_signup.html")


@app.route("/JPost")
def JPost():
    if user:
        return render_template("Jobs_Posts.html", user=user)
    return render_template("Jobs_posts.html")


@app.route("/user_profile")
def user_profile():
    if user[0][7] == 'company':
        job = jdetailsuser(user[0][1])
        return render_template("user-profile.html", jobs=job, user=user)
    else:
        return render_template("user-panel/user-profile.html")


@app.route("/jobs_details/<id>/<index>/", methods=['GET', 'POST'])
def jobs_details(id, index):
    if index == "admin":
        data = jdetails(id)
        print(data)
        return render_template("jobs_details.html", job=data, user=user)
    else:
        JA = validateJA(user[0][0], id)
        data = jdetails(id)
        return render_template("user-panel/jobs_details.html", job=data, user=user, df=df.values, JA=JA)


@app.route("/jobs_apply/<id>", methods=['POST'])
def jobs_apply(id):
    if request.method == 'POST':
        count = 0
        for index, row in df.iterrows():
            if row['Correct'] == request.form[str(row['Sr.'])]:
                count = count + 1
    data = jdetails(id)
    return render_template("user-panel/jobs_apply.html", user=user, jid=id, qs=count, job=data)


@app.route("/JD/<id>/<score>/", methods=['GET', 'POST'])
def JD(id, score):
    if request.method == 'POST':
        title = request.form['title']
        fname = request.form['fname']
        email = request.form['email']
        desc = request.form['desc']
        insertJA(user[0][0], id, fname, email, title, desc, score)
    jobs = getJobs()
    form = validateprofile(user[0][0])
    return render_template("user-panel/index.html", job=jobs, user=user, form=form)


@app.route("/Jobs_lists", methods=['GET', 'POST'])
def Jobs_lists():
    return render_template("jobs_lists.html")


@app.route("/Jobs_Posts", methods=['GET', 'POST'])
def Jobs_Posts():
    if user:
        return render_template("Jobs_Posts.html", user=user)
    return render_template("Jobs_posts.html")


@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        ProfilePost(request.form['name'], request.form['email'], request.form['address'], request.form['BussinessType'],
                    request.form['phoneNumber'], request.form['mobile'], request.form['zipcode'],
                    request.form['acceptTerms'])
        return redirect(url_for("profile"))
    return render_template("profile.html")


@app.route("/survey_form")
def survey_form():
    return render_template("user-panel/survey_form.html")


@app.route("/jobs_applied")
def jobs_applied():
    jobs = getJA(user[0][0])
    return render_template("user-panel/jobs_applied.html", jobs=jobs)


@app.route("/job_list")
def jobs_list():
    jobs = getJobs()
    return render_template("user-panel/jobs_list.html", job=jobs)


@app.route("/user-profile")
def userprofile():
    return render_template("user-panel/user-profile.html")


@app.route("/Uprofile", methods=['GET', 'POST'])
def Uprofile():
    if request.method == 'POST':
        print(user[0][0])
        UProfilePost(request.form['city'], user[0][0], request.form['Gender'], request.form['Professional_Information'],
                     request.form['Fresh'], request.form['acceptTerms'])
        return redirect(url_for("Uprofile"))
    return render_template("user-panel/profile.html")


@app.route("/edit_profile")
def edit_profile():
    if user[0][7] == 'company':
        jobs = getJobs()
        return render_template("edit-profile.html", jobs=jobs, user=user)
    else:
        return render_template("user-panel/edit-profile.html")


@app.route("/Update_Profile", methods=['POST', 'GET'])
def Update_Profile():
    if user[0][7] == 'company':
        if 'email' in request.form:
            email = request.form['email']
            fname = request.form['fname']
            lname = request.form['lname']
            updateprofile(user[0][0], fname, lname, email)
        else:
            passw = request.form['pass']
            updatepass(user[0][0],passw)
        jobs = Posted_Jobs(user[0][1])
        return render_template("index.html", job=jobs, user=user)
    else:
        if 'email' in request.form:
            email = request.form['email']
            fname = request.form['fname']
            lname = request.form['lname']
            updateprofile(user[0][0], fname, lname, email)
        else:
            passw = request.form['pass']
            updatepass(user[0][0], passw)
        jobs = getJobs()
        form = validateprofile(user[0][0])
        return render_template("user-panel/index.html", job=jobs, user=user, form=form)


if __name__ == "__main__":
    app.run()
