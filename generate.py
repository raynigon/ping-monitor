import secrets
import string

def generate_password()
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(20))
    return password


lines = [
    f"INFLUXDB_USERNAME=admin\n",
    f"INFLUXDB_PASSWORD={generate_password()}\n"
    f"INFLUXDB_DATABASE=network\n",
    f"GRAFANA_USERNAME=admin\n",
    f"GRAFANA_PASSWORD={generate_password()}\n"
]
with open(".env", "w"):
    