#!/usr/bin/env bash

while true; do
    git pull git@github.com:LSparky/MeidoBot.git
    ./bot.py
    for i in {5..1}; do
        echo “Restarting in $i”
        sleep 1
    done
done
