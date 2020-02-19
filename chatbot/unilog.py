from flask import *
from werkzeug.utils import secure_filename

from chatbot.dbcon import *

ap=Flask(__name__)
ap.secret_key="qwe"
@ap.route("/")
def main() :
    return render_template("index2.html")
@ap.route("/login")
def login() :
    return render_template("login.html")
@ap.route("/home")
def home() :
    return render_template("adhome.html")
@ap.route("/verifyst")
def verifyst() :
    return render_template("verifyst.html")
@ap.route("/apvdst")
def apvdst() :
    qry = "SELECT st_id,first_name,last_name,college.`clg_name`,regno,`student`.phone,`student`.email,course.`cname` FROM student JOIN `login` ON `login`.`lid`=`student`.`st_id` JOIN `course` ON `course`.`course_id`=`student`.`course_id` JOIN `college` ON `college`.`clg_id`=`student`.`clg_id`  WHERE `login`.`type`='student'"
    vals=select(qry)
    return render_template("appvdstud.html",v=vals)
@ap.route("/newst")
def newst() :
    qry="SELECT st_id,first_name,last_name,college.`clg_name`,regno,`student`.phone,`student`.email,course.`cname` FROM student JOIN `login` ON `login`.`lid`=`student`.`st_id` JOIN `course` ON `course`.`course_id`=`student`.`course_id` JOIN `college` ON `college`.`clg_id`=`student`.`clg_id`  WHERE `login`.`type`='pending'"
    vals=select(qry)
    return render_template("newstud.html",v=vals)
@ap.route("/adapcrs")
def adapcrs() :
    return render_template("adappcorse.html")
@ap.route("/adapvdcrs")
def adapvdcrs() :
    qry="select cname,duration,syllabus from course where course.status='approved'"
    s=select(qry)
    return render_template("adappvdcorse.html",v=s)
@ap.route("/adnewcrs")
def adnewcrs() :
    qry = "select course_id,cname,duration,syllabus from course where course.status='pending'"
    s = select(qry)
    return render_template("adnewcorse.html",v=s)

@ap.route("/adaddep")
def adaddep() :
    return render_template("adaddep.html")
@ap.route("/admngdep")
def admngdep() :
    qry = "SELECT depart_name,cont_no,course.cname FROM department JOIN course ON department.lid=course.dept_id"
    vals=select(qry)
    return render_template("admangdep.html",v=vals)

@ap.route("/admin_dep")
def admin_dep() :

    return render_template("admin_dep.html",)
@ap.route("/adadclg")
def adadclg():
    return render_template("adadclg.html")
# @ap.route("/adassign_crs")
# def adassign_crs():
#     qry="select * from course"
#     vals=select(qry)
#     return render_template("admin_asign_crs.html",v=vals)
@ap.route("/adviewclg")
def adviewclg():
    qry="SELECT clg_name,location,phone,email,course.cname,college_course.fee FROM college JOIN `college_course` ON `college`.`clg_id`=`college_course`.`clg_id` JOIN `course` ON `college_course`.`course_id`=`course`.`course_id`"
    vals=select(qry)
    return render_template("admin_college_view.html",v=vals)


@ap.route("/login_click",methods=['post'])
def login_click() :
    lname=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from login where lname=%s and password=%s"
    vals=(lname,password)
    res= display(qry,vals)
    if res is None:
        return '''<script>
        alert("Wrong password");
        window.location='/'</script>'''
    elif(res[3]=='admin'):
        return '''<script> 
        alert("Successfully login")
        window.location='/home'
        </script>'''
    else :
        session['lid']=res[0]
        return '''<script>
        alert("Successfully login");
        window.location='/dep_home'
        </script>'''
@ap.route("/add_dep",methods=['post'])
def add_dep() :
    dep_name=request.form['textfield']
    contact=request.form['textfield2']
    username=request.form['textfield3']
    password=request.form['textfield4']
    qrry = "insert into login(lname,password,type) values(%s,%s,'dept')"
    qry="insert into department(depart_name,cont_no,lid) values(%s,%s,%s)"
    value=(username,password)
    id=iud(qrry, value)
    vals = (dep_name,contact,id)
    iud(qry, vals)
    return '''<script>
    alert("Saved");
    window.location='/home'
    </script>'''
@ap.route("/approve_std")
def approve_std() :
    sid=request.args.get('id')
    qry="update login set type='student' where login.lid=%s"
    vals=sid
    iud(qry,vals)
    return '''<script>
    alert("Student approved");
    window.location='/newst'</script>'''
