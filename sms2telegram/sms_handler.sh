#!/usr/bin/bash
# SMS to Telegram gateway script for smsd
# Denis Chertkov, denis@chertkov.info, 22/10/2023
#
# Please set the correct token and chat_id variables!

if [[ $1 == "RECEIVED" ]]; then
  token='TELEGRAM_API_TOKEN'
  chat_id=CHAT_ID
  if sed -e '/^$/ q' < "$2" | grep "^Alphabet: UCS2" > /dev/null; then
    text=$(sed -e '1,/^$/ d' < "$2" | iconv -f UNICODEBIG -t UTF-8)
  else
    text=$(sed -e '1,/^$/ d' < "$2")
  fi

  prefix=$(grep "^From:" "$2" |awk '{print $2}'| awk '{if ($1+0 == $1) print "+"}')
  from=$(grep "^From:" "$2" |awk '{print $2}')
  subj=$(grep "^Subject:" "$2" |awk '{print $2}')
  time=$(grep "^Received:" "$2" |awk '{print $2 " " $3}')

  /usr/bin/curl -s --header 'Content-Type: application/json' --request 'POST' \
            --data "{\"chat_id\":\"${chat_id}\",\
            \"parse_mode\":\"HTML\" ,\
            \"disable_web_page_preview\":\"true\",
            \"text\":\"<b>From: $prefix${from}\n${time}</b>\n${text}\"}"\
             "https://api.telegram.org/bot${token}/sendMessage" > /dev/null 2>&1
fi
