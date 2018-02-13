#### How to install Brad's voice on you computer:

Option 1 (tested working):

- Clone Marytts from GitHub then checkout branch 5.x
- Replace `marytts/marytts-runtime/src/main/java/marytts/modules/acoustic/ProsodyElementHandler.java` with `brad_voice/results/ProsodyElementHandler.java`.
- Build Marytts with `mvn install`.
- Put `brad_voice/results/Feb11-170sentences/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar` in `marytts/target/marytts-5.3-SNAPSHOT/lib/voice-brad_voice_new-hsmm-5.3-SNAPSHOT.jar`. 
- Run Marytts server. 

Option 2 (theoretically working if you are using Mac OSX):

- Unzip `brad_voice/marytts-5.3.zip`. 
- Run Marytts server. 



#### How to install Pygame on mac:

1. `brew install mercurial`
2. `brew install sdl sdl_image sdl_mixer sdl_ttf portmidi`
3. `brew tap homebrew/headonly` (if you have any trouble here, try `brew install --HEAD smpeg` instead)
4. `sudo -H pip install hg+http://bitbucket.org/pygame/pygame` or `sudo -H pip3 install hg+http://bitbucket.org/pygame/pygame` for python3.