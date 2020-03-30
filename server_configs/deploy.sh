#!/bin/sh

RUN_DIR="/opt/flameboi-slack-api/"
BASE_DIR="/home/stu/flameboi-slack-api/"

sudo systemctl stop flameboi-dev.service

if [ -d $BASE_DIR ]  && echo "Repo exists!"
then
    echo "Updating the repo"
    cd $BASE_DIR
    /usr/bin/git pull
    echo "Done!"
else
    echo "Cloning the repo"
    cd 
    /usr/bin/git clone git@github.com:ASU-CodeDevils/flameboi-slack-api.git
    echo "Done!"
fi

echo "Make sure to put the .env file in the flameboi-slack-api/src/ directory!!!"

echo "Copying $BASE_DIR to $RUN_DIR..."
sudo cp -r $BASE_DIR $RUN_DIR
echo "Done!"
echo "Copying new service into systemd..."
sudo cp $RUN_DIR/server_configs/flameboi.service /etc/systemd/system/flameboi-dev.service
echo "Done!"


echo "Updating systemd services..."
sudo systemctl daemon-reload
sudo systemctl restart flameboi-dev.service
echo "Done!"

echo "Checking status of the new flameboi service..."
sudo systemctl status flameboi-dev.service