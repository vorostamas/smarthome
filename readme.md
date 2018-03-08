## skalavala's Home Automation/Smart Home

Here you will find a bunch of scripts that I use to automate my home.

I have a bunch of Raspberry Pi's, and Pi Zeros at home along with a bunch of "smart" devices of various brands. All these smart devices work great independently but not together. My goal is to bring all of them together and have them talk to each other with a little bit of programming and make them really smarter as a whole! I also want to be able to run all the software on Raspberry Pi's only.

The primary Home Automation software/platform that I use is [Home Assistant](https://home-assistant.io/) (HA). It is an open-source home automation platform written by a bunch of smart individuals. HA allows you to track and control devices easily with simple configuration and with a little bit of scripting, you can do wonders. It is also a perfect piece of software to run entirely on a single Raspberry Pi.

The following picture shows high level architecture of my home network, and what I use for basic automation stuff.
![My Home Automation Setup](https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/smart-home.jpg)

Please feel free to let me know if you find any issues with my code, and/or have any suggestions. Thank you!

## Here is a sample view of my dashboard

<img src="https://github.com/skalavala/smarthome/blob/master/images/skalavala-smarthome-dashboard.jpg" alt="Home Assistat" />

## Custom Components:

### Custom Variables:

I called it `input_label`, it is basically a `label` type component, where you can store any value you want, and can be used in automations, scripts and more. [check out the code here](https://github.com/skalavala/smarthome/blob/master/custom_components/input_label.py). Search for [input_label](https://github.com/skalavala/smarthome/search?utf8=%E2%9C%93&q=input_label) in my repo on how to use it.

### Life360 Custom Component:

The Life360 component uses Life360 API and retrieves information about the circle you created in the same format as OwnTracks. You just ned to setup OwnTracks, and drop-in the custom component, and you are all set!

[Click Here](https://github.com/skalavala/smarthome/blob/master/custom_components/sensor/life360.py) for the Life360 custom component code. Make sure you check out the [Packages](https://github.com/skalavala/smarthome/blob/master/packages/life360.yaml) section on how to use the Life360 Component.

### Palo Alto Component:

I wrote a Palo Alto component to keep an eye on who is logging into my firewall and VPN at home. Below is the screenshot and you can find the code in the `custom_components` folder and corresponding `Packages` folder.

<img src="https://raw.githubusercontent.com/skalavala/smarthome/master/images/paloalto.png"/>
