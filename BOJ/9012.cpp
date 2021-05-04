#include <iostream>
#include <stack>
#include <string>
using namespace std;


bool vps(string word){
    stack <char> st;
    int length = word.size();
    for(int j=0;j<length;j++){
        if(word[j]== '('){
            st.push('(');
        }
        else if(word[j] == ')'){
            if(!st.empty()){
                st.pop();
            }
            else{
                return false;
            }
        }
    }

    return st.empty();

}

int main(){
    int T;
    cin >> T;
    string word;
    for(int i=0;i<T;i++){

        cin >> word;
        if(vps(word)==true){
            cout <<"YES" << endl;
        }
        else{
            cout << "NO" <<endl;
        }
    }

}



