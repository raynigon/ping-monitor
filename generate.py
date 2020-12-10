import secrets
import string

def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    return password

hosts = "1.1.1.1"
lines = [
    f"INFLUXDB_USERNAME=admin\n",
    f"INFLUXDB_PASSWORD={generate_password()}\n"
    f"INFLUXDB_DATABASE=network\n",
    f"GRAFANA_USERNAME=admin\n",
    f"GRAFANA_PASSWORD={generate_password()}\n",
    f"PING_HOSTS={hosts}\n"
]

print(f"Configured to ping {hosts}")
print("Edit PING_HOSTS variable in .env file to change that (e.g. '1.1.1.1,google.com')\n")
print("Run `docker-compose up --build` to get started")

with open(".env", "w") as file:
    file.writelines(lines)
    