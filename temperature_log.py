#!/usr/bin/python

from datetime import datetime

temp = open("/sys/devices/platform/sunxi-i2c.0/i2c-0/0-0034/temp1_input","r").read().strip()

temp = temp[:-3]+"."+temp[-3:]
now = datetime.now()

output = str(now.day).zfill(2)+"."+str(now.month).zfill(2)+"."+str(now.year)+"\t"+str(now.hour).zfill(2)+":"+str(now.minute).zfill(2)+"\t"+temp

open("/var/www/temperature.log","a").write(output+"\n")

#print output
