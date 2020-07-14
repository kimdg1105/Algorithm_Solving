#include <iostream>
#include <stack>
#include <cstring>

using namespace std;

int IsVaild(stack<int> st){
    int si= st.size();
    int sum=0;
    for(int i=0;i<si;i++){
        sum += st.top();
        st.pop();
    }
    return sum;
}
int main(){
    while(1){
        stack <int> big;
        stack <int> small;
        int cntb=0;
        int cnts=0;
        int size=0;
        char arr[101];
        while (1)
        {
            cin.getline(arr,100);
            size = strlen(arr);
            if( arr[size-1] == '.'){
            break;
        }
        }

        for(int i=0;i<size;i++){
            if(arr[i]=='('){
                small.push(1);

            }
            if(arr[i]==')'){
                small.push(-1);
                if(IsVaild(small) <= -1 || IsVaild(big) >=1 ){
                    cout << "no" << endl;
                    break;
                }
            }
            if(arr[i]=='['){
                big.push(1);
            }
            if(arr[i]==']'){
                big.push(-1);
                if(IsVaild(big) <= -1 || IsVaild(small) >=1) {
                    cout << "no" << endl;
                    break;
                }
            }

            if(i==size-1){
                if(IsVaild(small) == 0 && IsVaild(big)==0){
                    cout << "yes" << endl;
                }
                else{
                    cout << "no" << endl;

                }
            }
        }
    }


}