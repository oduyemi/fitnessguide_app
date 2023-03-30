import os,random

from flask import render_template, redirect, flash, session, request, url_for
from fitnessguide.models import Options, Employment,Environment,Lifestyle,Personality,Relationship,Symptoms,Categories,Readjustment
from fitnessguide import app, db
from sqlalchemy.sql import text




@app.route('/')
def home():
    return render_template('users/demo.html')



@app.route('/employment', methods=['GET','POST'])
def employment():
    deets = db.session.query(Employment).all()
    mdeets = db.session.query(Employment).order_by(Employment.q_id).all()
    id = db.session.query(Employment).order_by(Employment.q_id).first()
    if request.method=='GET':
        return render_template('users/employment.html', deets=deets,mdeets=mdeets)
    else:
        em1 = request.form.get('q1')
        em2 = request.form.get('q2')
        em3 = request.form.get('q3')
        em4 = request.form.get('q4')
        em5 = request.form.get('q5')
        em6 = request.form.get('q6')
        em7 = request.form.get('q7')
        em8 = request.form.get('q8')
        em9 = request.form.get('q9')
        em10 = request.form.get('q10')
        em11 = request.form.get('q11')
        em12 = request.form.get('q12')
        em13 = request.form.get('q13')
        em14 = request.form.get('q14')
        em15 = request.form.get('q15')
        em16 = request.form.get('q16')


        sql1 = f"UPDATE Employment SET qstn_value = '{em1}' WHERE q_id = 1"
        sql2 = f"UPDATE Employment SET qstn_value = '{em2}' WHERE q_id = 2"
        sql3 = f"UPDATE Employment SET qstn_value = '{em3}' WHERE q_id = 3"
        sql4 = f"UPDATE Employment SET qstn_value = '{em4}' WHERE q_id = 4"
        sql5 = f"UPDATE Employment SET qstn_value = '{em5}' WHERE q_id = 5"
        sql6 = f"UPDATE Employment SET qstn_value = '{em6}' WHERE q_id = 6"
        sql7 = f"UPDATE Employment SET qstn_value = '{em7}' WHERE q_id = 7"
        sql8 = f"UPDATE Employment SET qstn_value = '{em8}' WHERE q_id = 8"
        sql9 = f"UPDATE Employment SET qstn_value = '{em9}' WHERE q_id = 9"
        sql10 = f"UPDATE Employment SET qstn_value = '{em10}' WHERE q_id =10"
        sql11 = f"UPDATE Employment SET qstn_value = '{em11}' WHERE q_id = 11"
        sql12 = f"UPDATE Employment SET qstn_value = '{em12}' WHERE q_id = 12"
        sql13 = f"UPDATE Employment SET qstn_value = '{em13}' WHERE q_id = 13"
        sql14 = f"UPDATE Employment SET qstn_value = '{em14}' WHERE q_id = 14"
        sql15 = f"UPDATE Employment SET qstn_value = '{em15}' WHERE q_id = 15"
        sql16 = f"UPDATE Employment SET qstn_value = '{em16}' WHERE q_id = 16"

        total = "SELECT SUM(qstn_value) FROM employment"
        catv = "UPDATE Categories SET cat_point = (SELECT SUM(qstn_value) FROM employment) WHERE cat_name = 'employment'"


        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(catv))

        db.session.commit()

        testing = "SELECT qstn_value from Employment"
        return redirect('/environment')
        #return render_template('users/environment.html',testing=testing, deets=deets,mdeets=mdeets,opt=opt)

