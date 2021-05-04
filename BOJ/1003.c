#include <stdio.h>
int D[41];


int main(){
    int input = 0;
    scanf("%d",&input);
    for(int i=0;i<input;i++){
        int a=0;
        scanf("%d",&a);
        fibo(a);
        if(a==0){
            printf("%d %d",1,0);
            printf("\n");
        }
        else if(a==1){
            printf("%d %d",0,1);
            printf("\n");
        }
        else{
        printf("%d %d",D[a-1],D[a]);
        printf("\n");

        }
    }
}

int fibo(int n){
    if(n==0){
        D[0] = 0;
        return 0;
    }
    else if (n==1){
        D[1] = 1;
        return 1;
    }
    else{
        if(D[n] != 0){
            return D[n];
        }
        else{
            D[n] = fibo(n-1) + fibo(n-2);
        }
    }
    return D[n];
}