@ap.route("/reject_stud")
def reject_stud():
    stid=request.args.get('id')
    qry="delete from login where login.lid=%s"
    qrry="delete from student where student.st_id=%s"
    vals=stid
    iud(qry,vals)
    iud(qrry,vals)
    return '''<script>
    alert("Student can't login");
    window.location='/newst'</script>'''
@ap.route("/approve_course")
def approve_course() :
    sid=request.args.get('id')
    qry="update course set status='approved' where course_id=%s"
    vals=sid
    iud(qry,vals)
    return '''<script>
    alert("Course approved");
    window.location='/adnewcrs'</script>'''
@ap.route("/reject_course")
def reject_course() :
    sid=request.args.get('id')
    qry="delete from course where course_id=%s"
    vals=sid
    iud(qry,vals)
    qrry = "delete from college_course where course_id=%s"
    value=sid
    iud(qrry,value)
    return '''<script>
    alert("Course rejected")
    window.location='/adnewcrs'</script>'''
@ap.route("/add_clg",methods=['post','get'])
def add_clg():
    college=request.form['textfield']
    place=request.form['textfield2']
    phone=request.form['textfield3']
    email=request.form['textfield4']
    qry="insert into college(clg_name,location,phone,email) values(%s,%s,%s,%s)"
    val=(college,place,phone,email)
    id=iud(qry,val)
    session['id']=id
    print(id)
    qry="SELECT * FROM `course`"
    s=select(qry)
    return render_template('admin_asign_crs.html',v=s)
@ap.route("/assign_course",methods=['post'])
def assign_course() :
    btn=request.form['Submit']
    if btn=='ADD':
        sel_course=request.form['select']
        fee=request.form['textfield5']
        id=session['id']
        qry="insert into college_course(clg_id,course_id,fee) values(%s,%s,%s)"
        vals=(id,sel_course,fee)
        iud(qry,vals)
        qry = "SELECT * FROM `course` WHERE `course_id` NOT IN( SELECT `course_id` FROM `college_course` WHERE `clg_id`=%s)" % str(id)
        s = select(qry)
        return render_template('admin_asign_crs.html', v=s)
    else:
        return '''<script>
        alert("Finished");
        window.location='/home'
        </script>'''


@ap.route("/dep_home")
def dep_home() :
    return render_template("dep_home.html")
@ap.route("/dep_crs",methods=['post','get'])
def dep_crs() :
    qry="SELECT * from course where status='approved'"
    vals=select(qry)
    return render_template("dep_course.html",v=vals)
@ap.route("/dep_add_crs",methods=['post','get'])
def dep_add_crs() :
    return render_template("dep_add_course.html")
@ap.route("/dep_add_course",methods=['post'])
def dep_add_course():
    id=str(session['lid'])
    course=request.form['textfield']
    duration=request.form['textfield2']
    syllabus=request.files['file']
    import time
    fn=time.strftime("%Y%m%d_%H%M%S_")+secure_filename(syllabus.filename)
    syllabus.save("static/syllabus/"+fn)
    qry="insert into course(cname,dept_id,duration,syllabus,status) values(%s,%s,%s,%s,'pending')"
    vals=(course,id,duration,fn)
    iud(qry,vals)
    return '''<script>alert("Course details added");
    window.location='/dep_crs'</script>'''
@ap.route("/dep_edit_crs",methods=['post','get'])
def dep_edit_crs() :
    id=request.args.get('id')
    session['id']=id
    print(id,"------------------")
    qry="select * from course where course_id=%s"
    val=(id)
    s=display(qry,val)
    return render_template("dep_edit_course.html",v=s)
@ap.route("/dep_edit_course",methods=['post','get'])
def dep_edit_course() :
    id=str(session['id'])
    course=request.form['textfield']
    duration=request.form['textfield2']
    syllabus=request.files['file']
    import time
    fn=time.strftime("%Y%m%d_%H%M%S_")+secure_filename(syllabus.filename)
    syllabus.save("static/syllabus/"+fn)
    qry="update course set cname=%s,duration=%s,syllabus=%s where course_id=%s"
    val=(course,duration,fn,id)
    iud(qry,val)
    return '''<script>alert("Successfully edited"); window.location='/dep_crs'</script>'''
@ap.route("/dep_delete_course",methods=['post','get'])
def dep_delete_course() :
    id=request.args.get('id')
    qry="delete from course where course_id=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("Successfully deleted"); window.location='/dep_crs'</script>'''


