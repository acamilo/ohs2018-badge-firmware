#!/bin/bash

# Install Toolchain
wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
tar -xzf ~/Downloads/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz
export PATH="$PATH:`pwd`/xtensa-esp32-elf/bin"

# init submodules
git submodule update --init --recursive
export ESPIDF="`pwd`/ohs2018-badge-firmware/esp-idf"
cd micropython/

# build 
make -C mpy-cross
cd ports/esp32/
make
