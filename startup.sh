#!/bin/bash
echo $(cd $(dirname $0) && pwd)
sudo mkdir /opt/miekaji/
sudo cp -f ./app/* /opt/miekaji/

sudo chown -R pi:pi /opt/miekaji/
sudo chmod -R a+x /opt/miekaji/

sudo sh -c "echo '
[Unit]
Description=Miekaji Device Service
After=bluetooth.service

[Service]
User=pi
Group=pi
WorkingDirectory=/opt/miekaji
ExecStart=/usr/bin/screen -DmS miekaji /bin/sh /opt/miekaji/run.sh
ExecStop=/bin/sh /opt/miekaji/stop.sh
Restart=always
KillMode=none

[Install]
WantedBy=multi-user.target
' > /etc/systemd/system/miekaji.service"

sudo systemctl enable miekaji
sudo systemctl start miekaji