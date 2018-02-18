
if [[ "$OSTYPE" == "linux-gnu" ]]; then
        # ...
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        brew install libjack-dev
        brew install libasound2-dev
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        echo "Did't tested on Linux on Windows, try at your own risk."
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        echo "Did't tested on MinGW, try at your own risk."
        sudo apt-get -y install libjack-dev
        sudo apt-get install libasound2-dev
else
        echo "known system..."
        exit 1
fi
# install marry tts 5.x
cd ./marytts
mvn install
cd ../

DIRECTORY="./marytts/target/marytts-5.3-SNAPSHOT/lib"
if [ ! -d "$DIRECTORY" ]; then
  # Exit if mvn build failed or something strange happened.
  echo "MaryTTS Install Failed..."
  exit 1
fi

cp ./brad_voice/results/Feb11-170sentences/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar \
   $DIRECTORY/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar