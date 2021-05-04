#include <cstdio>
#include <cmath>

#define M_PI 3.14159265358979323846
using namespace std;

int main(){
    int r;
    scanf("%d",&r);
    double uans,tans;
    uans = M_PI * r* r;
    tans = 2 * r* r;
    printf("%6f\n%6f",uans,tans);
}