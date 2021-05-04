#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        int k,n;
        cin >> k >> n;
        int dp[15][15] ={};
        for(int j=0;j<15;j++){
            dp[0][j] = j;
        }
        // for(int j=0;j<15;j++){
        //     dp[j][1] = 1;
        // }

        for(int r=1;r<=k;r++){
            for(int u=1;u<=n;u++){
                dp[r][u] += dp[r-1][u] + dp[r][u-1];
            }
        }
        cout << dp[k][n] << endl;

    }

}