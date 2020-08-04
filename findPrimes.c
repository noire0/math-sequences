#include <stdio.h>

int _prime(int n) {
	int factor=3;
	while (factor <= n) {
        	if (n%factor == 0) {
			if (factor == n) {
				return n;
			} else {
				return 0;
			}
		} else {
			factor+=2;
		}
	}
}

void main () {
	int n, max;
	_Bool input;
	printf("Maximum number to check:\n");
	input=scanf("%d", &max);
	if (input!=0) {
		n=3;
		printf("2\n");
		while (n <= max) {
			if (_prime(n) != 0) {
				printf("%d\n", _prime(n));
			}
			n+=2;
		}
	}
}			
