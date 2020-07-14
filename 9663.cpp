#include <iostream>
#include <vector>
using namespace std;


int getposition(int y,vector <vector<bool> > &board);
bool IsVaild(int y,int x,vector <vector<bool> > &board);
bool CheckRange(int y, int x, int size){
    return y>=0 && x>=0 && y <size && x <size;
};

int main(){
    int n;
    cin >> n;
    vector < vector<bool> > board(n, vector<bool>(n,false));
    // n*n 보드판 false로 초기화
    cout << getposition(0,board) << endl;
}

int getposition(int y,vector <vector<bool> > &board){
    int ret=0;
    if(y==board.size()){
        return 1;
    }
    for(int i=0;i<board.size();i++){
        if(IsVaild(y,i,board)){
                board[y][i] = true;
                ret += getposition(y+1,board);
                board[y][i] = false;
            }
    }

    return ret;

}

bool IsVaild(int y,int x,vector <vector<bool> > &board){
    int dx=0;
    while (--y>=0)
    {
        ++dx;
        if(board[y][x] == true){
            return false;
        }
        if(CheckRange(y,x-dx,board.size()) && board[y][x-dx]==true){
            return false;
        }
        if(CheckRange(y,x+dx,board.size()) && board[y][x+dx]==true){
            return false;
        }

    }
    return true;

}