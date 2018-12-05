#!/usr/bin/env bash

while true; do
    git pull git://github.com/LSparky/MeidoBot.git
    sed -i '' 's/alreadysend/notsendyet/g' token.json
    echo "waiting 2 seconds"
    sleep 2
    ./bot.py
    echo " "
    echo "You can exit the loop by doing ctrl + c 2x"
    echo " "
    for i in {5..1}; do
        echo “Restarting in $i”
        sleep 1
    done
done
