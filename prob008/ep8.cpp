#include<iostream>
#include<fstream>
using namespace std;

int main(){
	int greatestProduct;
	int product = 0;
	int n1, n2, n3, n4, n5;
	n1 = n2 = n3 = n4 = n5 = 0;
	ifstream inStream;
	inStream.open("data.dat");
	n4 = inStream.get() - 48;
	n3 = inStream.get() - 48;
	n2 = inStream.get() - 48;
	n1 = inStream.get() - 48;
	while(inStream.good()){
		n5 = n4;
		n4 = n3;
		n3 = n2;
		n2 = n1;
		n1 = inStream.get() - 48;
		product = n1*n2*n3*n4*n5;
		if(product > greatestProduct)
			greatestProduct = product;
		cout << n5 << " " << n4 << " " << n3 << " " << n2 << " " << n1 << " ||Product: " << product << " (" << greatestProduct << ")\n";
	}
	cout << greatestProduct;
	return 0;
}

