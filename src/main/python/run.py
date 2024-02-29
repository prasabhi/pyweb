# run.py
from concurrent.futures import ThreadPoolExecutor
from subprocess import Popen

def run_web_app():
    web_app_process = Popen(['python', 'app.py'])

def run_microservice():
    microservice_process = Popen(['python', 'microservice.py'])

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(run_web_app)
        executor.submit(run_microservice)
