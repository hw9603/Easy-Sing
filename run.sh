DIRECTORY="./marytts/target/marytts-5.3-SNAPSHOT/bin"
if [ ! -d "$DIRECTORY" ]; then
  # Exit if mvn build failed or something strange happened.
  echo -e "${RED}MaryTTS not Install... See README for how to install${NC}"
  exit 1
fi
./marytts/target/marytts-5.3-SNAPSHOT/bin/marytts-server &
# echo $!
PID=$!
python3 -m vocaloid
kill -- -$(ps -o pgid= $PID | grep -o [0-9]*)
# echo $PID
