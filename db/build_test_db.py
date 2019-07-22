#!/usr/bin/env python3
import subprocess
import sqlite3

def main():
    # connect to database
    db = sqlite3.connect("courses.db")
    dbc = db.cursor()

    # clear tables
    tables = subprocess.getoutput("sqlite3 courses.db .tables")
    for t in tables.split():
        dbc.execute("drop table %s;" % t)

    # reinitialize tables
    init_file = open("init.sql", "r")
    dbc.executescript(init_file.read())
    init_file.close()

    # insert test values into tables
    for i in courses.keys():
        c = courses[i]
        dbc.execute("insert into courses(id, dept, dept_name, course_num, \
            course_name, course_cred, course_reqs, course_desc, course_attr, \
            semesters) values (?,?,?,?,?,?,?,?,?,?)", \
            (i, c["dept"], c["dept_name"], c["course_num"], c["course_name"], \
            c["course_cred"], c["course_reqs"], c["course_desc"], \
            c["course_attr"], (",").join([str(j) for j in c["semesters"]])) \
        )

    for i in sections.keys():
        s = sections[i]
        dbc.execute("insert into sections(id, semester, course_id, section, \
            component, days, time, loc, prof) values (?,?,?,?,?,?,?,?,?)", \
            (i, s["semester"], s["course_id"], s["section"], s["component"], \
            s["days"], s["time"], s["loc"], s["prof"]) \
        )

    for i in semesters.keys():
        dbc.execute("insert into semesters(id,name) values (?,?)", \
            (i, semesters[i]["name"])
        )

    # commit inserts
    db.commit()

    # close connection
    db.close()


# define test list of courses and sections
courses = {
    1: {
        "dept": "MA",
        "dept_name": "Math",
        "course_num": "225",
        "course_name": "Baby Math",
        "course_cred": 3,
        "course_reqs": "",
        "course_desc": "little proofs",
        "course_attr": "fall and spring",
        "semesters": [1,2]
    },
    2: {
        "dept": "MA",
        "dept_name": "Math",
        "course_num": "425",
        "course_name": "Real Analysis 1",
        "course_cred": 3,
        "course_reqs": "MA 225",
        "course_desc": "bigger proofs",
        "course_attr": "fall",
        "semesters": [2]
    },
    3: {
        "dept": "PY",
        "dept_name": "Physics",
        "course_num": "401",
        "course_name": "Quantum 1",
        "course_cred": 3,
        "course_reqs": "",
        "course_desc": "party with dj griffiths",
        "course_attr": "spring",
        "semesters": [1]
    },
}

sections = {
    10001001: {
        "semester": 1,
        "course_id": 1,
        "section": "001",
        "component": "Lec",
        "days": "MWF",
        "time": "10:00am-11:00am",
        "loc": "1000 SAS Hall",
        "prof": "Alina Duca"
    },
    10001002: {
        "semester": 1,
        "course_id": 1,
        "section": "002",
        "component": "Lec",
        "days": "TH",
        "time": "11:00am-12:00pm",
        "loc": "1001 SAS Hall",
        "prof": "Andrew Cooper"
    },
    20001001: {
        "semester": 2,
        "course_id": 1,
        "section": "001",
        "component": "Lec",
        "days": "TH",
        "time": "10:00am-11:00am",
        "loc": "1000 SAS Hall",
        "prof": "Alina Duca"
    },
    20002001: {
        "semester": 2,
        "course_id": 2,
        "section": "001",
        "component": "Lec",
        "days": "MWF",
        "time": "1:00pm-2:00pm",
        "loc": "1002 SAS Hall",
        "prof": "Bevin Maultsby"
    },
    10003001: {
        "semester": 1,
        "course_id": 3,
        "section": "001",
        "component": "Lec",
        "days": "TH",
        "time": "9:00am-10:00am",
        "loc": "100 Riddick Hall",
        "prof": "Albert Young"
    },
}

semesters = {
    1: {"name": "Spring 2019"},
    2: {"name": "Fall 2019"},
}

if __name__ == "__main__":
    main()
