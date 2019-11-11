#!/usr/bin/env bash

if [ "$USER" != "root" ]; then
  echo "Without execute permission" && exit 1
fi

apt update
apt upgrade -y

curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt install -y nodejs
apt install python3-pip -y
pip3 install nltk
pip3 install textblob