#include <iostream>
#include <string>
using namespace std;

int main(){
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        string num;
        cin >> num;
        int size = num.size();
        int a = int(num[size-1]);

        if(a % 2 != 0){
            cout << "odd" << endl;
        }
        else{
            cout << "even" << endl;
        }
    }
}