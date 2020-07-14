#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
    int N;
    long long value=0;
    cin >> N;

    long long arr[N];
    for(int i=0;i<N;i++){
        cin >> arr[i];
    }
    sort(arr,arr+N);
    for(int i=0;i<N;i++){
        if(i+1==arr[i]){
            continue;
        }
        else{
            value += abs(arr[i]-(i+1));
        }
    }

    cout << value << endl;
}