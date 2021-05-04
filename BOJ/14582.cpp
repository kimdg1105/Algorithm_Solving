#include <iostream>

using namespace std;

int main(){
    int a[10];
    int b[10];
    int suma=0,sumb=0;
    int flag=0, subflag =0;

    for(int i=0;i<9;i++){
        cin >> a[i];
    }
    for(int i=0;i<9;i++){
        cin >> b[i];
    }

    for(int i=0;i<9;i++){
        suma += a[i];
        if(suma > sumb){
            flag =1;
        }
        sumb += b[i];
    }

        if(flag==1){
                cout << "Yes" <<endl;

        }
        else{
                cout << "No" <<endl;

        }
    return 0;

}