@app.route('/environment', methods=['GET','POST'])
def environment():
    deets = db.session.query(Employment).all()
    mdeets = db.session.query(Employment).order_by(Employment.q_id).all()
    id = db.session.query(Employment).order_by(Employment.q_id).first()
    if request.method=='GET':
        return render_template('users/environment.html', deets=deets,mdeets=mdeets)
    else:
        en1 = request.form.get('q1')
        en2 = request.form.get('q2')
        en3 = request.form.get('q3')
        en4 = request.form.get('q4')
        en5 = request.form.get('q5')
        en6 = request.form.get('q6')
        en7 = request.form.get('q7')
        en8 = request.form.get('q8')
        en9 = request.form.get('q9')
        en10 = request.form.get('q10')
        en11 = request.form.get('q11')
        en12 = request.form.get('q12')
        en13 = request.form.get('q13')
        en14 = request.form.get('q14')
        en15 = request.form.get('q15')
        en16 = request.form.get('q16')

        sql1 = f"UPDATE Environment SET qstn_value = '{en1}' WHERE q_id = 1"
        sql2 = f"UPDATE Environment SET qstn_value = '{en2}' WHERE q_id = 2"
        sql3 = f"UPDATE Environment SET qstn_value = '{en3}' WHERE q_id = 3"
        sql4 = f"UPDATE Environment SET qstn_value = '{en4}' WHERE q_id = 4"
        sql5 = f"UPDATE Environment SET qstn_value = '{en5}' WHERE q_id = 5"
        sql6 = f"UPDATE Environment SET qstn_value = '{en6}' WHERE q_id = 6"
        sql7 = f"UPDATE Environment SET qstn_value = '{en7}' WHERE q_id = 7"
        sql8 = f"UPDATE Environment SET qstn_value = '{en8}' WHERE q_id = 8"
        sql9 = f"UPDATE Environment SET qstn_value = '{en9}' WHERE q_id = 9"
        sql10 = f"UPDATE Environment SET qstn_value = '{en10}' WHERE q_id =10"
        sql11 = f"UPDATE Environment SET qstn_value = '{en11}' WHERE q_id = 11"
        sql12 = f"UPDATE Environment SET qstn_value = '{en12}' WHERE q_id = 12"
        sql13 = f"UPDATE Environment SET qstn_value = '{en13}' WHERE q_id = 13"
        sql14 = f"UPDATE Environment SET qstn_value = '{en14}' WHERE q_id = 14"
        sql15 = f"UPDATE Environment SET qstn_value = '{en15}' WHERE q_id = 15"
        sql16 = f"UPDATE Environment SET qstn_value = '{en16}' WHERE q_id = 16"

        total = "SELECT SUM(qstn_value) FROM environment"
        catv = "UPDATE Categories SET cat_point = (SELECT SUM(qstn_value) FROM environment) WHERE cat_name = 'environment'"
        
        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(catv))
        db.session.commit()
        return redirect(url_for('lifestyle'))


@app.route('/lifestyle', methods=['GET','POST'])
def lifestyle():
    deets = db.session.query(Lifestyle).all()
    mdeets = db.session.query(Lifestyle).order_by(Lifestyle.q_id).all()
    id = db.session.query(Lifestyle).order_by(Lifestyle.q_id).first()
    if request.method=='GET':
        return render_template('users/lifestyle.html', deets=deets,mdeets=mdeets)
    else:
        ls1 = request.form.get('q1')
        ls2 = request.form.get('q2')
        ls3 = request.form.get('q3')
        ls4 = request.form.get('q4')
        ls5 = request.form.get('q5')
        ls6 = request.form.get('q6')
        ls7 = request.form.get('q7')
        ls8 = request.form.get('q8')
        ls9 = request.form.get('q9')
        ls10 = request.form.get('q10')
        ls11 = request.form.get('q11')
        ls12 = request.form.get('q12')
        ls13 = request.form.get('q13')
        ls14 = request.form.get('q14')
        ls15 = request.form.get('q15')
        ls16 = request.form.get('q16')

        sql1 = f"UPDATE Lifestyle SET qstn_value = '{ls1}' WHERE q_id = 1"
        sql2 = f"UPDATE Lifestyle SET qstn_value = '{ls2}' WHERE q_id = 2"
        sql3 = f"UPDATE Lifestyle SET qstn_value = '{ls3}' WHERE q_id = 3"
        sql4 = f"UPDATE Lifestyle SET qstn_value = '{ls4}' WHERE q_id = 4"
        sql5 = f"UPDATE Lifestyle SET qstn_value = '{ls5}' WHERE q_id = 5"
        sql6 = f"UPDATE Lifestyle SET qstn_value = '{ls6}' WHERE q_id = 6"
        sql7 = f"UPDATE Lifestyle SET qstn_value = '{ls7}' WHERE q_id = 7"
        sql8 = f"UPDATE Lifestyle SET qstn_value = '{ls8}' WHERE q_id = 8"
        sql9 = f"UPDATE Lifestyle SET qstn_value = '{ls9}' WHERE q_id = 9"
        sql10 = f"UPDATE Lifestyle SET qstn_value = '{ls10}' WHERE q_id =10"
        sql11 = f"UPDATE Lifestyle SET qstn_value = '{ls11}' WHERE q_id = 11"
        sql12 = f"UPDATE Lifestyle SET qstn_value = '{ls12}' WHERE q_id = 12"
        sql13 = f"UPDATE Lifestyle SET qstn_value = '{ls13}' WHERE q_id = 13"
        sql14 = f"UPDATE Lifestyle SET qstn_value = '{ls14}' WHERE q_id = 14"
        sql15 = f"UPDATE Lifestyle SET qstn_value = '{ls15}' WHERE q_id = 15"
        sql16 = f"UPDATE Lifestyle SET qstn_value = '{ls16}' WHERE q_id = 16"

        total = "SELECT SUM(qstn_value) FROM lifestyle"
        catv = "UPDATE Categories SET cat_point = (SELECT SUM(qstn_value) FROM lifestyle) WHERE cat_name = 'lifestyle'"


        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(catv))
        db.session.commit()
        return redirect(url_for('personality'))



