# ohs2018-badge-firmware
## Install Toolchain
### Install Toolchain Dependancies
```
sudo apt-get install git wget make libncurses-dev flex bison gperf python python-serial
```

### Download and unpack Toolchain
for 64-bit Linux:
https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz

for 32-bit Linux:
https://dl.espressif.com/dl/xtensa-esp32-elf-linux32-1.22.0-80-g6c4433a-5.2.0.tar.gz

### Extract
```
mkdir -p ~/esp
cd ~/esp
tar -xzf ~/Downloads/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
```

### PATH Variable
Add the following to the end of your `~/.bashrc` file

```
export PATH="$PATH:$HOME/esp/xtensa-esp32-elf/bin"
```

## Install Dependencies
```
sudo apt-get install build-essential libreadline-dev libffi-dev git pkg-config

```
## Setup the Repo
```
git submodule update --init --recursive
ln -s $HOME/ohs2018-badge-firmware/badge/ $HOME/ohs2018-badge-firmware/micropython/ports/esp32/
```

## Setup ESPIDF Variable
add this to the end of your `~/.bashrc` file

```
export ESPIDF="/home/oshwa/ohs2018-badge-firmware/esp-idf"
```

## Build The Firmware
```
cd micropython/
make -C mpy-cross
cd ports/esp32/
make

make erase
make deploy
```
