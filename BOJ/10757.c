#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define stod(x) (x==0?0:x-'0')
char a[100000];
char b[100000];
char sum[100000];

void reverse(char *,int);
char* add(char *, char *);

int main(){
    scanf("%s %s",a,b);

    printf("%s",add(a,b));
}

void reverse(char * arr, int len){
    char temp;
    for(int i=0;i<len/2;i++){
        temp = arr[i];
        arr[i] = arr[len-1-i];
        arr[len-1-i] = temp;
    }
    return ;
}

char * add(char *a, char* b){
    int len =0;
    int carry =0;



    if(strlen(a)>= strlen(b)){
        len = strlen(a);
    }
    else{
        len = strlen(b);
    }

    reverse(a,strlen(a));
    reverse(b,strlen(b));
    for(int i=0;i<=len;i++){
        sum[i]= (stod(a[i])+stod(b[i])+carry)%10+'0';
        if((stod(a[i])+stod(b[i])+carry) >9){
            carry = 1;
        }
        else{
            carry = 0;
        }

        if(sum[len]=='0'){
            sum[len] =0;
        }
    }
    reverse(sum,strlen(sum));
    return sum;
}