#include <iostream>
#include <stdlib.h>
using namespace std;

long long divide(long long n,long long d){
	long long result=0;
	
	while(1){
		if(n%d!=0)
			break;
		else{
			n=n/d;
			result++;
		}
	}
	return result;
}

int main(){
	long long n,i;
	int five,two;
	
	cin >> n;
	five=0;
	two=0;
    
	for(i=1;i<=n;i++){
		five=five+divide(i,5);
		two=two+divide(i,2);
	}
	
	if(five>two)
		cout << two << '\n';
	else
	cout << five << '\n';
}

