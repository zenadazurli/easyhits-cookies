import subprocess
import time
import re
import os
import ast

API_KEY = os.environ.get("BROWSER_USE_API_KEY", "bu_P3OpQUSfyOTiW5RhGcpqdIkvaPkDWcVCJkY4XlsAD5s")
EMAIL = "sandrominori50+ulugarecexisa@gmail.com"
PASSWORD = "DDnmVV45!!"

def run(cmd, capture=False):
    if capture:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True)
    else:
        subprocess.run(cmd, shell=True)

def js(code):
    run(f'browser-use eval "{code}"')

print("🚀 Login EasyHits4U...")

run(f"browser-use config set api_key {API_KEY}")
run("browser-use cloud connect")
run("browser-use open https://www.easyhits4u.com/logon/")
time.sleep(5)

# Inserisci email
run('browser-use keys "Tab"')
run(f'browser-use type "{EMAIL}"')
time.sleep(1)

# Inserisci password
run('browser-use keys "Tab"')
run(f'browser-use type "{PASSWORD}"')
time.sleep(1)

# Click sul pulsante (selettore preciso)
js("document.querySelector('.modal-overlay-guest .btn_green').click()")
time.sleep(10)

# Cookie
result = run("browser-use cookies get", capture=True)
output = result.stdout

# Parsing robusto
sesids = None
user_id = None
try:
    start = output.find("cookies: [")
    if start != -1:
        bracket_count = 0
        end = start
        for i, ch in enumerate(output[start:], start):
            if ch == '[':
                bracket_count += 1
            elif ch == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    end = i + 1
                    break
        cookies_str = output[start:end]
        cookies_str = cookies_str.replace("cookies: ", "")
        cookies_list = ast.literal_eval(cookies_str)
        for c in cookies_list:
            if c.get('name') == 'sesids':
                sesids = c.get('value')
            if c.get('name') == 'user_id':
                user_id = c.get('value')
except Exception as e:
    print(f"Errore parsing: {e}")

print(f"sesids={sesids}")
print(f"user_id={user_id}")

# Salva su file
if sesids and user_id:
    with open("cookies.txt", "w") as f:
        f.write(f"sesids={sesids}\nuser_id={user_id}")
    print("✅ Cookie salvati in cookies.txt")