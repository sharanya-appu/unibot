import math
import re
from collections import Counter

import pymysql as pymysql
from flask import *
from chatbot.dbcon import *

from werkzeug.utils import secure_filename

app = Flask(__name__)
con = pymysql.Connect(host='localhost', port=3306, user='root', password='root', db='chatbot')
cmd = con.cursor()
WORD = re.compile(r'\w+')

@app.route("/stud_register",methods=['post'])
def stud_register() :
    fname=request.form['fname']
    last_name=request.form['lname']
    dob=request.form['dob']
    place=request.form['place']
    dist=request.form['dist']
    pin=request.form['pin']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    college=request.form['college']
    course=request.form['course']
    regno=request.form['regno']
    sem=request.form['sem']
    uname=request.form['uname']
    password=request.form['password']
    qrry = "insert into login(lname,password,type) values(%s,%s,'pending')"
    value=(uname,password)
    id=iud(qrry, value)
    qry="insert into student(first_name,last_name,dob,place,district,pin,gender,phone,email,clg_id,course_id,regno,sem) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vals = (fname,last_name,dob,place,dist,pin,gender,phone,email,college,course,regno,sem)
    s=iud(qry, vals)
    return jsonify({'result':"success"})


@app.route("/login_click",methods=['post'])
def login_click() :
    lname=request.form['uname']
    password=request.form['pass']
    qry="select * from login where lname=%s and password=%s"
    vals=(lname,password)
    res= display(qry,vals)
    if res is None:
        return jsonify({'result':"Invalid"})
    elif(res[3]=='student'):
        return jsonify({'result':str(res[0])})


@app.route("/college",methods=['post'])
def college() :
    qry="select clg_id,clg_name from college"
    s=select(qry)
    row_headers=['clg_id','clg_name']
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))

    return jsonify(json_data)


@app.route("/course",methods=['post'])
def course() :
    clg=request.form['clgid']
    qry="SELECT college_course.course_id,cname FROM course JOIN college_course ON `college_course`.`course_id`=`course`.`course_id` WHERE college_course.clg_id=%s "
    val=(clg)
    s=select1(qry,val)
    row_headers=['course_id','cname']
    json_data=[]
    for result in s :
        json_data.append(dict(zip(row_headers,result)))

    return jsonify(json_data)

@app.route("/doubt",methods=['post'])
def doubt() :
    msg=request.form['msg']
    lid=request.form['lid']

    print("msg", msg)

    # uid = request.args.get("uid")

    def text_to_vector(text):
        words = WORD.findall(text)
        return Counter(words)

    def get_cosine(vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])
        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    vector1 = text_to_vector(msg)
    # cmd.execute("select question from dataset")
    # s = cmd.fetchall()
    qry="select question from dataset"
    s=select(qry)
    print("s--", s)
    res = []
    for d in s:
        vector2 = text_to_vector(str(d))
        cosine = get_cosine(vector1, vector2)
        # print("cosine",cosine)

        res.append(cosine)

    print("res---", res)

    ss = -1
    cnt = 0
    i = 0
    for s in res:
        if s > 0.3:
            if ss <= float(s):
                cnt = i
                ss = s
        i = i + 1

    print("ss", ss)
    print("cnt", cnt)
    id = 0
    global aa
    if ss != -1:
        print("select * from dataset where qtn_id='" + str(cnt + 1) + "'")
        # cmd.execute("select * from chatbot where id='" + str(cnt + 1) + "'")
        # aa = cmd.fetchone()
        qry="select * from dataset where qtn_id=%s"
        val=(str(cnt+1))
        aa=display(qry,val)
        id = aa[0]

        # print(aa)
        msg = msg.replace("'", " ")
        # cmd.execute("insert into ai_chat values(null,'" + str(uid) + "','" + msg + "','" + aa[2] + "',curdate(),'')")
        # con.commit()

        # cmd.execute("insert into reponse(response,db_id) values()")

        qry = "insert into doubt(doubt,st_id,reply)values(%s,%s,%s)"
        vals = (msg, lid,aa[2])
        s = iud(qry, vals)

        # if aa[2] == 'staff':
        #     res = checkavailability()
        #     ress = res.split('#')
        #
        #     cmd.execute("insert into assign values(null,'" + str(ress[0]) + "','" + str(uid) + "',now())")
        #     con.commit()
        #     return jsonify({'task': " we assigned " + ress[1] + " for you for more enquiries "})

        return jsonify({'task': aa[2]})
    else:
        qry = "insert into doubt(doubt,st_id,reply,date)values(%s,%s,%s,curdate())"
        vals = (msg, lid,  "Sorry i can't get you!!")
        s = iud(qry, vals)
        return jsonify({'task': "Sorry i can't get you!!"})


# @app.route("/response",method=['post'])
# def response() :
#     qry="SELECT response FROM response JOIN doubt ON response.db_id=doubt.dbid "








if __name__ == '__main__':
    app.run(host='192.168.43.30', port=5000)
