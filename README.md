## 0. Introduction

EasySing is a project for EECS 498. 

## 1. How to install EasySing

EasySing requires `jdk` (Java 8), `mvn` (version 3.x), `python3`, and `pip3`   installed. To test that:
```shell
echo $JAVA_HOME
echo $PATH
which java
java -version
mvn --version
pip3 --version
python3 --version
```

If you are using Max OSX, `brew` is strongly recommended. If you are using Linux, `apt-get` is required for package installation. Our install script will check those dependencies. 

##### 1.1. Installation Steps:

At root directory `…/498-Vocaloid`,  run `./setup.sh` 

## 2. How to run EasySing

At root directory `…/498-Vocaloid`,  run `./run.sh`

3. How to use EasySing
---



4. Troubleshooting
---

**3.1** On Mac OSX, if you saw this error:

```
ImportError: dlopen(/usr/local/lib/python3.6/site-packages/PyQt5/QtWidgets.so, 2): 
Library not loaded: @rpath/QtWidgets.framework/Versions/5/QtWidgets
  Referenced from: /usr/local/lib/python3.6/site-packages/PyQt5/QtWidgets.so
  Reason: image not found
```

Try to reinstall PyQt5:

```
sudo pip3 uninstall PyQt5
LDFLAGS=-L/usr/local/opt/qt/lib CPPFLAGS=-I/usr/local/opt/qt/include pip3 install PyQt5  
```

If the previous command didn't work, try run this line before reinstalling PyQt5 and then reinstall PyQt5:

```brew install pyqt```