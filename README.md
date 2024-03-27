# SM64coopdx Patcher For Linux
Note: this is not like the windows coopdx patcher and this has only been tested on Fedora

A simple python script for (almost)automaticaly compiling SM64coopdx for linux.

# How to use
### Dependencies (Taken from the coopdx build documentation)
The script has the following package requirements:

* python3 >= 3.6
* libsdl2-dev
* libglew-dev
* git
* libcurl
* zlib

#### Debian / Ubuntu - targeting 64 bits
```
sudo apt install build-essential git python3 libglew-dev libsdl2-dev libz-dev libcurl4-openssl-dev
```
#### Debian / Ubuntu - targeting 32 bits
```
sudo apt install build-essential git python3 libglew-dev:i386 libsdl2-dev:i386 libz-dev:i386 libcurl4-openssl-dev:i386
```
#### Fedora - targeting 64 bits
```
sudo dnf install make gcc python3 glew-devel SDL2-devel zlib-devel libcurl-devel
```
#### Fedora - targeting 32 bits
```
sudo dnf install python3.i686 glew-devel.i686 SDL2-devel.i686 zlib-devel.i686 libcurl-devel.i686
```
#### Arch Linux
```
sudo pacman -S base-devel python sdl2 glew zlib-devel libcurl-devel
```

### Usage Documentation
All the input necesary is documented when the scripts ask you
Note: If your wondering where does the coopdx folder appear well it appears in the home directory
