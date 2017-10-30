# Autorun services

The following are the services that run automatically during startup.

## The HomeBridge Service
The homebridge.service in `/etc/systemd/system/` folder, and the contents are:

```
[Unit]
Description=Homebridge
BindsTo=home-assistant.service
After=home-assistant.service

[Service]
Type=simple
User=homeassistant
ExecStartPre=/bin/sleep 60
ExecStart=/usr/bin/homebridge -U /home/mahasri/.homebridge/
RestartSec=10
Restart=on-failure
```

## The home-assistant Service

The file is in `/etc/systemd/system/` folder, and the contents are:

```
[Unit]
Description=Home Assistant
Wants=mosquitto.service homebridge.service
Before=homebridge.service
After=network.target mosquitto.service

[Service]
Type=simple
User=%i
ExecStart=/srv/homeassistant/bin/hass -c "/home/homeassistant/.homeassistant"

[Install]
WantedBy=multi-user.target
```

## Mosquitto Service

The mosquitto.service file will be in either`/etc/systemd/system` or `/lib/systemd/system` folder

```
[Unit]

Description=Mosquitto MQTT Broker daemon
ConditionPathExists=/etc/mosquitto/mosquitto.conf
After=network.target
Requires=network.target

[Service]
Type=forking
RemainAfterExit=no
StartLimitInterval=0
PIDFile=/run/mosquitto.pid
ExecStart=/usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf -d
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target
```
