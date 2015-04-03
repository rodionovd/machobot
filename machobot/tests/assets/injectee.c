// tests/assets/injectee.c - machobot
// Copyright (c) 2015 Dmitry Rodionov
// https://github.com/rodionovd/machobot
//
// This software may be modified and distributed under the terms
// of the MIT license.  See the LICENSE file for details.

/*
	$ clang -dynamiclib -single_module -O3 -current_version 1.0.0 -compatibility_version 1.0.0 \
	-arch x86_64 -arch i386 -install_name "@executable_path/injectee.dylib" -o injectee.dylib injectee.c
*/


#include <stdlib.h>
#define kMagicReturnValue 0xFD

__attribute__((constructor))
void aloha(void)
{
	exit(kMagicReturnValue);
}