#include<iostream>
using namespace std;

int prevTerm = 1;
int curTerm = 1;
int sum = 0;

int fib(){
	int next = prevTerm + curTerm;
	prevTerm = curTerm;
	curTerm = next;
}

int main(){
	while(curTerm <= 4000000){
		if(curTerm % 2 == 0)
			sum += curTerm;
		fib();
	}
	cout << sum;
	return 0;
}
