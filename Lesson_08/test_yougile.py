from APIYougile import YougileApi

api = YougileApi("https://ru.yougile.com")
login = 'volkovs976@rambler.ru'
password = 'volkovs976@rambler.ru'
id_company = 'd3207efd-dea6-406d-a320-6bc7778753ce'
title_project = 'SkyPro'
new_title_project = 'SkyPro_new'
users = {}


def test_positive_create_project():
# 1. получить токен
    token_company_response = api.create_key(login, password, id_company)

    assert token_company_response.status_code == 201, (
        f"Failed to get token:{token_company_response.status_code}"
        f" - {token_company_response.text}"
    )
    token_company = token_company_response.json()["key"]

# 2. Создать проект
    create_project_response = api.create_project(title_project, token_company)

    assert create_project_response.status_code == 201, (
        f"Failed to create project: {create_project_response.status_code}"
        f" - {create_project_response.text}"
    )
    id_project = create_project_response.json()["id"]

    assert len(id_project) > 0, "Project ID should not be empty"

def test_negative_create_project():
    token_company = 'none-key-company'
    create_project_response = api.create_project(title_project, token_company)

    assert create_project_response.status_code == 401, (
        f"Failed to create project: {create_project_response.status_code}"
        f" - {create_project_response.json().get("error")}"
    )
    response_json = create_project_response.json()
    error_message = response_json.get('error', 'Неизвестная ошибка')

    # Проверяем наличие поля "error"
    assert 'error' in response_json, "Project created sucssesfully"
    assert 'id' not in response_json, "Project created sucssesfully"
    assert len(error_message) > 0, "Message should not be empty"

def test_positive_change_project_id():
    token_company_response = api.create_key(login, password, id_company)

    assert token_company_response.status_code == 201, (
        f"Failed to get token: {token_company_response.status_code}"
        f" - {token_company_response.text}"
    )
    token_company = token_company_response.json()["key"]
    create_project_response = api.create_project(title_project, token_company)

    assert create_project_response.status_code == 201, (
        f"Failed to create project: {create_project_response.status_code}"
        f" - {create_project_response.text}"
    )
    id_project = create_project_response.json()["id"]
    assert len(id_project) > 0, "Project ID should not be empty"

# 2. изменить название проекта по ID
    change_project_id_response = api.change_project_id(id_project, token_company, new_title_project)

    assert change_project_id_response.status_code == 200,(
        f"Failed to change project by ID: {change_project_id_response.status_code}"
        f" - {change_project_id_response.text}")

    response_json = change_project_id_response.json()
    assert 'id' in response_json

    id_changed_project = change_project_id_response.json()["id"]
    assert id_changed_project == id_project

def test_negative_change_project_id():
    token_company_response = api.create_key(login, password, id_company)

    assert token_company_response.status_code == 201, (
        f"Failed to get token: {token_company_response.status_code}"
        f" - {token_company_response.text}"
    )
    token_company = token_company_response.json()["key"]

# изменить название проекта
    id_project = 'none-project-id'
    change_project_id_response = api.change_project_id(id_project, token_company, new_title_project)

    assert change_project_id_response.status_code == 404, (
        f"Expected status code - 404, but  : {change_project_id_response.status_code}"
        f"{change_project_id_response.json().get("error")}"
    )
    response_json = change_project_id_response.json()
    error_message = response_json.get("error")
    assert 'error' in response_json, "Project created sucssesfully"
    assert 'id' not in response_json, "Project created sucssesfully"
    assert len(error_message) > 0, "Message should not be empty"

def test_positive_get_project_id():
    token_company_response = api.create_key(login, password, id_company)

    assert token_company_response.status_code == 201, (
        f" Failed to get token: {token_company_response.status_code}"
        f" - {token_company_response.text}"
    )
    token_company = token_company_response.json()["key"]

    create_project_response = api.create_project(title_project, token_company)

    assert create_project_response.status_code == 201, (
        f"Failed to create project: {create_project_response.status_code}"
        f" - {create_project_response.text}"
    )
    id_project = create_project_response.json()["id"]

# 2. Получить инфу проекта по ID
    get_project_id_response = api.get_project_id(id_project, token_company)

    assert get_project_id_response.status_code == 200, (
        f"Ошибка получения проекта: {get_project_id_response.status_code}"
        f" - {get_project_id_response.text}"
    )
    get_title = get_project_id_response.json()['title']
    assert get_title == title_project


def test_negative_get_project_id():
    token_company_response = api.create_key(login, password, id_company)

    assert token_company_response.status_code == 201, (
        f"Ошибка получения токена: {token_company_response.status_code}"
        f" - {token_company_response.text}"
    )
    token_company = token_company_response.json()["key"]

# 2. Получить информацию проекта по ID
    id_project = 'none-project-id'
    get_project_id_response = api.get_project_id(id_project, token_company)

    assert get_project_id_response.status_code == 404, (
            f"Expected status code - 404, but: {get_project_id_response.status_code}"
            f"{get_project_id_response.json().get("error")}"
    )
    status_code = get_project_id_response.status_code
    response_json = get_project_id_response.json()
    error_message = response_json.get("error")

    assert 'error' in response_json, "Project created sucssesfully"
    assert 'id' not in response_json, "Project created sucssesfully"
    assert len(error_message) > 0, "Message should not be empty"