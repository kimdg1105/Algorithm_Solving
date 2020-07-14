#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;

    long sum=0;

    for(int i=1;i<=N;i++){
        sum += (i*(i+1))/2;
    }

    for(int i=1;i<=N;i++){
        if(N%2==0){
            if(i%2 == 0){
                continue;
            }
            sum += (i*(i+1))/2;
        }
        else{
            if(i%2==1){
                continue;

            }
            sum += (i*(i+1))/2;
        }
    }

        cout << sum <<endl;

}