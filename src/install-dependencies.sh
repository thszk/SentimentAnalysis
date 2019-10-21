#!/usr/bin/env bash

if [ "$USER" != "root" ]; then
  echo "Without execute permission" && exit 1
fi

apt update
apt upgrade -y

apt install python3-pip -y
pip3 install newspaper3k
pip3 install nltk
pip3 install textblob