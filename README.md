# ohs2018-badge-firmware
```
git submodule update --init --recursive

make -C mpy-cross
cd micopython/ports/esp32/
make

make erase
make deploy
```
