FROM grafana/grafana:latest

COPY datasource.yml /etc/grafana/provisioning/datasources
COPY dashboard.yml /etc/grafana/provisioning/dashboards
COPY dashboards/* /etc/grafana/provisioning/dashboards