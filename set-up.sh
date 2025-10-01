#!/bin/bash

#Set up commands for Linux / Coder Workspace

#Ensure Python 3.11 is installed before setting up Pipenv
sudo apt install -y python3.11 python3.11-venv

sudo apt update

sudo apt install -y python3-pip python3-pipenv

#Run pipenv shell to activate the environment depenancies

sudo pipenv shell

#Set up commands for Windows

#Run pipenv shell to activate the environment depenancies

pip install pipenv

pipenv shell

