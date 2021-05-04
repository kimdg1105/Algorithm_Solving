#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int n;
    int len;
    cin >> n;

    int arr[n+1][n+1];
    int dp[n+1][n+1];
    for (int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            cin >> arr[i][j];
        }
    }
    for(int i=0;i<=n;i++){
        dp[0][i] = 0;
    }
    int total = 0;
    for (int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            if(j==1){
                dp[i][j] = dp[i-1][j]+arr[i][j];
            }
            else if(j==i){
                dp[i][j] = dp[i-1][j-1]+arr[i][j];
            }
            else{
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+arr[i][j];
            }
            if(total < dp[i][j]){
                total = dp[i][j];
            }
        }
    }
    cout << total << endl;
}