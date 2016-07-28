CC = gcc
CFLAGS = -Wall -Wfatal-errors -Iinclude -O3 -march=native -std=c99
CFLAGS_SHARED = -shared -fPIC
CFILES = src/simbd.c
HFILES = include/simbd.h


all: lib

lib: $(HFILES) $(CFILES)	
	mkdir -p lib
	$(CC) $(CFLAGS) $(CFLAGS_SHARED) $(CFILES) -o lib/libsimbd.so -lm

clean:
	rm -f pyrampr/*.pyc 
	rm -rf lib
