#include <iostream>

using namespace std;

int main(){
    int N, M;

    int num1, num2;
    cin >> N >> M;
    int bucket[N+1];
    for(int i=1;i<=N;i++){
        bucket[i] =i;
    }


    for(int i=0;i<M;i++){
        cin >> num1 >> num2;
        int tmp;
        tmp = bucket[num1];
        bucket[num1] = bucket[num2];
        bucket[num2] = tmp;
    }

    for(int i=1;i<=N;i++){
        cout << bucket[i] << " ";
    }
}