#!/usr/bin/env bash

while true; do
    git pull
    ./bot.py
    for i in {5..1}; do
        echo “Restarting in $i”
        sleep 1
    done
done