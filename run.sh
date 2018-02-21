# check whether marytts exits
DIRECTORY="./marytts/target/marytts-5.3-SNAPSHOT/bin"
if [ ! -d "$DIRECTORY" ]; then
  # Exit if mvn build failed or something strange happened.
  echo -e "${RED}MaryTTS not Install... See README for how to install${NC}"
  exit 1
fi
./marytts/target/marytts-5.3-SNAPSHOT/bin/marytts-server &
# $PID is the pid of marytts
PID=$!
# run the main GUI.
python3 -m vocaloid
# kill processes
if [ -n $(pgrep -P $PID) ]; then
	kill $(pgrep -P $PID)
fi
if [ -n $PID ]; then
	kill $PID
fi

