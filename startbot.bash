#!/usr/bin/env bash

while true; do
    git fetch --all
    git reset --hard origin/master
    echo "waiting 5 seconds"
    sleep 5
    ./bot.py
    echo " "
    echo "You can exit the loop by doing ctrl + c 2x"
    echo " "
    for i in {5..1}; do
        echo “Restarting in $i”
        sleep 1
    done
done
