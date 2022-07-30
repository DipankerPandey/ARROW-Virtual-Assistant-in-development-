import sqlite3
from internet import check_internet_connection


def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection


def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM QuestionsAndAnswers")

    return cur.fetchall()


def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO QuestionsAndAnswers values ('" + question + "','" + answer + "')"
    cur.execute(query)
    con.commit()

def get_sam_mem():
    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM Sam")

    return cur.fetchall()


def insert_sam_mem(question, answer):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO Sam values ('" + question + "','" + answer + "')"
    cur.execute(query)
    con.commit()

def get_answer_from_sam(question):
    rows = get_sam_mem()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer

def get_answer_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    return answer


def put_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value='" + str(last_seen_date) + "'where name= 'last_seen_date'"
    cur.execute(query)
    con.commit()


def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name= 'last_seen_date'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])


def turn_on_speech():
    if check_internet_connection():
        con = create_connection()
        cur = con.cursor()
        query = "update memory set value='" + "on" + "'where name= 'speech'"
        cur.execute(query)
        con.commit()
        return "You shall hear my voice now"
    else:
        return "No internet access"


def turn_off_speech():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value='" + "off" + "'where name= 'speech'"
    cur.execute(query)
    con.commit()
    return "Ok i wont speak..."


def speak_is_on():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name= 'speech'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    return False


def listen_command():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name= 'name_said'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    return False


def turn_on_name_said():
    if check_internet_connection():
        con = create_connection()
        cur = con.cursor()
        query = "update memory set value='" + "on" + "'where name= 'name_said'"
        cur.execute(query)
        con.commit()


def turn_off_name_said():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value='" + "off" + "'where name= 'name_said'"
    cur.execute(query)
    con.commit()


def turn_on_hearing():
    if check_internet_connection():
        con = create_connection()
        cur = con.cursor()
        query = "update memory set value='" + "on" + "'where name= 'hear_me'"
        cur.execute(query)
        con.commit()
        return r"I'll be listening"


def turn_off_hearing():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value='" + "off" + "'where name= 'hear_me'"
    cur.execute(query)
    con.commit()
    return "You can type now"


def hearing():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name= 'hear_me'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    return False

def sam_mode():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name= 'sam_mode'"
    cur.execute(query)
    ans = str(cur.fetchall()[0][0])
    if ans == "on":
        return True
    return False


def turn_on_sam_mode():
    if check_internet_connection():
        con = create_connection()
        cur = con.cursor()
        query = "update memory set value='" + "on" + "'where name= 'sam_mode'"
        cur.execute(query)
        con.commit()


def turn_off_sam_mode():
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value='" + "off" + "'where name= 'sam_mode'"
    cur.execute(query)
    con.commit()
