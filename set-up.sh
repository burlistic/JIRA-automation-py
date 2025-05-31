#!/bin/bash

#Set up commands for Linux / Coder Workspace

sudo apt update

sudo apt install -y python3 python3-pip python3-pipenv

#Run pipenv shell to activate the environment depenancies

sudo pipenv shell

#Set up commands for Windows

#Run pipenv shell to activate the environment depenancies

pip install pipenv

pipenv shell

