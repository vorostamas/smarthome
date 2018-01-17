## Welcome

Here you will find a bunch of scripts that I use to automate my home.

I have a bunch of Raspberry Pi's, and Pi Zeros at home along with a bunch of "smart" devices of various brands. All these smart devices work great independently but not together. My goal is to bring all of them together and have them talk to each other with a little bit of programming and make them really smarter as a whole! I also want to be able to run all the software on Raspberry Pi's only.

The primary Home Automation software/platform that I use is [Home Assistant](https://home-assistant.io/) (HA). It is an open-source home automation platform written by a bunch of smart individuals. HA allows you to track and control devices easily with simple configuration and with a little bit of scripting, you can do wonders. It is also a perfect piece of software to run entirely on a single Raspberry Pi.

The following picture shows high level architecture of my home network, and what I use for basic automation stuff.
![My Home Automation Setup](https://raw.githubusercontent.com/skalavala/skalavala.github.io/master/images/smart-home.jpg)

Please feel free to let me know if you find any issues with my code, and/or have any suggestions. Thank you!

## My Smart Devices

<p>
The following are some of the smart devices that I use for my current Smart Home setup. Please feel free to reach out to me or check my repository on how to configure them,
</p>

<table>
  <tr>
    <td>Aeltec Multi Sensor</td>
    <td>Wemo Light Switches</td>
    <td>TP-Link HS-200 Smart Switches</td>
    <td>ETekcity RF Outlets</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/gp/product/B00S68NUSW/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=704831c7baba3b21178df5de167c6126" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00S68NUSW&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00S68NUSW" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B00DGEGJ02/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=skalavala-20&linkId=c0bcc93aef46d79faf589f9cec082e3a" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00DGEGJ02&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00DGEGJ02" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B01EZV35QU/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=skalavala-20&linkId=d7e1abad6128911404b87e5f5349bba2" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01EZV35QU&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01EZV35QU" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/Etekcity-Wireless-Electrical-Household-Appliances/dp/B00DQELHBS/ref=as_li_ss_il?s=hi&ie=UTF8&qid=1494177162&sr=1-4&keywords=etekcity&linkCode=li2&tag=skalavala-20&linkId=4620077874a3abdc2d21ddb27f084a0e" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00DQELHBS&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00DQELHBS" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
  </tr>
  <tr>
    <td>Lifx Light Bulbs</td>
    <td>Lifx LED Strip</td>
    <td>Phlips Hue Bulbs</td>
    <td>Philips Hue Hub &amp Bulbs Set</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/LIFX-Smart-Multicolor-Dimmable-Amazon/dp/B0161IJ5F0/ref=as_li_ss_il?s=hi&ie=UTF8&qid=1494176853&sr=1-4&keywords=lifx&linkCode=li2&tag=skalavala-20&linkId=62e9d31c7814f4156b3bd47a88fa0d9b" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0161IJ5F0&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B0161IJ5F0" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/LIFX-Adjustable-Multicolor-Dimmable-Assistant/dp/B01KY02NLY/ref=as_li_ss_il?_encoding=UTF8&pd_rd_i=B01KY02NLY&pd_rd_r=6MW1N3DVWJ4SJZ0VE17Q&pd_rd_w=LN1kT&pd_rd_wg=bzct6&psc=1&refRID=6MW1N3DVWJ4SJZ0VE17Q&linkCode=li2&tag=skalavala-20&linkId=42ee0bde17f89751e2bf6edbb2edca47" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01KY02NLY&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01KY02NLY" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B01M9AU8MB/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=2c3fce363561246967ff89cceb427722" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01M9AU8MB&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01M9AU8MB" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/Philips-Ambiance-Equivalent-Compatible-Assistant/dp/B07351P1JK/ref=as_li_ss_il?_encoding=UTF8&pd_rd_i=B07351P1JK&pd_rd_r=C3B05NR08TWTNN8W4MDV&pd_rd_w=0zgkI&pd_rd_wg=sZ7W6&psc=1&refRID=C3B05NR08TWTNN8W4MDV&linkCode=li2&tag=skalavala-20&linkId=a7084b413a51c3f36a1198c37fdca7af" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07351P1JK&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B07351P1JK" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
  </tr>
  
  <tr>
    <td>Denon Receiver</td>
    <td>Hik-Vision Bullet IP Cameras</td>
    <td>8-port PoE Switch</td>
    <td>Nest 4th Gen Thermostat</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/Denon-AVR-X2400H-Command-Receiver-Technology/dp/B0725YKHXW/ref=as_li_ss_il?ie=UTF8&qid=1499361830&sr=8-2&keywords=AVRX2400H&linkCode=li2&tag=skalavala-20&linkId=a5420ca45122ba8eea7652549d5fa162" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0725YKHXW&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B0725YKHXW" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B06W55J5MC/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=a93709f97d8788946f2881194ad4a58c" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B06W55J5MC&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B06W55J5MC" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B00HXT8QSO/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=d8d4700e96729069dbe3026efa0778a5" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00HXT8QSO&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00HXT8QSO" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/Nest-Thermostat-Temperature-Stainless-Generation/dp/B0131RG6VK/ref=as_li_ss_il?s=electronics&ie=UTF8&qid=1516148298&sr=1-1&keywords=nest+thermostat+4th+generation&linkCode=li2&tag=skalavala-20&linkId=56b02d084b529ff5d6726411e4af0dc1" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0131RG6VK&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B0131RG6VK" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
  </tr>

  <tr>
    <td>Ecobee4 Thermostat</td>
    <td>Ecobee4 Room Sensors</td>
    <td>SimpliSafe Home Security System</td>
    <td>Ring Doorbell Pro</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/ecobee4-Alexa-Enabled-Thermostat-Sensor-Amazon/dp/B06W2LQY6L/ref=as_li_ss_il?s=electronics&ie=UTF8&qid=1516148354&sr=1-1-spons&keywords=ecobee4&psc=1&linkCode=li2&tag=skalavala-20&linkId=450de6e15a79c2402b618bf579c75df5" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B06W2LQY6L&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B06W2LQY6L" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/ecobee-Room-Sensor-Pack-Stands/dp/B00NXRYOIQ/ref=as_li_ss_il?ie=UTF8&qid=1499361927&sr=8-1&keywords=ecobee+sensor&linkCode=li2&tag=skalavala-20&linkId=200046e52f9f4842d4fab5957d4b4f1b" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00NXRYOIQ&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00NXRYOIQ" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/SimpliSafe-Wireless-Security-Command-Bravo/dp/B01N0DVLRD/ref=as_li_ss_il?ie=UTF8&qid=1494176783&sr=8-2&keywords=simplisafe&th=1&linkCode=li2&tag=skalavala-20&linkId=1678a824ed4f5f7ed7d8a3f24dae8c87" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01N0DVLRD&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01N0DVLRD" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/Ring-88LP000CH000-Video-Doorbell-Pro/dp/B01DM6BDA4/ref=as_li_ss_il?ie=UTF8&qid=1494176823&sr=8-1&keywords=ring+doorbell+pro&linkCode=li2&tag=skalavala-20&linkId=2affe069ee8322ded7f7690860ddc44c" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01DM6BDA4&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01DM6BDA4" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
  </tr>


  <tr>
    <td>Aeotec ZWave Stick</td>
    <td>Aeotec ZWave Multi Sensors (6 in 1)</td>
    <td>Aetec Garage Door Tilt Sensors</td>
    <td>Aeotec Door &amp; Window Sensors</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/Aeotec-Z-Stick-Z-Wave-create-gateway/dp/B00X0AWA6E/ref=as_li_ss_il?s=electronics&ie=UTF8&qid=1516148522&sr=1-1-spell&keywords=zwave+aeotecStick&linkCode=li2&tag=skalavala-20&linkId=3f883f9ceb134c73c9e8133fa1379591" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00X0AWA6E&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00X0AWA6E" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B0151Z8ZQY/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=af4d9d741b44bfaf02bf7aab83129d12" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B0151Z8ZQY&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B0151Z8ZQY" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B01MRZB0NT/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=5bab4a1c766c31f9370fe591967921de" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01MRZB0NT&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01MRZB0NT" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B01N5HB4U5/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=6e967cfca61ba655357c2395a5ff3857" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01N5HB4U5&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01N5HB4U5" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
  </tr>


  <tr>
    <td>Leeo Smoke and CO Alarm Detector</td>
    <td>Motion Sensor Switches</td>
    <td>Bluetooth Speakers</td>
    <td>Rasberry Pi-3s</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/gp/product/B00XMX4GUC/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=b9e14086fcd7b8500533507cee843c05" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00XMX4GUC&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00XMX4GUC" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B00L43RTSS/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=8fa4d24115f5eaa10422021a70ec8a54" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00L43RTSS&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00L43RTSS" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B010OYASRG/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=7db9e0a9e57ced3cb0bafa6b5c50f041" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B010OYASRG&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B010OYASRG" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/Raspberry-Single-Computer-Performance-Heatsink/dp/B01CMC50S0/ref=as_li_ss_il?s=electronics&ie=UTF8&qid=1494177248&sr=1-8&keywords=raspberry+pi3&linkCode=li2&tag=skalavala-20&linkId=d18e25dd97cad2fe37300d4ef0006358" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B01CMC50S0&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B01CMC50S0" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
  </tr>

  <tr>
    <td>RF Transceivers</td>
    <td>Garage Relays</td>
    <td>ESP 8266/Node MCU</td>
    <td>Relays</td>
  </tr>
  <tr>
    <td><a href="https://www.amazon.com/gp/product/B00HEDRHG6/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=420320f78ea70ed4616ac0e923402474" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00HEDRHG6&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00HEDRHG6" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B00ER6MH22/ref=as_li_ss_il?ie=UTF8&psc=1&tag=&linkCode=li2&tag=skalavala-20&linkId=c7bf874c4c03275eefa879d113491550" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00ER6MH22&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00ER6MH22" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/gp/product/B010O1G1ES/ref=as_li_ss_il?ie=UTF8&psc=1&linkCode=li2&tag=skalavala-20&linkId=11090ba0f83b9d7af2089f6b283d7bb6" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B010O1G1ES&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B010O1G1ES" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
    <td><a href="https://www.amazon.com/Tolako-Arduino-Indicator-Channel-Official/dp/B00VRUAHLE/ref=as_li_ss_il?s=electronics&ie=UTF8&qid=1494177346&sr=1-3&keywords=1+channel+relay&linkCode=li2&tag=skalavala-20&linkId=7903186dacc438feea3eaa46296e57b3" target="_blank"><img border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00VRUAHLE&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=skalavala-20" ></a><img src="https://ir-na.amazon-adsystem.com/e/ir?t=skalavala-20&l=li2&o=1&a=B00VRUAHLE" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /></td>
  </tr>

</table>

* Custom Built Smart outlet - where I used a PiZero and relay switch to turn ON/OFF the electrical outlet. I made a small wooden box to house all the items. It is a poor man's version of smart electrical outlet, but a very smart one, and I have more control over this outlet than the commercial smart outlets.


## Here is a sample view of my dashboard

<img src="https://github.com/skalavala/smarthome/blob/master/images/skalavala-smarthome-dashboard.jpg" alt="Home Assistat" />
