#### 0. Introduction

EasySing is a project for EECS 498.

#### 1. How to install EasySing:

EasySing requires `jre` (java8), `python3`, `pip3`, and `mvn` (version 3.x)  installed. (To test that just type `java` or `python3` or `pip3` or `mvn` in command line and see whether the command exists)

If you are using Max OSX, `brew` is strongly recommended. If you are using Linux, `apt-get` is required for package installation. 

##### 1.1. Installation Steps:

1. At root directory `…/498-Vocaloid`,  run `./setup.sh` 

#### 2. How to run EasySing:

At root directory `…/498-Vocaloid`,  run `python3 -m vocaloid`

#### 3. Troubleshooting:

3.1 On Mac OSX, if you saw this error:
```shell
ImportError: dlopen(/usr/local/lib/python3.6/site-packages/PyQt5/QtWidgets.so, 2): Library not loaded: @rpath/QtWidgets.framework/Versions/5/QtWidgets
  Referenced from: /usr/local/lib/python3.6/site-packages/PyQt5/QtWidgets.so
  Reason: image not found
```

Try to reinstall PyQt5:

```
sudo pip3 uninstall PyQt5
LDFLAGS=-L/usr/local/opt/qt/lib CPPFLAGS=-I/usr/local/opt/qt/include pip3 install PyQt5  
```

If the previous command didn't work, try run this line before that:

`brew install pyqt` 
