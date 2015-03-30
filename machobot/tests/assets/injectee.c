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