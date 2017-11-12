---
layout: page
title: DIY USB Camera & Raspberry Pi
description: The article below explains how you can use USB based camera and integrate with Home Assistant
---

# USB Camera 


After installing Raspbian Operating System on your Raspberry Pi, connect USB camera to Raspberry Pi and run the following command. 

```
lsusb
```

The above command shows you a list of USB devices connected to your Raspberry Pi. If you see the camera there, you are good to go. If you don't your camera may not be supported.

Now that you know the camera is recognized by your Raspberry Pi, it is timeto install software. The sofware that is commonly used is called `Motion`. To install, run the command.

```
sudo apt-get install motion
```

After the installation, you need make a few modifications to the settings, and the configuration settings for `motion` is in `/etc/motion/motion.conf` file. So, go ahead and open the file.

*    Make sure `daemon` is ON.
*    Set `framerate` anywhere in between 1000 to 1500.
*    Keep `stream_port` to 8081.
*    `stream_quality` should be 100.
*    Change `stream_localhost` to OFF.
*    Change `webcontrol_localhost` to OFF.
*    Set `quality` to 100.
*    Set `width` & `height` to 640 & 480.
*    Set `post_capture` to 5.

Save and exit the file.


After making changes, you also need to makechanges to one more file. Type in the command 'sudo nano /etc/default/motion ' and press enter.

```
sudo vi /etc/default/motion
``` 

*   Set ' start_motion_daemon ' to yes. Save and exit.

Use the folowing commands to start, stop, and restart `motion` service. 

To start `motion` service, run the following command.
```
sudo service motion start
```

To stop `motion` service, run the following command.
```
sudo service motion stop
```

To restart `motion` service, run the following command.
```
sudo service motion restart
```

To check the status of `motion` service, run the following command:

```
sudo systemctl status motion
```

After running the service using `sudo motion`, if you run into any errors, it may be the permissions error. See Permissions section below.

## Checking the Images:

Go to the ip address of the Raspberry Pi, and access the url as below:

```
http://192.168.x.xxx:8081
```

The port number `8081` can be changed to whatever you need. It is specified in the `/etc/motion/motion.conf` file.

## Permissions

The `motion` service requires write access to several folders. The service also runs under user `motion` and group `motion`. Make sure you give the following folders access by running the command.

```
sudo chown motion:motion /var/run/motion
sudo chown motion:motion /var/log/motion
sudo chown motion:motion /var/log/motion/motion.log
```


If everything runs as expected, enjoy!