#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int n;
    cin >> n;
    int podo[n];
    int dp[100001] ={};

    for(int i=1;i<=n;i++){
        cin >> podo[i];
    }
    dp[1] = podo[1];
    dp[2] = podo[1] + podo[2];

    for(int i=3;i<=n;i++){
        dp[i] = max(podo[i]+podo[i-1]+dp[i-3],podo[i]+dp[i-2]);
        dp[i] = max(dp[i-1],dp[i]);
    }

    cout << dp[n] << endl;





}