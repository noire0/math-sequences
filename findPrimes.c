#include <stdio.h>
#include <math.h>
#include <getopt.h>
#define sqrt_n (int) floor(sqrt(n))

_Bool isPrime(int n)
{
	int factor=2;
	while (factor <= sqrt(n)) {
		if (n%factor == 0)
			return 0;
		else
			factor+=1;
	}
	return 1;
}

int main () {
	int n=3, max;
	_Bool input, nIsPrime;
	printf("Maximum integer to check:\n");
	input=scanf("%d", &max);
	if (input) {
		printf("OK\n2\n");
		while (n <= max) {
			nIsPrime = isPrime(n);
			if (nIsPrime == 1)
				printf("%d\n", n);
			n+=2;
		}
	} else {
		printf("Write an integer.\n");
	}
	return !input;
}
