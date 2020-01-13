FROM grafana/grafana:latest


COPY datasource.yml /etc/grafana/provisioning/datasources
COPY dashboard.yml /etc/grafana/provisioning/dashboards/dashboard.yml
COPY dashboards/ping.json /etc/grafana/provisioning/dashboards/ping/ping.json