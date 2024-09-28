import subprocess
import time

def wait_for_postgres(host, max_retires=5, delay_seconds=5):
    retries = 0
    while retries < max_retires:
        try:
            result = subprocess.run(
                [ "pg_isready", "-h", host], check=True capture_output=True, text=True)
            if "accepting connections" in result.stdout:
                print ("Postgres Conectado!")
                return True
        except subprocess.CalledProcessError as e:
            print(f"Erro ao conectar o Postgres: {e}")
            retries += 1
            print(
                f"Tentando Novamente em {delay_seconds} segundos... (Attempt {retries}/{max_retires})")
            time.sleep(delay_seconds)
        print ("Maximo de tentativas Realizadas. Fechando")
            )