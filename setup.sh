command -v java >/dev/null 2>&1 || \
    { echo >&2 "I require java but it's not installed.  Aborting."; exit 1; }
command -v mvn >/dev/null 2>&1 || \
    { echo >&2 "I require mvn but it's not installed.  Aborting."; exit 1; }
command -v python3 >/dev/null 2>&1 || \
    { echo >&2 "I require python3 but it doesn't exist.  Aborting."; exit 1; }
command -v pip3 >/dev/null 2>&1 || \
    { echo >&2 "I require pip3 but it doesn't exist.  Aborting."; exit 1; }

if [[ "$OSTYPE" == "linux-gnu" ]]; then
        # ...
        command -v apt-get >/dev/null 2>&1 || \
            { echo >&2 "I require apt-get but it's not installed.  Aborting."; exit 1; }
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        command -v brew >/dev/null 2>&1 || \
            { echo >&2 "I require brew but it's not installed.  Aborting."; exit 1; }
        brew install libjack-dev
        brew install libasound2-dev
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        echo "Did't tested on Linux on Windows, try at your own risk."
        command -v apt-get >/dev/null 2>&1 || \
            { echo >&2 "I require apt-get but it's not installed.  Aborting."; exit 1; }
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        echo "Did't tested on MinGW, try at your own risk."
        command -v apt-get >/dev/null 2>&1 || \
            { echo >&2 "I require apt-get but it's not installed.  Aborting."; exit 1; }
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
else
        echo "unknown system..."
        exit 1
fi

# install python dependency
echo "Installing python dependency"
sudo pip3 install -e .

# install marytts 5.x
echo "Installing MaryTTS 5.x"
cd ./marytts
mvn --quiet install
cd ../

DIRECTORY="./marytts/target/marytts-5.3-SNAPSHOT/lib"
if [ ! -d "$DIRECTORY" ]; then
  # Exit if mvn build failed or something strange happened.
  echo "MaryTTS Install Failed..."
  exit 1
fi
# install brad's voice.
cp ./brad_voice/results/Feb11-170sentences/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar \
   $DIRECTORY/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar
echo "successfully installed"