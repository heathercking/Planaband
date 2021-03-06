from db.run_sql import run_sql
from models.lesson import Lesson

from models.pupil import Pupil
from models.nok import NextOfKin
from models.tutor import Tutor
from models.lesson import Lesson
from models.attendance import Attendance
import repositories.pupil_repository as pupil_repository
import repositories.nok_repository as nok_repository
import repositories.tutor_repository as tutor_repository
import repositories.lesson_repository as lesson_repository



def save(pupil):
    sql = "INSERT INTO pupils (name, dob, instrument, grade, nok_id, notes, active) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [pupil.name, pupil.dob, pupil.instrument, pupil.grade, pupil.nok.id, pupil.notes, pupil.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    pupil.id = id
    return pupil


def select_all():
    pupils = []

    sql = "SELECT * FROM pupils ORDER BY name"
    results = run_sql(sql)

    for row in results:
        nok = nok_repository.select(row['nok_id'])
        pupil = Pupil(row['name'], row['dob'], row['instrument'], row['grade'], nok, row['notes'], row['active'], row['id'])
        pupils.append(pupil)
    return pupils


def select(id):
    pupil = None
    sql = "SELECT * FROM pupils WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        nok = nok_repository.select(result['nok_id'])
        pupil = Pupil(result['name'], result['dob'], result['instrument'], result['grade'], nok, result['notes'], result['active'], result['id'])
    return pupil


def update(pupil):
    sql = "UPDATE pupils SET (name, dob, instrument, grade, nok_id, notes, active) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pupil.name, pupil.dob, pupil.instrument, pupil.grade, pupil.nok.id, pupil.notes, pupil.active, pupil.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM pupils WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM pupils"
    run_sql(sql)


def lessons(pupil):
    lessons = []

    sql = "SELECT lessons.* FROM lessons INNER JOIN attendances ON attendances.lesson_id = lessons.id WHERE pupil_id = %s ORDER BY date"
    values = [pupil.id]
    results = run_sql(sql, values)

    for row in results:
        tutor = tutor_repository.select(row['tutor_id'])
        lesson = Lesson(row['name'], row['date'], row['time'], row['instrument'], tutor, row['max_capacity'], row['group_status'], row['id'])
        lessons.append(lesson)
    return lessons


def attendances(pupil):
    attendances = []

    sql = "SELECT * FROM attendances WHERE pupil_id = %s"
    values = [pupil.id]
    results = run_sql(sql, values)

    for row in results:
        pupil = pupil_repository.select(row['pupil_id'])
        lesson = lesson_repository.select(row['lesson_id'])
        attendance = Attendance(lesson, pupil, row['attended'], row['id'])
        attendances.append(attendance)
    return attendances
