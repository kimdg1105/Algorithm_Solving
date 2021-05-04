#include <cstdio>
#include <cmath>
using namespace std;

int main(){

    long int m,n;
    scanf("%d %d",&m,&n);
    int len = n-m+1;
    long int arr[1000001]={};

    for(int num=0;num<=n;num++){
        arr[num] = num;
    }


    for(int i=2;i<=n;i++){
        if(arr[i]==0){
            continue;
        }
        for(int j=i+i;j<=n;j+=i){
            arr[j] = 0;

        }
    }

    for (int i = m; i <= n; i++) {

        if (arr[i] != 0 && arr[i] != 1){
            printf("%d\n",arr[i]);
        }
    }


}
