import requests


def check_login(login: str, password: str):
    data = f'{{ "login": "{login}", "password": "{password}" }}'
    r = requests.post('http://127.0.0.1:8000/readers/login', data=data)
    answer = r.json()
    
    return answer

    