@app.route('/personality', methods=['GET','POST'])
def personality():
    deets = db.session.query(Personality).all()
    mdeets = db.session.query(Personality).order_by(Personality.q_id).all()
    id = db.session.query(Personality).order_by(Personality.q_id).first()
    if request.method=='GET':
        return render_template('users/personality.html', deets=deets,mdeets=mdeets)
    else:
        p1 = request.form.get('q1')
        p2 = request.form.get('q2')
        p3 = request.form.get('q3')
        p4 = request.form.get('q4')
        p5 = request.form.get('q5')
        p6 = request.form.get('q6')
        p7 = request.form.get('q7')
        p8 = request.form.get('q8')
        p9 = request.form.get('q9')
        p10 = request.form.get('q10')
        p11 = request.form.get('q11')
        p12 = request.form.get('q12')
        p13 = request.form.get('q13')
        p14 = request.form.get('q14')
        p15 = request.form.get('q15')
        p16 = request.form.get('q16')
        p17 = request.form.get('q17')
        p18 = request.form.get('q18')
        p19 = request.form.get('q19')
        p20 = request.form.get('q20')

        sql1 = f"UPDATE Personality SET qstn_value = '{p1}' WHERE q_id = 1"
        sql2 = f"UPDATE Personality SET qstn_value = '{p2}' WHERE q_id = 2"
        sql3 = f"UPDATE Personality SET qstn_value = '{p3}' WHERE q_id = 3"
        sql4 = f"UPDATE Personality SET qstn_value = '{p4}' WHERE q_id = 4"
        sql5 = f"UPDATE Personality SET qstn_value = '{p5}' WHERE q_id = 5"
        sql6 = f"UPDATE Personality SET qstn_value = '{p6}' WHERE q_id = 6"
        sql7 = f"UPDATE Personality SET qstn_value = '{p7}' WHERE q_id = 7"
        sql8 = f"UPDATE Personality SET qstn_value = '{p8}' WHERE q_id = 8"
        sql9 = f"UPDATE Personality SET qstn_value = '{p9}' WHERE q_id = 9"
        sql10 = f"UPDATE Personality SET qstn_value = '{p10}' WHERE q_id =10"
        sql11 = f"UPDATE Personality SET qstn_value = '{p11}' WHERE q_id = 11"
        sql12 = f"UPDATE Personality SET qstn_value = '{p12}' WHERE q_id = 12"
        sql13 = f"UPDATE Personality SET qstn_value = '{p13}' WHERE q_id = 13"
        sql14 = f"UPDATE Personality SET qstn_value = '{p14}' WHERE q_id = 14"
        sql15 = f"UPDATE Personality SET qstn_value = '{p15}' WHERE q_id = 15"
        sql16 = f"UPDATE Personality SET qstn_value = '{p16}' WHERE q_id = 16"
        sql17 = f"UPDATE Personality SET qstn_value = '{p17}' WHERE q_id = 17"
        sql18 = f"UPDATE Personality SET qstn_value = '{p18}' WHERE q_id = 18"
        sql19 = f"UPDATE Personality SET qstn_value = '{p19}' WHERE q_id = 19"
        sql20 = f"UPDATE Personality SET qstn_value = '{p20}' WHERE q_id = 20"

        total = "SELECT SUM(qstn_value) FROM personality"
        catv = "UPDATE Categories SET cat_point = (SELECT SUM(qstn_value) FROM personality) WHERE cat_name = 'personality'"

        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(sql17))
        db.session.execute(text(sql18))
        db.session.execute(text(sql19))
        db.session.execute(text(sql20))
        db.session.execute(text(catv))
        db.session.commit()
        return redirect(url_for('relationship'))


