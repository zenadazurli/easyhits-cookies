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

# ASPETTA CHE TURNSTILE SIA RISOLTO (campo cf-turnstile-response con valore)
print("⏳ Attesa risoluzione Turnstile...")
run('browser-use wait selector "input[name=\'cf-turnstile-response\']"')
run('browser-use wait 2')
run('browser-use eval "document.querySelector(\'input[name=\\\'cf-turnstile-response\\\']\')?.value"')

# CLICK SUL PULSANTE
print("🔑 Click su Enter...")
js("document.querySelector('button.btn_green').click()")

# ASPETTA LA DASHBOARD
print("⏳ Attesa redirect...")
for i in range(30):
    time.sleep(1)
    url_result = run("browser-use eval 'window.location.href'", capture=True)
    url = url_result.stdout.strip()
    if "account" in url or "surf" in url:
        print("✅ Dashboard raggiunta!")
        break

# Cookie
result = run("browser-use cookies get", capture=True)
output = result.stdout

# Parsing
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
