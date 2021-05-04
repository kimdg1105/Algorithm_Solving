#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int A=1;
    int N;
    int arr[51];
    int cnt;
    int size=0;
    cin >> cnt;
    for(int i=0;i<cnt;i++){
        cin >> arr[i];
        size++;
    }
    sort(arr,arr+size);
    A = arr[0] * arr[size-1];

    cout << A << endl;
}