@app.route('/relationship', methods=['GET','POST'])
def relationship():
    deets = db.session.query(Relationship).all()
    mdeets = db.session.query(Relationship).order_by(Relationship.q_id).all()
    id = db.session.query(Relationship).order_by(Relationship.q_id).first()
    if request.method=='GET':
        return render_template('users/relationship.html', deets=deets,mdeets=mdeets)
    else:
        r1 = request.form.get('q1')
        r2 = request.form.get('q2')
        r3 = request.form.get('q3')
        r4 = request.form.get('q4')
        r5 = request.form.get('q5')
        r6 = request.form.get('q6')
        r7 = request.form.get('q7')
        r8 = request.form.get('q8')
        r9 = request.form.get('q9')
        r10 = request.form.get('q10')
        r11 = request.form.get('q11')
        r12 = request.form.get('q12')
        r13 = request.form.get('q13')
        r14 = request.form.get('q14')
        r15 = request.form.get('q15')
        r16 = request.form.get('q16')


        sql1 = f"UPDATE Relationship SET qstn_value = '{r1}' WHERE q_id = 1"
        sql2 = f"UPDATE Relationship SET qstn_value = '{r2}' WHERE q_id = 2"
        sql3 = f"UPDATE Relationship SET qstn_value = '{r3}' WHERE q_id = 3"
        sql4 = f"UPDATE Relationship SET qstn_value = '{r4}' WHERE q_id = 4"
        sql5 = f"UPDATE Relationship SET qstn_value = '{r5}' WHERE q_id = 5"
        sql6 = f"UPDATE Relationship SET qstn_value = '{r6}' WHERE q_id = 6"
        sql7 = f"UPDATE Relationship SET qstn_value = '{r7}' WHERE q_id = 7"
        sql8 = f"UPDATE Relationship SET qstn_value = '{r8}' WHERE q_id = 8"
        sql9 = f"UPDATE Relationship SET qstn_value = '{r9}' WHERE q_id = 9"
        sql10 = f"UPDATE Relationship SET qstn_value = '{r10}' WHERE q_id =10"
        sql11 = f"UPDATE Relationship SET qstn_value = '{r11}' WHERE q_id = 11"
        sql12 = f"UPDATE Relationship SET qstn_value = '{r12}' WHERE q_id = 12"
        sql13 = f"UPDATE Relationship SET qstn_value = '{r13}' WHERE q_id = 13"
        sql14 = f"UPDATE Relationship SET qstn_value = '{r14}' WHERE q_id = 14"
        sql15 = f"UPDATE Relationship SET qstn_value = '{r15}' WHERE q_id = 15"
        sql16 = f"UPDATE Relationship SET qstn_value = '{r16}' WHERE q_id = 16"


        total = "SELECT SUM(qstn_value) FROM relationship"
        catv = "UPDATE Categories SET cat_point = (SELECT SUM(qstn_value) FROM relationship) WHERE cat_name = 'relationship'"


        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(catv))
        db.session.commit()
        return redirect(url_for('symptoms'))


