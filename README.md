# Ping Monitor

![Ping Monitor Screenshot](.docs/screenshot.png)

A simple application to monitor network uptime at home.
This setup starts three docker containers.
Grafana for UI, InfluxDB as storage and a python docker container,
containing a small skript which sends ICMP pings and stores the results in the InfluxDB.

## Metrics

Currently following metrics are supported:
- active: Flag which indicates if a connection was possible
- round_trip_time_max: Longest running ping in a batch
- round_trip_time_min: Shortest running ping in a batch
- round_trip_time_avg: Average RTT for a batch

## Used Libraries

- https://github.com/influxdata/influxdb
- https://github.com/alessandromaggio/pythonping