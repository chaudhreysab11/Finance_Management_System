from flask import Flask,flash, render_template, request,redirect,session,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "finance"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345"
app.config["MYSQL_DB"] = "NamalFinance"

mysql = MySQL(app)


@app.route("/",methods=['GET','POST'])
def index():
    cur = mysql.connection.cursor()
    if request.method=="POST":
        login_details = request.form
        username = login_details['name']
        password = login_details['password']
        cur.execute("SELECT u_id,u_name,u_class FROM Users where (u_name=%s and u_password=%s)",(username,password))
        user = cur.fetchone()
        if user:
            if user[2]=='Staff':
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for("dashboardstaff"))
            elif user[2]=='Faculty':
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for("dashboardfaculty"))
            elif user[2]=='Student':
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for("dashboardstd"))
            elif user[2]=='Employee':
                session['loggedin'] = True
                session['id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for("dashboardemp"))
            
        else:
            flash("Username or password incorrect.") 
    return render_template('Login.html')

@app.route('/dashboardstaff')
def dashboardstaff():
    cur = mysql.connection.cursor()
    if session['loggedin'] == True:
        cur.execute("SELECT * FROM Staff where (u_id=%s)",(session['id'],))
        stf_detail = cur.fetchone()
        stf_id = stf_detail[0]
        stf_name = stf_detail[1]
        stf_desg= stf_detail[3]
        stf_email = stf_detail[2]
        stf_sal = stf_detail[4]
        cur.execute("SELECT * FROM Expenses")
        exp_detail = cur.fetchone()
        elec_exp = exp_detail[0]
        eobi_exp = exp_detail[1]
        umrah_exp = exp_detail[2]
        rent_exp = exp_detail[3]
        mess_exp = exp_detail[4]
        lp_exp = exp_detail[5]
        income_tax = exp_detail[6]
        care_rent = exp_detail[7]
        tot_exp = elec_exp+eobi_exp+umrah_exp+rent_exp+mess_exp+lp_exp+income_tax+care_rent
        salary_tot = stf_sal-tot_exp
        return render_template('DashboardStaff.html',stfId=stf_id,stfName=stf_name,stfDesg=stf_desg,stfEmail=stf_email,salary=stf_sal,
                                elecExp=elec_exp,eobiExp=eobi_exp,umrahExp=umrah_exp,rentExp=rent_exp,messExp=mess_exp,lpExp=lp_exp,
                                incomeTax=income_tax,careRent=care_rent,totalExp=tot_exp,salaryTot=salary_tot)
    else:
       session.pop('loggedin', None) 
       return redirect(url_for('index'))

@app.route('/dashboardstd')
def dashboardstd():
    cur = mysql.connection.cursor()
    if session['loggedin'] == True:
        cur.execute("SELECT * FROM Student where (u_id=%s)",(session['id'],))
        std_detail = cur.fetchone()
        std_id = std_detail[0]
        std_name = std_detail[1]
        std_dept= std_detail[3]
        std_email = std_detail[2]
        std_gender = std_detail[4]
        std_hflag = std_detail[5]
        std_waiver = std_detail[6]
        std_previous = std_detail[7]

        cur.execute("SELECT * FROM Fees")
        fee_detail = cur.fetchone()
        tuition_fee = fee_detail[0]
        hostel_fee = fee_detail[1]
        lab_exam_fee = fee_detail[2]
        if  std_hflag == True:
            if std_gender == 'F':
                hostel_waiver = fee_detail[1]
            else:
                hostel_waiver = 0
        else:
            hostel_fee=0
            hostel_waiver = 0
        tot_tuition_fee = tuition_fee*4
        tot_le_fee = lab_exam_fee*2
        tot_hostel_fee = hostel_fee*2
        tot_fee_even = tuition_fee
        tot_fee_odd = tuition_fee+hostel_fee+lab_exam_fee
        grand_tot = (tot_fee_even*2) + (tot_fee_odd*2)
        tuition_waiver = tuition_fee*std_waiver
        tot_tuition_waiver = tuition_waiver*4
        le_waiver = 0
        tot_hostel_waiver = hostel_waiver*2
        total_waiver_all = tuition_waiver+le_waiver+hostel_waiver
        total_waiver = tuition_waiver
        tot_waivers = (total_waiver_all*2) + (total_waiver*2)
        tot_pay_odd = tot_fee_odd-total_waiver_all
        tot_pay_even = tot_fee_even - total_waiver
        total_payable = grand_tot-tot_waivers
        return render_template('DashboardStd.html',stdId=std_id,stdName=std_name,stdDept=std_dept,stdEmail=std_email,previosBal=std_previous,tuitionFee=tuition_fee,leFee=lab_exam_fee,hostelFee=hostel_fee,
                                totalFeeOdd=tot_fee_odd,totalFeeEven=tot_fee_even,totTuitionFee=tot_tuition_fee,totLeFee=tot_le_fee,totHostelFee=tot_hostel_fee,grandTotal=grand_tot,tuitionWaiver=tuition_waiver,
                                totTuitionWaiver=tot_tuition_waiver,leWaiver=le_waiver,totLeWaiver=0,hostelWaiver=hostel_waiver,totHostelWavier=tot_hostel_waiver,totalWaiverAll=total_waiver_all,totalWaiver=total_waiver,
                                totWaivers=tot_waivers,totalPayOdd=tot_pay_odd,totalPayEven=tot_pay_even,totalPayable=total_payable)
    else:
       session.pop('loggedin', None) 
       return redirect(url_for('index'))


@app.route('/dashboardfaculty')
def dashboardFaculty():
    cur = mysql.connection.cursor()
    if session['loggedin'] == True:
        cur.execute("SELECT * FROM Faculty where (u_id=%s)",(session['id'],))
        emp_detail = cur.fetchone()
        emp_id = emp_detail[0]
        emp_name = emp_detail[1]
        emp_desg= emp_detail[3]
        emp_email = emp_detail[2]
        emp_sal = emp_detail[4]
        cur.execute("SELECT * FROM Expenses")
        exp_detail = cur.fetchone()
        elec_exp = exp_detail[0]
        eobi_exp = exp_detail[1]
        umrah_exp = exp_detail[2]
        rent_exp = exp_detail[3]
        mess_exp = exp_detail[4]
        lp_exp = exp_detail[5]
        income_tax = exp_detail[6]
        care_rent = exp_detail[7]
        tot_exp = elec_exp+eobi_exp+umrah_exp+rent_exp+mess_exp+lp_exp+income_tax+care_rent
        salary_tot = emp_sal-tot_exp
        return render_template('DashboardFaculty.html',empId=emp_id,empName=emp_name,empDesg=emp_desg,empEmail=emp_email,salary=emp_sal,
                                elecExp=elec_exp,eobiExp=eobi_exp,umrahExp=umrah_exp,rentExp=rent_exp,messExp=mess_exp,lpExp=lp_exp,
                                incomeTax=income_tax,careRent=care_rent,totalExp=tot_exp,salaryTot=salary_tot)
    else:
       session.pop('loggedin', None) 
       return redirect(url_for('index'))

@app.route('/dashboardemp',methods=['GET','POST'])
def dashboardemp():
    if session['loggedin'] == True:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Employee where (u_id=%s)",(session['id'],))
        result = cur.fetchone()
        cur.execute("SELECT * FROM Posts order by p_date ")
        posts = cur.fetchall()
        if result[2] =='Approver':
            if request.method=='POST':
                session['number'] = request.form['id']

                if request.form['check'] == 'Accept':
                    return redirect(url_for('accept')) 
                else:
                    return redirect(url_for('reject'))
            data = []
            newdata = []
            for i in posts:
                if i[3] == 'Unknown':
                    newdata.append(i)
                else:
                    data.append(i)
            return render_template('DashboardApprover.html',data=data,newdata=newdata,len=len,empName=result[1])
        elif result[2] == 'Reviewer':
            if request.method=='POST':
                post_details = request.form
                title = post_details['title']
                postinfo = post_details['postinfo']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO Posts (p_title,p_data) VALUES (%s,%s)",(title,postinfo))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('dashboardemp'))
            return render_template('DashboardReviewer.html',data=posts,len=len,empName=result[1])
    else:
       session.pop('loggedin', None) 
       return redirect(url_for('index'))

@app.route('/accept')
def accept():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Posts SET p_status= 'Accept' WHERE p_id=%s",(session['number'],))
    mysql.connection.commit()
    cur.close()
    session.pop('number',None)
    return redirect(url_for('dashboardemp'))

@app.route('/reject')
def reject():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE Posts SET p_status= 'Reject' WHERE p_id=%s",(session['number'],))
    mysql.connection.commit()
    cur.close()
    session.pop('number',None)
    return redirect(url_for('dashboardemp'))

@app.route('/logout')
def logout():
    session['loggedin'] = False
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/teststore')
def teststore():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Test(t_status) VALUES (%s)",('Pass',))
    mysql.connection.commit()
    cur.close()
    return "Pass"
    

@app.route('/testfetch')
def testfetch():
    cur = mysql.connection.cursor()
    cur.execute("SELECT t_status FROM Test")
    res = cur.fetchone()
    return "Pass"
@app.route('/testuser')
def testuser():
    cur = mysql.connection.cursor()
    cur.execute("SELECT u_name FROM Users")
    res = cur.fetchall()
    result = [x[0] for x in res]
    return result 
