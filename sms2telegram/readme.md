Description
============

This script can be used as a handler for [SMS Server Tools](http://smstools3.kekekasvi.com/) (smstools Linux package) for forwarding all incoming SMS to Telegram.

I found a detailed description of the installation [here](https://medium.com/@MichaelMarner/sending-receiving-sms-on-linux-acf7610e2d2). Also can be helpful.


Instructions
============
Create the telegram bot according to the [Telegram Bot guide](https://core.telegram.org/bots#how-do-i-create-a-bot).

Save the sms_handler.sh file from this repositotory to /usr/local/bin folder. Befor usage please set the correct Telegram API token and chat id from the previous step: token and chat_id variables:
```
  token='TELEGRAM_API_TOKEN_ExAmPlE'
  chat_id=587412369
```
Then add the string
```
eventhandler = /usr/local/bin/sms_handler.sh
```
to the main section of the /etc/smsd.conf file. For example:
```
#
# /etc/smsd.conf
#
# Description: Main configuration file for the smsd
#

devices = E1550
eventhandler = /usr/local/bin/sms_handler.sh
outgoing = /var/spool/sms/outgoing
checked = /var/spool/sms/checked
incoming = /var/spool/sms/incoming
logfile = /var/log/smstools/smsd.log
infofile = /var/run/smstools/smsd.working
pidfile = /var/run/smstools/smsd.pid
[CUTTED]
```
And restart the smstools daemon to apply the changes.\
Now all incoming SMS to the number handeled by smstools will be forwarded to your Telegram bot chat.

Author
============
Denis Chertkov, denis@chertkov.info, 12/05/2023
