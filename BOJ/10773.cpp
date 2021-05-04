#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack <int> st;

    int k;
    cin >> k;

    for(int i=0;i<k;i++){
        int n;
        cin >> n;
        if(n==0){
            st.pop();
        }
        else{
            st.push(n);
        }
    }
        int sum=0;


        while(!st.empty()){
            sum += st.top();
            st.pop();
        }

        cout << sum << endl;
    }
