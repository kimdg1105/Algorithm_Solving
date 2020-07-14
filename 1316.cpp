#include <iostream>
#include <string>
using namespace std;

int main(){
    int n;
    string word;

    cin >> n;
    int cnt=0;
    for(int i=0;i<n;i++){
        cin >> word;
        int si = word.length();
        int flag = 0;
        for(int j=0;j<si;j++){
            for(int k=1;k<si;k++){
                if(word[j]==word[k]){
                    if(k-j >1){
                        if(word[k] != word[k-1]){
                        flag = 1;

                        }
                    }
                }
            }
        }
        if(!flag){
                cnt++;
            }

    }

    cout << cnt << endl;
}