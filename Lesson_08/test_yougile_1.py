from APIYougile import YougileApi

api = YougileApi("https://ru.yougile.com")
login = 'volkovs976@rambler.ru'
password = 'volkovs976@rambler.ru'
id_company = 'd3207efd-dea6-406d-a320-6bc7778753ce'
title_project = 'SkyPro'
new_title_project = 'SkyPro_new'
users = {}


def test_positive_create_project():
    try:
# 1. получить токен
        token_company_response = api.create_key(login, password, id_company)

        if token_company_response.status_code == 201:
            token_company = token_company_response.json()["key"]
            print(f"Токен успешно получен: {token_company[:10]}...")
        else:
            print(f"Ошибка получения токена:"
                  f" {token_company_response.status_code}"
                  f" - {token_company_response.text}")
            return False

# 2. Создать проект
        create_project_response = api.create_project(title_project, token_company)

        if create_project_response.status_code == 201:
            id_project = create_project_response.json()["id"]
            print(f"Проект успешно создан с ID: {id_project}")
        else:
            print(f"Ошибка создания проекта:"
                  f" {create_project_response.status_code}"
                  f" - {create_project_response.text}")
            return False

        assert len(id_project) > 0, "ID  не может быть отрицательным"

        print("Тест test_positive_create_project пройден успешно!")
        return True

    except Exception as e:
        print(f"Произошла ошибка в test_positive_create_project: {str(e)}")
        return False

def test_negative_create_project():
    try:
        token_company = 'none-key-company'
        create_project_response = api.create_project(title_project, token_company)

        if create_project_response.status_code == 401:
            status_code = create_project_response.status_code
            error_message = create_project_response.json().get("error")
            print(f"Проект не был создан. Статус-код:: {status_code}"
                  f"Произошла ошибка авторизации: {error_message}")
        else:
            print(f"Ожидался статус 401, но получен {create_project_response.status_code}")
            return False

        print("Тест test_negative_create_project пройден успешно!")
        return True

    except Exception as e:
        print(f"Произошла ошибка в test_negative_create_project: {str(e)}")
        return False

def test_positive_change_project_id():
    try:
        token_company_response = api.create_key(login, password, id_company)

        if token_company_response.status_code == 201:
            token_company = token_company_response.json()["key"]
            print(f"Токен успешно получен: {token_company[:10]}...")
        else:
            print(f"Ошибка получения токена:"
                  f" {token_company_response.status_code}"
                  f" - {token_company_response.text}")
            return False

        create_project_response = api.create_project(title_project, token_company)

        if create_project_response.status_code != 201:
            print(f"Ошибка создания проекта: "
                  f"{create_project_response.status_code}"
                  f" - {create_project_response.text}")
            return False

        assert create_project_response.status_code == 201

        id_project = create_project_response.json()["id"]
        print(f"Проект успешно создан с ID: {id_project}")

# 2. изменить название проекта по ID
        change_project_id_responce = api.change_project_id(id_project, token_company, new_title_project)

        if change_project_id_responce.status_code == 200:
            status_code = change_project_id_responce.status_code
            print(f"Проект успешно изменен. Статус-код:{status_code}")
        else:
            print(f"Ошибка изменения названия проекта:"
            f" {change_project_id_responce.status_code} -"
            f" {change_project_id_responce.text}")
            return False

        response_json = change_project_id_responce.json()
        assert 'id' in response_json

        id_changed_project = change_project_id_responce.json()["id"]
        assert id_changed_project == id_project

        print("Тест test_positive_change_project_id пройден успешно!")
        return True

    except Exception as e:
        print(
            f"Произошла ошибка в test_positive_change_project_id: {str(e)}")
        return False

def test_negative_change_project_id():
    try:
        token_company_response = api.create_key(login, password, id_company)

        if token_company_response.status_code == 201:
            token_company = token_company_response.json()["key"]
            print(f"Токен успешно получен: {token_company[:10]}...")
        else:
            print(f"Ошибка получения токена:"
                  f" {token_company_response.status_code}"
                  f" - {token_company_response.text}")
            return False

        # изменить название проекта
        id_project = 'none-project-id'
        change_project_id_responce = api.change_project_id(id_project, token_company, new_title_project)

        if change_project_id_responce.status_code == 404:
            status_code = change_project_id_responce.status_code
            error_message = change_project_id_responce.json().get("error")
            print(f"Проект не был изменен."
                  f" Статус-код:{status_code}. "
                  f"Произошла ошибка: {error_message}")
        else:
            print(f" Ожидался статус 404, "
                  f"но получен {change_project_id_responce}")
            return False

        response_json = change_project_id_responce.json()

        assert 'id' not in response_json
        assert 'error' in response_json

        print("Тест test_negative_change_project_id пройден успешно!")
        return True

    except Exception as e:
        print(
            f"Произошла ошибка в test_negative_change_project_id: {str(e)}")
        return False

def test_positive_get_project_id():
    try:
        token_company_response = api.create_key(login, password, id_company)

        if token_company_response.status_code == 201:
            token_company = token_company_response.json()["key"]
            print(f"Токен успешно получен: {token_company[:10]}...")
        else:
            print(f"Ошибка получения токена:"
                  f" {token_company_response.status_code}"
                  f" - {token_company_response.text}")
            return False

        create_project_response = api.create_project(title_project, token_company)

        if create_project_response.status_code != 201:
            print(f"Ошибка создания проекта: "
                  f"{create_project_response.status_code}"
                  f" - {create_project_response.text}")
            return False

        assert create_project_response.status_code == 201

        id_project = create_project_response.json()["id"]
        print(f"Проект успешно создан с ID: {id_project}")

# 2. Получить инфу проекта по ID
        get_project_id_responce = api.get_project_id(id_project, token_company)

        if get_project_id_responce.status_code == 200:
            status_code = get_project_id_responce.status_code
            print(f"Информация о проекте успешно получена."
                  f" Статус-код:{status_code}")
            get_title = get_project_id_responce.json()['title']
            assert get_title == title_project
        else:
            print(f"Ошибка получения проекта:"
                  f" {get_project_id_responce.status_code}"
                  f" - {get_project_id_responce.text}")
            return False

        print("Тест test_positive_get_project_id пройден успешно!")
        return True

    except Exception as e:
        print(
            f"Произошла ошибка в test_positive_get_project_id: {str(e)}")
        return False

def test_negative_get_project_id():
    try:
        token_company_response = api.create_key(login, password, id_company)

        if token_company_response.status_code == 201:
            token_company = token_company_response.json()["key"]
            print(f"Токен успешно получен: {token_company[:10]}...")

        else:
            print(f"Ошибка получения токена:"
                  f" {token_company_response.status_code}"
                  f" - {token_company_response.text}")
            return False

# 2. Получить инфу проекта по ID
        id_project = 'none-project-id'
        get_project_id_responce = api.get_project_id(id_project, token_company)

        if get_project_id_responce.status_code == 404:
            status_code = get_project_id_responce.status_code
            error_message = get_project_id_responce.json().get("error")
            print(f"Информация о проекте не была получена."
                  f" Статус-код:{status_code}. "
                  f"Произошла ошибка: {error_message}")
        else:
            print(f" Ожидался статус 404, "
                  f"но получен {get_project_id_responce}")
            return False

        response_json = get_project_id_responce.json()

        assert 'title' not in response_json
        assert 'error' in response_json

        print("Тест test_negative_get_project_id пройден успешно!")
        return True

    except Exception as e:
        print(
            f"Произошла ошибка в test_negative_get_project_id: {str(e)}")
        return False