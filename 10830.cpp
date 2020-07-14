#include <iostream>
#include <vector>
using namespace std;
int n;
int arr[5][5];

 vector <vector <int> > cal(long long b){
     vector <vector <int> > ans(n, vector <int> (n));
     vector <vector <int> > sub(n, vector <int> (n));
     if(b==1){
         for(int i=0;i<n;i++){
             for(int j=0;j<n;j++){
                 sub[i][j] = arr[i][j];
             }
         }

         return sub;
     }

     if(b%2 == 0){
         sub = cal(b/2);
         for(int i=0;i<n;i++){
             for(int j=0;j<n;j++){
                 for(int k=0;k<n;k++){
                     ans[i][j] += sub[i][k] * sub[k][j];
                 }
                 ans[i][j] %= 1000;
             }
         }
         return ans;
     }

     else{
     sub = cal(b-1);
      for(int i=0;i<n;i++){
             for(int j=0;j<n;j++){
                 for(int k=0;k<n;k++){
                     ans[i][j] += sub[i][k] * arr[k][j];
                 }
                 ans[i][j] %= 1000;
             }
         }
         return ans;
     }

 }

int main(){
    long long b;
    cin >> n >> b;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int num;
            cin >> num;
            arr[i][j] =  num;
        }
    }

    vector <vector <int> > mat(n, vector<int>(n));
    mat = cal(b);

    for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
            if(mat[i][j]==1000){
                mat[i][j]=0;
            }
         }
     }

    for(int i=0;i<n;i++){
         for(int j=0;j<n;j++){
             cout << mat[i][j] << " ";
         }
         cout <<"\n";
     }

    return 0;
}