#!/usr/bin/env bash

while true; do
<<<<<<< HEAD
    git pull git@github.com:LSparky/MeidoBot.git
=======
    git pull git://github.com/LSparky/MeidoBot.git
    echo "waiting 4 seconds"
    sleep 4
>>>>>>> ffc2dc9... Update startbot.bash
    ./bot.py
    for i in {5..1}; do
        echo “Restarting in $i”
        sleep 1
    done
done
