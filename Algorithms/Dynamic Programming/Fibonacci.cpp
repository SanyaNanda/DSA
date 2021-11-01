#include <iostream>
#include <vector>
using namespace std;


int fib(int n, vector<int> &dp ){
    if(n==0 or n==1) return n;
    if(dp[n]!=-1) return dp[n];
    int answer = fib(n-1,dp)+fib(n-2,dp);
    dp[n]=answer;
    cout<<answer<<endl;
    return answer;
}

int main(){
    int n;
    cin>>n;
    vector<int> dp(n+1,-1);
    fib(n,dp);
    return 0;
}