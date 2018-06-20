# ohs2018-badge-firmware
```
ln -s badge micropython/ports/esp32/badge
git submodule update --init --recursive

cd micropython/
make -C mpy-cross
cd ports/esp32/
make

make erase
make deploy
```
