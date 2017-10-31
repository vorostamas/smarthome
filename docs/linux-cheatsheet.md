# Some useful commands for linux/unix users

## .profile contents

The .profile file comes in handy when you want to set user specific environmental variables, and run some basic scripts to help you keep things going for that specific user session. The following script adds `.`  (current folder) to the path, so that when you run any command, it first looks within the current folder first before looking into other folders. 

It also has code to show the IP addresses and hostname when I login,
It also creates an alias `h` for my home assistant config directory. By creating an alias, you can simply run `h` in the console to get to the homeassistant config folder easily.

```
PATH=./:$PATH

echo "---------------------------------------------------------"
echo "                   Welcome, Mahasri Kalavala             "
echo "---------------------------------------------------------"
ips=($(hostname -I))

for ip in "${ips[@]}"
do
    echo "IP Address: " $ip
done
echo "Host name:  " $HOSTNAME

echo "---------------------------------------------------------"

alias h="cd /home/homeassistant/.homeassistant"
alias cls="/usr//bin/clear"
```

After making changes to the .profile file, ensure the file has “execute” permissions. If the file does not have “execute” permissions, it will not execute. To give “execute” permission, you can run the following command in the home directory.

`chmod +x ~/.profile`

You can also explicitly run the .profile file by using the following command

`source ~/.profile`

## Raspberry Pi Basic Setup

If you are setitng up Raspberry Pi for the first time, you may want to:

Run `sudo raspi-config` and set the following:
* Setup Hostname
* Setup Wi-Fi
* Change Default Password
* Set Time Zone
* Set Locale
* Set keyboard
* Set WiFi Country (optional)
* Enable VNC Server (if you want to have remove desktop, if not SSH is fine)

As soon as you set up the commands above, you may want to restart by running `sudo reboot now` and move onto the next steps:

* Run `sudo apt-get update && sudo apt-get upgrade -y` command to update and upgrade

Since some of the updates require disk space, it will ask you to confirm, just type ‘y’ and hit ‘enter’ to continue. It may ask you multiple times depending upon number of packages being updated. Optionally, you can also run the command with ‘-y’ option.

You may also want to update the firmware to ensure you are using the latest one. To update the firmware, run the following command(s) in the same order.

```
sudo apt-get install rpi-update
sudo rpi-update
sudo reboot
```

While you are at it, run the following commands to update the time server and install ca-certificates.
```
sudo apt-get install ca-certificates
sudo apt-get install ntpdate
sudo ntpdate -u ntp.ubuntu.com
```

Optionally, you can run the following command to clean up any packages

```
sudo apt-get clean
```
or

```
sudo apt-get autoremove 
sudo apt-get autoclean
sudo apt-get remove <application_name>
sudo apt-get purge package
```

## Setup Samba - File Sharing

Samba allows you to share folders, and when you are on Windows machines, you will be able to look up RPi by host name.

```
sudo apt-get update
sudo apt-get -y install samba
sudo reboot
```

After installing Samba and rebooting the RPi, you need to set default password and update the configuration file to enable sharing of files. The password is not required, but it is always a good practice to secure folders from unauthorized users.

```
sudo smbpasswd -a pi
```

Make configuration changes by running the command below

```
sudo vi /etc/samba/smb.conf
```

Go to the bottom of the file, and enter the following

```
[Home]
 comment=Home Directory Share
 path=/home
 browseable=Yes
 writeable=Yes
 read only = false
 only guest=no
 create mask=0777
 directory mask=0777
 public=no
```

You can have as many shares as you want. There is virtually no limit on the number of shares.
To restart Samba, execute the following command

```
sudo service smbd restart
```

Run the following command to test and verify the samba configuration
```
testparm 
```

## Restarting Raspberry Pi every night at 4:05 AM

Why 4:05AM? I don't know! You can pick whatever the time you want...

If you are not running anything critical on your Raspberry Pi, and you are okay with it automatically restart every now and then, the following script is for you. I like to restart my RPi every day at 4:05 in the morning. I like the idea of resetting everything back to “normal” on a more frequent basis to run things smoother.

Type the following command in the console 
```
sudo crontab –e
```

And enter the following line 
```
0 4   *   *   *    /sbin/shutdown -r +5
```

What the above lines means, it basically the following:
```
minute hour dayOfMonth Month dayOfWeek commandToRun
```

## Setting up Gstreamer

Run the following command to install GStreamer
```
sudo apt-get install python3-gst-1.0 \
    gir1.2-gstreamer-1.0 gir1.2-gst-plugins-base-1.0 \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly \
    gstreamer1.0-tools
```

Run the following command to link gsp/gi path to HA for Gstreamer to function properly    

BEFORE you run the following command, make sure the path to the virtal environment is correct

```
sudo ln -s /usr/lib/python3/dist-packages/gi /srv/homeassistant/homeassistant_venv/lib/python3.4/site-packages
```


Make sure the homeassistant user is added to the audio group by running the following command.

```
sudo usermod -a -G audio homeassistant
```

## Respberry Pi GPIO Access

If you are using GPIOs on Raspberry Pi, you need to give access to `homeassistant` user to the GPIO. You can do that by running the following command:

```
sudo usermod -G gpio -a homeassistant
```

