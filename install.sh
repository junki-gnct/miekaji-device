#!/bin/bash
sudo apt update
sudo apt -y install screen
sudo apt -y install bluez
sudo apt -y install bluetooth blueman
sudo apt -y install libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev libdbus-glib-1-dev libbluetooth-dev
sudo pip3 install pybluez
sudo pip3 install smbus

RNDSTR=`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 4 | head -n 1`

sudo sh -c "echo 'miekaji-${RNDSTR}' > /etc/hostname"
sudo sh -c "echo '\n127.0.2.1      miekaji-${RNDSTR}\n' >> /etc/hosts"

sudo sed -i -e 's/^ExecStart=\/usr\/lib\/bluetooth\/bluetoothd$/ExecStart=\/usr\/lib\/bluetooth\/bluetoothd -C\nExecStartPost=\/usr\/bin\/sdptool add SP/g' /etc/systemd/system/dbus-org.bluez.service
sudo sed -i -e 's/^ExecStart=\/usr\/lib\/bluetooth\/bluetoothd$/ExecStart=\/usr\/lib\/bluetooth\/bluetoothd -C\nExecStartPost=\/usr\/bin\/sdptool add SP/g' /lib/systemd/system/bluetooth.service