@app.route('/symptoms', methods=['GET','POST'])
def symptoms():
    deets = db.session.query(Symptoms).all()
    mdeets = db.session.query(Symptoms).order_by(Symptoms.q_id).all()
    id = db.session.query(Symptoms).order_by(Symptoms.q_id).first()
    if request.method=='GET':
        return render_template('users/symptoms.html', deets=deets,mdeets=mdeets)
    else:
        s1 = request.form.get('q1')
        s2 = request.form.get('q2')
        s3 = request.form.get('q3')
        s4 = request.form.get('q4')
        s5 = request.form.get('q5')
        s6 = request.form.get('q6')
        s7 = request.form.get('q7')
        s8 = request.form.get('q8')
        s9 = request.form.get('q9')
        s10 = request.form.get('q10')
        s11 = request.form.get('q11')
        s12 = request.form.get('q12')
        s13 = request.form.get('q13')
        s14 = request.form.get('q14')
        s15 = request.form.get('q15')
        s16 = request.form.get('q16')


        sql1 = f"UPDATE Symptoms SET qstn_value = '{s1}' WHERE q_id = 1"
        sql2 = f"UPDATE Symptoms SET qstn_value = '{s2}' WHERE q_id = 2"
        sql3 = f"UPDATE Symptoms SET qstn_value = '{s3}' WHERE q_id = 3"
        sql4 = f"UPDATE Symptoms SET qstn_value = '{s4}' WHERE q_id = 4"
        sql5 = f"UPDATE Symptoms SET qstn_value = '{s5}' WHERE q_id = 5"
        sql6 = f"UPDATE Symptoms SET qstn_value = '{s6}' WHERE q_id = 6"
        sql7 = f"UPDATE Symptoms SET qstn_value = '{s7}' WHERE q_id = 7"
        sql8 = f"UPDATE Symptoms SET qstn_value = '{s8}' WHERE q_id = 8"
        sql9 = f"UPDATE Symptoms SET qstn_value = '{s9}' WHERE q_id = 9"
        sql10 = f"UPDATE Symptoms SET qstn_value = '{s10}' WHERE q_id =10"
        sql11 = f"UPDATE Symptoms SET qstn_value = '{s11}' WHERE q_id = 11"
        sql12 = f"UPDATE Symptoms SET qstn_value = '{s12}' WHERE q_id = 12"
        sql13 = f"UPDATE Symptoms SET qstn_value = '{s13}' WHERE q_id = 13"
        sql14 = f"UPDATE Symptoms SET qstn_value = '{s14}' WHERE q_id = 14"
        sql15 = f"UPDATE Symptoms SET qstn_value = '{s15}' WHERE q_id = 15"
        sql16 = f"UPDATE Symptoms SET qstn_value = '{s16}' WHERE q_id = 16"


        total = "SELECT SUM(qstn_value) FROM symptoms"
        catv = "UPDATE Categories SET cat_point = (SELECT SUM(qstn_value) FROM symptoms) WHERE cat_name = 'symptoms'"
        sumdeets = "UPDATE Categories SET total_score = (SELECT SUM(cat_point) FROM Categories) WHERE cat_name = 'total'"

        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(catv))
        db.session.execute(text(sumdeets))
        db.session.commit()
        return redirect(url_for('step2'))


@app.route('/result', methods=['GET','POST'])
def result():
    #ideets = Categories.query.all()
    catname = db.session.query(Categories.cat_name).all()
    catpoint= db.session.query(Categories.cat_point).all()
    alldeets = db.session.query(Categories).all()
    deets = db.session.query(Categories.total_score).filter(Categories.cat_name=='total').one()
    
    #udeets = ResultSet.getInt(deets)
    mdeets = db.session.query(Categories.cat_id).all()
    if request.method=='GET':
        return render_template('users/result.html', deets=deets,mdeets=mdeets,catpoint=catpoint,catname=catname,alldeets=alldeets)


@app.route('/step2', methods=['GET','POST'])
def step2():
    deets = db.session.query(Symptoms).all()
    mdeets = db.session.query(Symptoms).order_by(Symptoms.q_id).all()
    id = db.session.query(Symptoms).order_by(Symptoms.q_id).first()
    if request.method=='GET':
        return render_template('users/step2.html', deets=deets,mdeets=mdeets)
    else:
        s1 = request.form.get('q1')
        s2 = request.form.get('q2')
        s3 = request.form.get('q3')
        s4 = request.form.get('q4')
        s5 = request.form.get('q5')

        if s1=='yes' or s2=='yes' or  s3=='yes' or s4=='yes' or s5=='yes':
            m = 3
            adddeets = f'UPDATE Categories SET total_score = total_score + {m} WHERE cat_name = "total"'
            
            db.session.execute(text(adddeets))
            db.session.commit()

        return redirect(url_for('step3'))


@app.route('/step3', methods=['GET','POST'])
def step3():
    deets = db.session.query(Symptoms).all()
    mdeets = db.session.query(Symptoms).order_by(Symptoms.q_id).all()
    id = db.session.query(Symptoms).order_by(Symptoms.q_id).first()
    if request.method=='GET':
        return render_template('users/step3.html', deets=deets,mdeets=mdeets)
    else:
        s1 = request.form.get('q1')
        s2 = request.form.get('q2')
        s3 = request.form.get('q3')
        s4 = request.form.get('q4')
        s5 = request.form.get('q5')

        n = 2
        lastdeets = f'UPDATE Categories SET total_score = total_score +{n} WHERE cat_name = "total"'
        
        db.session.execute(text(lastdeets))
        db.session.commit()

        return redirect(url_for('result'))


