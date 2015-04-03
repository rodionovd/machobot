// tests/assets/deps.c - machobot
// Copyright (c) 2015 Dmitry Rodionov
// https://github.com/rodionovd/machobot
//
// This software may be modified and distributed under the terms
// of the MIT license.  See the LICENSE file for details.

/*
	$ clang -lutil -weak_library injectee.dylib -weak_framework CoreFoundation \
	-o deps deps.c
*/

int main(int argc, char *argv[]) {}
