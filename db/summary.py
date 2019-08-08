#!/usr/bin/env python3
import sqlite3

def get_semesters(cursor):
    data = cursor.execute("select id, name from semesters;")
    semesters = dict()
    for row in data:
        semesters[int(row[0])] = {"name": row[1]}
    return semesters

def get_departments(cursor):
    data = cursor.execute("select id, dept, dept_name from departments;")
    departments = dict()
    for row in data:
        departments[int(row[0])] = {"dept": row[1], "dept_name": row[2]}
    return departments

def get_professors(cursor):
    data = cursor.execute("select id, name from professors;")
    professors = dict()
    for row in data:
        professors[int(row[0])] = {"name": row[1]}
    return professors

def __parse_course(row):
    course = dict()
    # row = course_id, dept_id, course_num, course_name, course_cred,
    #       course_reqs, course_desc, course_attr, semesters
    course["dept_id"] = int(row[1])
    course["course_num"] = row[2]
    course["course_name"] = row[3]
    course["course_cred"] = int(row[4])
    course["course_reqs"] = row[5]
    course["course_desc"] = row[6]
    course["course_attr"] = row[7]
    course["semesters"] = [int(s) for s in row[8].split(",")]
    return course

def get_course(cursor, course_id):
    data = cursor.execute(
        "select * from courses where id==?;", (course_id,)
    )
    return __parse_course(next(data))

def get_courses(cursor, course_ids):
    course_ids = set(int(i) for i in course_ids if int(i) > 0)
    course_ids = list(str(i) for i in course_ids)
    data = cursor.execute(
        "select * from courses where id in (%s);" % (",").join(course_ids)
    )
    courses = dict()
    for row in data:
        courses[int(row[0])] = __parse_course(row)
    return courses

def get_dept_courses_count(cursor, dept_id):
    data = cursor.execute(
        "select count(dept_id) from courses where dept_id==?;", (dept_id,)
    )
    return int(next(data)[0])

def get_professor_course_counts(cursor, prof_id):
    data = cursor.execute(
        "select course_id, count(id) from sections where prof_id==? \
        group by course_id;", (prof_id,)
    )
    course_counts = dict()
    for row in data:
        course_counts[int(row[0])] = int(row[1])
    return course_counts

def main():
    # connect to database
    db = sqlite3.connect("courses.db")
    dbc = db.cursor()

    semesters = get_semesters(dbc)
    print("semesters:")
    for i in semesters:
        s = semesters[i]
        print(f"  %2d: {s['name']}" % i)

    departments = get_departments(dbc)
    print("departments:")
    for i in departments:
        d = departments[i]
        n = get_dept_courses_count(dbc, i)
        print(f"  %2d: {d['dept']} - {d['dept_name']}: {n} courses" % i)

    professors = get_professors(dbc)
    print("professors:")
    for i in professors:
        p = professors[i]
        course_counts = get_professor_course_counts(dbc, i)
        courses = get_courses(dbc, course_counts.keys())
        depts = dict()
        for course_id in course_counts:
            dept = departments[courses[course_id]["dept_id"]]["dept"]
            depts[dept] = depts.get(dept, 0) + course_counts[course_id]
        print(f"  %2d: {p['name']}: {depts}" % i)

    # close connection
    db.close()

if __name__ == "__main__":
    main()