@app.route('/sed_lifestyle', methods=['GET','POST'])
def sed_lifestyle():
    deets = db.session.query(Symptoms).all()
    mdeets = db.session.query(Symptoms).order_by(Symptoms.q_id).all()
    id = db.session.query(Symptoms).order_by(Symptoms.q_id).first()
    if request.method=='GET':
        return render_template('users/sedentary_lifestyle.html', deets=deets,mdeets=mdeets)
    else:
        slt1 = request.form.get('sl1')
        slt2 = request.form.get('sl2')
        slt3 = request.form.get('sl3')
        slt4 = request.form.get('sl4')
        slt5 = request.form.get('sl5')
        slt6 = request.form.get('sl6')
        slt7 = request.form.get('sl7')
        slt8 = request.form.get('sl8')
        slt9 = request.form.get('sl9')
        slt10 = request.form.get('sl10')
        slt11 = request.form.get('sl11')
        slt12 = request.form.get('sl12')
        slt13 = request.form.get('sl13')
        slt14 = request.form.get('sl14')
        slt15 = request.form.get('sl15')
        slt16 = request.form.get('sl16')
        slt17 = request.form.get('sl17')

        #sltsum = int(slt1 + slt2 + slt3 + slt4 + slt5 + slt6 + slt7 + slt8 + slt9 + slt10 + slt11 + slt12 + slt13 + slt14 + slt15 +slt16 + slt17)

        # if sltsum >24:
        #     flash('please, your total hours spent in a day should not be more than 24hrs')
        #     return redirect(url_for('sed_lifestyle'))
        # else:

        s1 = parseFloat(slt1 * 0.8)
        s2 = slt2 * 0.8
        s3 = slt3 * 0.8
        s4 = slt4 * 1.5
        s5 = slt5 * 1.5
        s6 = slt6 * 1.5
        s7 = slt7 * 1.5
        s8 = slt8 * 2
        s9 = slt9 * 3
        s10 = slt10 * 4
        s11 = slt11 * 5
        s12 = slt12 * 3
        s13 = slt13 * 4
        s14 = slt14 * 5
        s15 = slt15 * 7
        s16 = slt16 * 8
        s17 = slt17 * 9


        sql1 = f"UPDATE Symptoms SET qstn_value = '{s1}' WHERE q_id = 1"
        sql2 = f"UPDATE Symptoms SET qstn_value = '{s2}' WHERE q_id = 2"
        sql3 = f"UPDATE Symptoms SET qstn_value = '{s3}' WHERE q_id = 3"
        sql4 = f"UPDATE Symptoms SET qstn_value = '{s4}' WHERE q_id = 4"
        sql5 = f"UPDATE Symptoms SET qstn_value = '{s5}' WHERE q_id = 5"
        sql6 = f"UPDATE Symptoms SET qstn_value = '{s6}' WHERE q_id = 6"
        sql7 = f"UPDATE Symptoms SET qstn_value = '{s7}' WHERE q_id = 7"
        sql8 = f"UPDATE Symptoms SET qstn_value = '{s8}' WHERE q_id = 8"
        sql9 = f"UPDATE Symptoms SET qstn_value = '{s9}' WHERE q_id = 9"
        sql10 = f"UPDATE Symptoms SET qstn_value = '{s10}' WHERE q_id =10"
        sql11 = f"UPDATE Symptoms SET qstn_value = '{s11}' WHERE q_id = 11"
        sql12 = f"UPDATE Symptoms SET qstn_value = '{s12}' WHERE q_id = 12"
        sql13 = f"UPDATE Symptoms SET qstn_value = '{s13}' WHERE q_id = 13"
        sql14 = f"UPDATE Symptoms SET qstn_value = '{s14}' WHERE q_id = 14"
        sql15 = f"UPDATE Symptoms SET qstn_value = '{s15}' WHERE q_id = 15"
        sql16 = f"UPDATE Symptoms SET qstn_value = '{s16}' WHERE q_id = 16"


        total = "SELECT SUM(qstn_value) FROM symptoms"
        catv = "UPDATE Categories SET cat_point = (SELECT SUM(qstn_value) FROM symptoms) WHERE cat_name = 'symptoms'"
        sumdeets = "UPDATE Categories SET total_score = (SELECT SUM(cat_point) FROM Categories) WHERE cat_name = 'total'"

        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(catv))
        db.session.execute(text(sumdeets))
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/social', methods=['GET','POST'])
def social():
    deets = db.session.query(Symptoms).all()
    mdeets = db.session.query(Symptoms).order_by(Symptoms.q_id).all()
    id = db.session.query(Symptoms).order_by(Symptoms.q_id).first()
    if request.method=='GET':
        return render_template('users/social.html', deets=deets,mdeets=mdeets)
    else:
        soc1 = request.form.get('dos1')
        soc2 = request.form.get('dos2')
        soc3 = request.form.get('dos3')
        soc4 = request.form.get('dos4')
        soc5 = request.form.get('dos5')
        soc6 = request.form.get('dos6')
        soc7 = request.form.get('dos7')
        soc8 = request.form.get('dos8')
        soc9 = request.form.get('dos9')
        soc10 = request.form.get('dos10')
        soc11 = request.form.get('dos11')
        soc12 = request.form.get('dos12')
        soc13 = request.form.get('dos13')
        soc14 = request.form.get('dos14')
        soc15 = request.form.get('dos15')
        soc16 = request.form.get('dos16')
        soc17 = request.form.get('dos17')
        soc18 = request.form.get('dos18')
        soc19 = request.form.get('dos19')
        soc20 = request.form.get('dos20')
        soc21 = request.form.get('dos21')
        soc22 = request.form.get('dos22')
        soc23 = request.form.get('dos23')
        soc24 = request.form.get('dos24')
        soc25 = request.form.get('dos25')
        soc26 = request.form.get('dos26')
        soc27 = request.form.get('dos27')
        soc28 = request.form.get('dos28')
        soc29 = request.form.get('dos29')
        soc30 = request.form.get('dos30')
        soc31 = request.form.get('dos31')
        soc32 = request.form.get('dos32')
        soc33 = request.form.get('dos33')
        soc34 = request.form.get('dos34')
        soc35 = request.form.get('dos35')
        soc36 = request.form.get('dos36')
        soc37 = request.form.get('dos37')
        soc38 = request.form.get('dos38')
        soc39 = request.form.get('dos39')
        soc40 = request.form.get('dos40')
        soc41 = request.form.get('dos41')
        soc42 = request.form.get('dos42')
        soc43 = request.form.get('dos43')
        soc44 = request.form.get('dos44')

     

        sql1 = f"UPDATE Social SET qstn_value = '{soc1}' WHERE q_id = 1"
        sql2 = f"UPDATE Social SET qstn_value = '{soc2}' WHERE q_id = 2"
        sql3 = f"UPDATE Social SET qstn_value = '{soc3}' WHERE q_id = 3"
        sql4 = f"UPDATE Social SET qstn_value = '{soc4}' WHERE q_id = 4"
        sql5 = f"UPDATE Social SET qstn_value = '{soc5}' WHERE q_id = 5"
        sql6 = f"UPDATE Social SET qstn_value = '{soc6}' WHERE q_id = 6"
        sql7 = f"UPDATE Social SET qstn_value = '{soc7}' WHERE q_id = 7"
        sql8 = f"UPDATE Social SET qstn_value = '{soc8}' WHERE q_id = 8"
        sql9 = f"UPDATE Social SET qstn_value = '{soc9}' WHERE q_id = 9"
        sql10 = f"UPDATE Social SET qstn_value = '{soc10}' WHERE q_id =10"
        sql11 = f"UPDATE Social SET qstn_value = '{soc11}' WHERE q_id = 11"
        sql12 = f"UPDATE Social SET qstn_value = '{soc12}' WHERE q_id = 12"
        sql13 = f"UPDATE Social SET qstn_value = '{soc13}' WHERE q_id = 13"
        sql14 = f"UPDATE Social SET qstn_value = '{soc14}' WHERE q_id = 14"
        sql15 = f"UPDATE Social SET qstn_value = '{soc15}' WHERE q_id = 15"
        sql16 = f"UPDATE Social SET qstn_value = '{soc16}' WHERE q_id = 16"
        sql17 = f"UPDATE Social SET qstn_value = '{soc17}' WHERE q_id = 17"
        sql18 = f"UPDATE Social SET qstn_value = '{soc18}' WHERE q_id = 18"
        sql19 = f"UPDATE Social SET qstn_value = '{soc19}' WHERE q_id = 19"
        sql20 = f"UPDATE Social SET qstn_value = '{soc20}' WHERE q_id = 20"
        sql21 = f"UPDATE Social SET qstn_value = '{soc21}' WHERE q_id = 21"
        sql22 = f"UPDATE Social SET qstn_value = '{soc22}' WHERE q_id = 22"
        sql23 = f"UPDATE Social SET qstn_value = '{soc23}' WHERE q_id = 23"
        sql24 = f"UPDATE Social SET qstn_value = '{soc24}' WHERE q_id = 24"
        sql25 = f"UPDATE Social SET qstn_value = '{soc25}' WHERE q_id = 25"
        sql26 = f"UPDATE Social SET qstn_value = '{soc26}' WHERE q_id = 26"
        sql27 = f"UPDATE Social SET qstn_value = '{soc27}' WHERE q_id = 27"
        sql28 = f"UPDATE Social SET qstn_value = '{soc28}' WHERE q_id = 28"
        sql29 = f"UPDATE Social SET qstn_value = '{soc29}' WHERE q_id = 29"
        sql30 = f"UPDATE Social SET qstn_value = '{soc30}' WHERE q_id = 30"
        sql31 = f"UPDATE Social SET qstn_value = '{soc31}' WHERE q_id = 31"
        sql32 = f"UPDATE Social SET qstn_value = '{soc32}' WHERE q_id = 32"
        sql33 = f"UPDATE Social SET qstn_value = '{soc33}' WHERE q_id = 33"
        sql34 = f"UPDATE Social SET qstn_value = '{soc34}' WHERE q_id = 34"
        sql35 = f"UPDATE Social SET qstn_value = '{soc35}' WHERE q_id = 35"
        sql36 = f"UPDATE Social SET qstn_value = '{soc36}' WHERE q_id = 36"
        sql37 = f"UPDATE Social SET qstn_value = '{soc37}' WHERE q_id = 37"
        sql38 = f"UPDATE Social SET qstn_value = '{soc38}' WHERE q_id = 38"
        sql39 = f"UPDATE Social SET qstn_value = '{soc39}' WHERE q_id = 39"
        sql40 = f"UPDATE Social SET qstn_value = '{soc40}' WHERE q_id = 40"
        sql41 = f"UPDATE Social SET qstn_value = '{soc41}' WHERE q_id = 41"
        sql42 = f"UPDATE Social SET qstn_value = '{soc42}' WHERE q_id = 42"
        sql43 = f"UPDATE Social SET qstn_value = '{soc43}' WHERE q_id = 43"
        sql44 = f"UPDATE Social SET qstn_value = '{soc44}' WHERE q_id = 44"




        total = "SELECT SUM(qstn_value) FROM social"
        catv = "UPDATE Readjustment SET srs_score = (SELECT SUM(qstn_value) FROM social) WHERE srs_name = 'social readjustment scale'"
        #sumdeets = "UPDATE Categories SET total_score = (SELECT SUM(cat_point) FROM Categories) WHERE cat_name = 'total'"

        db.session.execute(text(sql1))
        db.session.execute(text(sql2))
        db.session.execute(text(sql3))
        db.session.execute(text(sql4))
        db.session.execute(text(sql5))
        db.session.execute(text(sql6))
        db.session.execute(text(sql7))
        db.session.execute(text(sql8))
        db.session.execute(text(sql9))
        db.session.execute(text(sql10))
        db.session.execute(text(sql11))
        db.session.execute(text(sql12))
        db.session.execute(text(sql13))
        db.session.execute(text(sql14))
        db.session.execute(text(sql15))
        db.session.execute(text(sql16))
        db.session.execute(text(sql17))
        db.session.execute(text(sql18))
        db.session.execute(text(sql19))
        db.session.execute(text(sql20))
        db.session.execute(text(sql21))
        db.session.execute(text(sql22))
        db.session.execute(text(sql23))
        db.session.execute(text(sql24))
        db.session.execute(text(sql25))
        db.session.execute(text(sql26))
        db.session.execute(text(sql27))
        db.session.execute(text(sql28))
        db.session.execute(text(sql29))
        db.session.execute(text(sql30))
        db.session.execute(text(sql31))
        db.session.execute(text(sql32))
        db.session.execute(text(sql33))
        db.session.execute(text(sql34))
        db.session.execute(text(sql35))
        db.session.execute(text(sql36))
        db.session.execute(text(sql37))
        db.session.execute(text(sql38))
        db.session.execute(text(sql39))
        db.session.execute(text(sql40))
        db.session.execute(text(sql41))
        db.session.execute(text(sql42))
        db.session.execute(text(sql43))
        db.session.execute(text(sql44))
        db.session.execute(text(catv))
        #db.session.execute(text(sumdeets))
        db.session.commit()
        return redirect(url_for('home'))

    
