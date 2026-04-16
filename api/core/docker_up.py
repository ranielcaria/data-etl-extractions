import subprocess, os, time
from tkinter import messagebox

def run_docker_up(status_var):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'db-testing.docker-compose.yml')
    is_on = status_var.get()
    action = 'up -d' if is_on else 'down'
    label = 'Iniciando' if is_on else 'Parando'

    try:
        subprocess.Popen(f'docker compose -f "{file_path}" {action}', shell=True)
        if is_on:
            time.sleep(3)
            sql = 'CREATE SCHEMA IF NOT EXISTS "pms"; CREATE TABLE IF NOT EXISTS "pms"."example" (example TEXT);'
            docker_sql = f"docker exec testing-db psql -U postgres -d data_etl -c '{sql}'"
            subprocess.Popen(docker_sql, shell=True)

        messagebox.showinfo('Docker', f'{label}: Docker')
    except Exception as error:
        messagebox.showerror('Error Docker', f'Error ao executar: {error}')