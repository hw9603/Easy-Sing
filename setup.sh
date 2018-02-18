
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
cd ./marytts/
mvn install