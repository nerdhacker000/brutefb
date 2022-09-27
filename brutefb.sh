clear
export PS1="\e[0;32m[github.com/nerdhacker000]\$ \e[0m"
echo " FOR EDUCATIONAL PURPOSES "
echo "  __..__...__...__.._   _._____.___" 
echo " |__ |__) |__) |__) |   |	  |  |___" 
echo " |   |___)|___)|   \|___|   |  |___" 
echo " github:https:github.com/nerdhacker000/"
echo "More tutorials on my website: https://nerdhaka.blogspot.com"
echo "developer: Nerd Haka
echo "[1] 6-character password"
echo "[2] 7-character password"
echo "Choose password length:"
read length
echo "Initializing..."
if [[ $length -eq 1 ]]
then
  echo "Starting 6-character password attack..."
fi
python3 brutefb6.py
