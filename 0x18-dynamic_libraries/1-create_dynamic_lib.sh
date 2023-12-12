#!/bin/bash
gcc -fpic -c *.c
gcc _shared *.o -o liball.so