@ap.route("/dep_noti")
def dep_noti():
    qry = "SELECT `notification`.`not_id`,`notification`.`notification`,`notification`.`date`,`course`.`cname` FROM `notification`JOIN `course`ON `notification`.`course_id`= `course`.`course_id`"
    vals = select(qry)
    return render_template("dep_notification.html",v=vals)
@ap.route("/dep_add_noti",methods=['post','get'])
def dep_add_noti() :
    id=str(session['lid'])
    qry="SELECT course_id,course.cname FROM course where course.dept_id=%s"
    vals=(id,)
    s=select1(qry,vals)
    return render_template("dep_add_notification.html",v=s)
@ap.route("/dep_add_notification",methods=['post'])
def dep_add_notification() :
    notification=request.form['textarea']
    course=request.form['select']
    qry="insert into notification(notification,date,course_id) values(%s,curdate(),%s)"
    val=(notification,course)
    iud(qry,val)
    return '''<script>alert("Successfully Added"); window.location='/dep_noti'</script>'''
@ap.route("/dep_delete_notification",methods=['post','get'])
def dep_delete_notification() :
    id=request.args.get('id')
    qry="delete from notification where not_id=%s"
    val=(id)
    iud(qry,val)
    return '''<script>alert("Successfully Deleted"); window.location='/dep_noti'</script>'''


@ap.route("/dep_exam",methods=['post','get'])
def dep_exam():
    qry="select exam.exid,exam.exam_noti,course.cname,exam.date,exam.time_table from exam join course on exam.course_id=course.course_id"
    val=select(qry)
    return render_template("dep_exam.html",v=val)
@ap.route("/dep_add_exam",methods=['post','get'])
def dep_add_exam() :
    id = str(session['lid'])
    qry = "SELECT course_id,course.cname FROM course where course.dept_id=%s"
    vals = (id)
    s = select1(qry, vals)
    return render_template("dep_add_exam.html",v=s)
@ap.route("/dep_add_exam_details",methods=['post','get'])
def dep_add_exam_details() :
    exam=request.form['textarea']
    course=request.form['select']
    time_table=request.files['file']
    import time
    fn=time.strftime("%Y%m%d_%H%M%S_")+secure_filename(time_table.filename)
    time_table.save("static/time_table/"+fn)
    qry="insert into exam(exam_noti,date,course_id,time_table) values(%s,curdate(),%s,%s)"
    vals=(exam,course,fn)
    iud(qry,vals)
    return '''<script>alert("Successfully Added"); window.location='/dep_exam'</script>'''
@ap.route("/dep_delete_exam",methods=['post','get'])
def dep_delete_exam() :
    ex_id=request.args.get('id')
    qry="delete from exam where exid=%s"
    val=(ex_id)
    iud(qry,val)
    return '''<script>alert("Successfully Deleted"); window.location='/dep_exam'</script>'''


@ap.route("/dep_result",methods=['post','get'])
def dep_result() :
    qry="SELECT * FROM exam"
    s=select(qry)
    return render_template("dep_add_result.html",v=s)
@ap.route("/dep_add_results",methods=['post'])
def dep_add_results() :
    regno=request.form['textfield']
    exam=request.form['select']
    result=request.files['file']
    import time
    fn = time.strftime("%Y%m%d_%H%M%S_") + secure_filename(result.filename)
    result.save("static/result/"+fn)
    qry="insert into result(reg_no,exid,stresult) values(%s,%s,%s)"
    val=(regno,exam,fn)
    iud(qry,val)
    return '''<script>alert("Successfully Added"); window.location='/dep_result'</script>'''

@ap.route("/dep_changepass",methods=['post','get'])
def dep_changepass() :
    return render_template("dep_changepass.html")
@ap.route("/dep_change_password",methods=['post'])
def dep_change_password():
    uname=request.form['textfield']
    current_pass=request.form['textfield2']
    new_pass=request.form['textfield3']
    confirm_pass=request.form['textfield4']
    if new_pass==confirm_pass :
        qry="update login set password=%s where password=%s and lname=%s "
        val=(new_pass,current_pass,uname)
        iud(qry,val)
        return '''<script>alert("Password successfully changed");window.location='/dep_home'</script>'''
    else :
        return '''<script>alert("Password Mismatch");window.location='/dep_changepass'</script>'''

@ap.route("/logout")
def logout() :
    return render_template("/login.html")


if(__name__=="__main__") :
    ap.run(debug=True)
