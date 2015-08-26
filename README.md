# Cubietruck Temperature-Monitor

This project consists of a Python script that runs on your Cubietruck and logs the SoC temperature to a file.<br/>
A D3-based webpage allows you to monitor the temperature via LAN or internet.

Author: Matthias Bock<br/>
License: GNU Affero GPLv3 (AGPLv3)

## Installation

Install apache2, cd to your Cubietruck /var/www directory and clone this repository:

<pre>apt-get install apache2
cd /var/www
git clone https://github.com/interoberlin/Cubietruck-Temperature-Monitor.git</pre>

Enable temperature logging by adding this line at the end of your Cubietruck's /etc/crontab:

<pre>* * * * * root /var/www/temperature_log.py</pre>

