#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include "blake2/blake2.h"

int main() {
	char in[] = "123456789";
	unsigned char out[32];
	blake2b_state       S[1];
	
	blake2b_init(S, sizeof(out));
	blake2b_update(S, in, sizeof(in));
    return blake2b_final(S, out, sizeof(out));
}
