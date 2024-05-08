import requests


def read_file(in_file):
    try:
        file = open(in_file, "r")
        return file.read()
    except Exception:
        print("File error, file prob not found")


def get_big_oh(in_file):
    code = read_file(in_file)
    code_payload = {"code": f"{code}"}
    response = requests.post("https://www.bigocalc.com/api/calculate", json=code_payload)
    if response.status_code != 200:
        print(f"failed")
    print(response.text)


if __name__ == '__main__':
    
    file_name = "code.c"
    get_big_oh(file_name)
