#include <stdio.h>

int main(){
    int start = 64;

    int n;
    int half=0;
    int sum =0;
    scanf("%d",&n);
    half = start/2;
    sum = sum + half;
    int cnt = 1;
    while(sum >= n){
        half = sum/2;
        sum = sum + half;
        cnt ++;
    }

    printf("%d",cnt);


    return 0;
}