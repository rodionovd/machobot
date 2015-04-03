// tests/assets/target.c - machobot
// Copyright (c) 2015 Dmitry Rodionov
// https://github.com/rodionovd/machobot
//
// This software may be modified and distributed under the terms
// of the MIT license.  See the LICENSE file for details.

/*
	For a fat target:
		$ clang -arch x86_64 -arch i386 -o fat_target target.c
	For an i386 target:
		$ clang -arch i386 -o target32 target.c
	For an x86_64 target:
		$ clang -arch x86_64 -o target64 target.c
*/

#include <stdio.h>

int main(int argc, char *argv[]) {
	return 0;
}