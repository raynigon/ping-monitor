from influxdb import InfluxDBClient
import pythonping
import time
import datetime
import os


def create_client():
    influx_host = os.getenv("INFLUXDB_HOST", "localhost")
    influx_port = int(os.getenv("INFLUXDB_PORT", 8086))
    influx_user = os.getenv("INFLUXDB_USERNAME", "admin")
    influx_password = os.getenv("INFLUXDB_PASSWORD", "admin")
    influx_database = os.getenv("INFLUXDB_DATABASE", "rpi")
    
    client = InfluxDBClient(influx_host, influx_port, influx_user, influx_password, influx_database)
    client.create_database(influx_database)
    return client

def create_fields(r: pythonping.executor.ResponseList):
    if r is None:
        return {
            "active": 0
        }
    active = 0
    if r.success(option=pythonping.executor.SuccessOn.Most):
        active = 1
    return {
        "active": active,
        "round_trip_time_max": float(r.rtt_avg*1000),
        "round_trip_time_min": float(r.rtt_min*1000),
        "round_trip_time_avg": float(r.rtt_avg*1000)
    }


def ping_and_save():
    fields = {}
    try:
        r = pythonping.ping('raynigon.de')
    except Exception as e:
        r = None
    client.write_points([
        {
            "measurement": "network_ping",
            "tags": {},
            "time": datetime.datetime.utcnow().isoformat(),
            "fields": create_fields(r)
        }
    ])

while True:
    try:
        client = create_client()
        break
    except Exception as e:
        print(e)
        time.sleep(5)

while True:
    ping_and_save()
    time.sleep(5)
