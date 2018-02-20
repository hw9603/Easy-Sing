RED='\033[0;31m' # For color shell
GREEN='\033[0;32m' # For color shell
NC='\033[0m' # No Color
command -v java >/dev/null 2>&1 || \
    { echo -e >&2 "${RED}I require java but it's not installed.  Aborting.${NC}"; exit 1; }
command -v mvn >/dev/null 2>&1 || \
    { echo -e >&2 "${RED}I require mvn but it's not installed.  Aborting.${NC}"; exit 1; }
command -v python3 >/dev/null 2>&1 || \
    { echo -e >&2 "${RED}I require python3 but it doesn't exist.  Aborting.${NC}"; exit 1; }
command -v pip3 >/dev/null 2>&1 || \
    { echo -e >&2 "${RED}I require pip3 but it doesn't exist.  Aborting.${NC}"; exit 1; }
echo -e "${GREEN}Installing python system dependency${NC}"
if [[ "$OSTYPE" == "linux-gnu" ]]; then
        # ...
        command -v apt-get >/dev/null 2>&1 || \
            { echo -e >&2 "${RED}I require apt-get but it's not installed.  Aborting.${NC}"; exit 1; }
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        echo -e "${RED}Mac OSX${NC}"
        # command -v brew >/dev/null 2>&1 || \
        #     { echo -e >&2 "${RED}I require brew but it's not installed.  Aborting."; exit 1; }
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        echo -e "${RED}Did't tested on Linux on Windows, try at your own risk.${NC}"
        command -v apt-get >/dev/null 2>&1 || \
            { echo -e >&2 "${RED}I require apt-get but it's not installed.  Aborting.${NC}"; exit 1; }
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        echo -e "${RED}Did't tested on MinGW, try at your own risk.${NC}"
        command -v apt-get >/dev/null 2>&1 || \
            { echo -e >&2 "${RED}I require apt-get but it's not installed.  Aborting.${NC}"; exit 1; }
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
else
        echo -e "${RED}Unknown System...  Aborting.${NC}"
        exit 1
fi

# install python dependency
echo -e "${GREEN}Installing python dependency${NC}"
sudo pip3 install -e .

# install marytts 5.x
echo -e "${GREEN}Installing MaryTTS 5.x${NC}"
cd ./marytts
mvn -q install
cd ../

DIRECTORY="./marytts/target/marytts-5.3-SNAPSHOT/lib"
if [ ! -d "$DIRECTORY" ]; then
  # Exit if mvn build failed or something strange happened.
  echo -e "${RED}MaryTTS Install Failed...${NC}"
  exit 1
fi
# install brad's voice.
cp ./brad_voice/results/Feb11-170sentences/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar \
   $DIRECTORY/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar
echo -e "${GREEN}Successfully Installed${NC}"