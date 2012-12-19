#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

ifstream inStream;
int* numbers [100];
int* digits = NULL;
int* sum = new int[60];

void initializeSum(){
	for(int i = 0; i < 60; ++i){
		sum[i] = 0;
	}
}

void inputNumbers(){
	inStream.open("data.txt");
	for(int i = 0; i < 100; ++i){
		digits = new int[50];
		for(int j = 0; j < 50; ++j){
			digits[j] = (inStream.get() -'0');
		}
		numbers[i] = digits;
		inStream.ignore();		
	}
}

void printSum(){
	long long tempSum = 0;
	for(int j = 50; j >= 0; --j){
		for(int i = 0; i < 100; i++){
			tempSum += numbers[i][j];
		}
		sum[j + 10] = tempSum % 10;
		tempSum = (tempSum - (tempSum % 10))/10;
	}
	for(int j = 9; j >= 0; j--){
		sum[j] = tempSum % 10;
		tempSum = (tempSum - (tempSum % 10))/10;
	}
	for(int i = 0; i < 20; i++){
		cout << sum[i];
	}
}

int main(){
	
	initializeSum();
	inputNumbers();
	printSum();
	return 0;
}


