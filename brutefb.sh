#!/bin/bash
clear
export PS1="\e[0;32m[nerdhacker000]\? \e[0m"
echo "	   FOR EDUCATIONAL PURPOSES "
echo
echo "	    __  __    __    __   _   _ _____  ___" 
echo "     |__ |__)  |__)  |__)  |   |   |   |___" 
echo "     |   |___) |___) |   \ \___/   |   |___" 
echo
echo
echo "	Github:https:github.com/nerdhacker000/"
echo "	My website: https://nerdhaka.blogspot.com"
echo "	Tool developer: Nerd Haka"
echo
echo "	[1] 6 to 7 character password"
echo "	[2] 8 to 10 character password"
echo " - - - - - - - - - - - - - - - - - -" 
echo "	Choose password character length to attack:"
echo
read length
echo "	Initializing..."
python $length.py
