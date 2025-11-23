from StudentTable import StudentTable

db = StudentTable("")

user_id = '4'
level = 'Beginner'
education_form = 'personal'
new_education_form = 'group'
subject_id = '6'


def test_create_new_student():
    db.create(user_id, level, education_form, subject_id)
    created_student = db.get_student_by_id(user_id)

    assert len(created_student) > 0, "Запись о студенте не найдена."
    assert created_student[0]['user_id'] == int(user_id)
    assert created_student[0]['level'] == level
    assert created_student[0]['education_form'] == education_form
    assert created_student[0]['subject_id'] == int(subject_id)

    db.delete(user_id)
    result = db.get_student_by_id(user_id)
    assert len(result) == 0


def test_change_education_form():
    db.create(user_id, level, education_form, subject_id)
    created_student = db.get_student_by_id(user_id)

    assert len(created_student) > 0, "Запись о студенте не найдена."
    assert created_student[0]['user_id'] == int(user_id)
    assert created_student[0]['level'] == level
    assert created_student[0]['education_form'] == education_form
    assert created_student[0]['subject_id'] == int(subject_id)

    db.change_education_form(user_id, new_education_form)
    changed_student = db.get_student_by_id(user_id)

    assert len(changed_student) > 0, (
        "Запись о студенте не найдена"
        " после изменения формы образования."
    )
    assert changed_student[0]['user_id'] == int(user_id)
    assert changed_student[0]['level'] == level
    assert (changed_student[0]['education_form'] ==
            new_education_form)
    assert changed_student[0]['subject_id'] == int(subject_id)

    db.delete(user_id)
    rows = db.get_student_by_id(user_id)
    assert len(rows) == 0


def test_delete():
    db.create(user_id, level, education_form, subject_id)
    created_student = db.get_student_by_id(user_id)

    assert len(created_student) > 0, "Запись о студенте не найдена."
    assert created_student[0]['user_id'] == int(user_id)
    assert created_student[0]['level'] == level
    assert created_student[0]['education_form'] == education_form
    assert created_student[0]['subject_id'] == int(subject_id)

    deleted_student = db.delete(user_id)
    assert deleted_student["detail"] == "Student successfully deleted"

    rows = db.get_student_by_id(user_id)
    assert len(rows) == 0
