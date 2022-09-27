clear
export PS1="\e[0;32m[github.com/nerdhacker000]\$ \e[0m"
echo " FOR EDUCATIONAL PURPOSES "
echo "  __..__...__...__.._   _._____.___" 
echo " |__ |__) |__) |__) |   |	  |  |___" 
echo " |   |___)|___)|   \|___|   |  |___" 
echo " github:https:github.com/nerdhacker000/"
echo "More tutorials on my website: https://nerdhaka.blogspot.com"
echo "developer: Nerd Haka
echo "Choose password lenght:"
echo "[1] 6-character password"
echo "[2] 7-character password"
read lenght
echo "Initializing..."
if [[$length - eq 1]] 
then
./brutefb6.sh
else if[[#]]
then
./brutefb7.sh
fi
python3 brutefb6.py
