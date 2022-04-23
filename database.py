import pymysql

myDB = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="jp"
)

cursor = myDB.cursor()


def insertParticipant(email, firstName, lastName, phone, passw, date, role):
    result = cursor.execute(
        "INSERT INTO user(email, fname, lname, phone, pass, dob, role) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (email, firstName, lastName, phone, passw, date, role))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def validate(em, pa):
    cursor.execute("SELECT * FROM user WHERE email= %s AND pass = %s ", (em, pa))
    result = cursor.fetchall()
    myDB.commit()
    if len(result) > 0:
        return result
    else:
        return False


def jobPost(title, location, exp, ddate, sf, st, desig, statm, quiz, desc, user):
    result = cursor.execute(
        "INSERT INTO jobs(Jtitle, Jlocation, Jexperience, Deadline_Date, Salayfrom, Salaryto, Designation, Statement, "
        "Quiz, Description,Posted_By) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (title, location, exp, ddate, sf, st, desig, statm, quiz, desc, user))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def ProfilePost(name, email, add, type, phone, mobile, zip, term):
    result = cursor.execute(
        "INSERT INTO comp_p(Comp_Name, Comp_Email, Comp_Address, Comp_Type, Comp_Phone, Comp_Mobile, ZipCode, "
        "Terms) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (name, email, add, type, phone, mobile, zip, term))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def ProfilePost(name, email, add, type, phone, mobile, zip, term):
    result = cursor.execute(
        "INSERT INTO comp_p(Comp_Name, Comp_Email, Comp_Address, Comp_Type, Comp_Phone, Comp_Mobile, ZipCode, "
        "Terms) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (name, email, add, type, phone, mobile, zip, term))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def UProfilePost(city, UID, gender, Prof_Info, Experience, Term):
    result = cursor.execute(
        "INSERT INTO user_p(city, UID, gender, Prof_Info, Experience, Term) VALUES (%s, %s, %s, %s, %s, %s)",
        (city, UID, gender, Prof_Info, Experience, Term))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def Posted_Jobs(user):
    cursor.execute("select * from jobs WHERE Posted_By = %s", user)
    result = cursor.fetchall()
    myDB.commit()
    if result:
        return result
    else:
        return False


def getJobs():
    cursor.execute("select * from jobs")
    result = cursor.fetchall()
    myDB.commit()
    if result:
        return result
    else:
        return False


def addskill(id, skill):
    result = cursor.execute("UPDATE user_p SET Skill_Recommended = %s WHERE UID = %s", (skill, id))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def validateprofile(user):
    cursor.execute("select * from user_p WHERE UID = %s AND Skill_Recommended is NOT NULL", user)
    result = cursor.fetchone()
    myDB.commit()
    if result:
        return True
    else:
        return False


def jdetails(id):
    cursor.execute("SELECT * FROM jobs WHERE JID = %s", id)
    result = cursor.fetchall()
    myDB.commit()
    if len(result) > 0:
        return result
    else:
        return False


def jdetailsuser(user):
    cursor.execute("SELECT * FROM jobs WHERE Posted_By = %s", user)
    result = cursor.fetchall()
    myDB.commit()
    if len(result) > 0:
        return result
    else:
        return False


def insertJA(uid, jid, fname, email, title, desc, QS):
    result = cursor.execute("INSERT INTO jobs_applied(UID, JID, Fname, email, Job_title, Description, Quiz_Score) "
                            "VALUES (%s, %s, %s, %s,%s,%s,%s)",
                            (uid, jid, fname, email, title, desc, QS))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def getPc(id):
    cursor.execute("SELECT Profile_Completion From Job WHERE ID = %s", (id))
    result = cursor.fetchone()
    myDB.commit()
    if result > 0:
        return True
    else:
        return False


def validateJA(UID, JID):
    cursor.execute("SELECT * From jobs_applied WHERE UID = %s AND JID = %s", (UID, JID))
    result = cursor.fetchone()
    myDB.commit()
    if result is None:
        return False
    elif len(result) > 0:
        return True
    else:
        return False


def getJA(UID):
    cursor.execute("SELECT * From jobs_applied WHERE UID = %s", (UID))
    result = cursor.fetchall()
    myDB.commit()
    if result is None:
        return False
    if len(result) > 0:
        return result
    else:
        return False


def updateprofile(UID, fname, lname, email):
    result = cursor.execute("UPDATE user SET fname = %s, lname = %s, email = %s WHERE ID = %s",
                            (fname, lname, email, UID))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False


def updatepass(UID, passw):
    result = cursor.execute("UPDATE user SET pass = %s WHERE ID = %s",
                            (passw, UID))
    myDB.commit()
    if result == 1:
        return True
    else:
        return False