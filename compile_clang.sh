mkdir -p build

clang -c src/stb_wrapper.c -o build/stb_wrapper.o
#clang -o build/main -g -O2 -m64 -std=c99 -Wall -Weverything -Wno-float-equal -pedantic -lm build/stb_wrapper.o src/main.c
clang -o build/main -g -O0 -std=c99 -Wno-float-equal -lm build/stb_wrapper.o src/main.c
