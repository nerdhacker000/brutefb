#!/bin/bash

clear
export PS1="\e[0;32m[github.com/nerdhacker000]\$ \e[0m"
echo "		FOR EDUCATIONAL PURPOSES "
echo
echo "		 __  __   __   __  _   _ _____ ___" 
echo "		|__ |__) |__) |__) |   |   |  |___" 
echo "		|   |___)|___)|   \|___|   |  |___" 
echo
echo
echo "Github:https:github.com/nerdhacker000/"
echo "My website: https://nerdhaka.blogspot.com"
echo "developer: Nerd Haka
echo "[1] 6-character password"
echo "[2] 7-character password"
echo "Choose password length:"
read length
echo "Initializing..."
if [[ $length -eq 1 ]]
python brutefb6.py
then
fi
exit
