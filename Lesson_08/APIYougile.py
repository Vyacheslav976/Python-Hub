import requests


class YougileApi:

    def __init__(self, url):
        self.url = url

# Получение ID компании
#     def get_ID_company(self, login, password):
#         data = {'login': login, 'password': password}
#         headers = {'Content-Type': 'application/json'}
#         resp = requests.post(self.url + '/api-v2/auth/companies',
#                              json=data, headers=headers)
#         return resp

# Функция, которая создаёт ключ и возвращает его
#     def create_key(self, login, password, id_company):
#         data = {'login': login, 'password': password, 'companyId': id_company}
#         headers = {'Content-Type': 'application/json'}
#         resp = requests.post(self.url + '/api-v2/auth/keys',
#                              json=data, headers=headers)
#         return resp
# Получение существующих ключей
    def get_existing_keys(self, login, password, id_company):
        data = {
            "login": login,
            "password": password,
            "companyId": id_company
        }
        headers = {'Content-Type': 'application/json'}
        resp = requests.post(self.url + '/api-v2/auth/keys/get',
                             json=data, headers=headers)
        return resp

# Создание проекта
    def create_project(self, title_project, token_company):
        headers = {'Authorization': "Bearer " + token_company,
                   'Content-Type': 'application/json'}
        data = {'title': title_project}

        resp = requests.post(self.url + '/api-v2/projects',
                             json=data, headers=headers)
        return resp

# Изменение проекта по ID
    def change_project_id(self, id_project, token_company, new_title_project):
        headers = {'Authorization': "Bearer " + token_company,
                   'Content-Type': 'application/json'}
        body = {'deleted': True, 'title': new_title_project}

        resp = requests.put(self.url + '/api-v2/projects/' + id_project,
                            json=body, headers=headers)
        return resp

# Получение проекта по ID
    def get_project_id(self, id_project, token_company):
        headers = {'Authorization': "Bearer " + token_company,
                   'Content-Type': 'application/json'}

        resp = requests.get(self.url + '/api-v2/projects/' + id_project,
                            headers=headers)
        return resp
