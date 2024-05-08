import requests

account_info = {
    "username": "urMO21m201je",
    "password": "1234568hbd"
}
#login_url = 'http://www.renren.com/PLogin.do' github copilot thing idk
login_url = "https://www.positivephysics.org/user/login"
site_page = "https://www.positivephysics.org/dashboard/physics/velocity?courseID=1&unitID=14&mode=work"


session = requests.Session()
login_post = session.post(login_url, json=account_info)
if login_post.status_code != 200:
    print("Login Failed with status code: ", login_post.status_code)
print("Login Success!")
page_data = session.get(site_page)
print(page_data.text)
