#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <numeric>
#include <vector>
using namespace std;
using i128=__int128_t;
long long det(vector<vector<long long>> a){
 int n=a.size(); if(!n)return 1; long long sign=1,prev=1;
 for(int k=0;k<n-1;k++){int p=k;while(p<n&&a[p][k]==0)p++;if(p==n)return 0;if(p!=k){swap(a[p],a[k]);sign=-sign;}long long pivot=a[k][k];
  for(int i=k+1;i<n;i++)for(int j=k+1;j<n;j++){i128 num=(i128)a[i][j]*pivot-(i128)a[i][k]*a[k][j];if(k){assert(num%prev==0);num/=prev;}a[i][j]=(long long)num;}prev=pivot;if(!prev)return 0;}
 return sign*a[n-1][n-1];
}
bool has_negative_minor(const vector<vector<int>>& G){
 int n=G.size(); vector<int> comb;
 for(int sz=1;sz<=5;sz++){
  comb.resize(sz);iota(comb.begin(),comb.end(),0);
  while(true){vector<vector<long long>> sub(sz,vector<long long>(sz));for(int i=0;i<sz;i++)for(int j=0;j<sz;j++)sub[i][j]=G[comb[i]][comb[j]];if(det(sub)<0)return true;
   int t=sz-1;while(t>=0&&comb[t]==n-sz+t)t--;if(t<0)break;comb[t]++;for(int j=t+1;j<sz;j++)comb[j]=comb[j-1]+1;
  }
 }
 return false;
}
bool positive_two_cycles(const vector<vector<int>>& T){
 int n=T.size();vector<int>deg(n);for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){if(T[i][j]<0)return false;if(T[i][j])deg[i]++,deg[j]++;}for(int d:deg)if(d!=2)return false;
 vector<int>seen(n);vector<int>sizes;for(int s=0;s<n;s++)if(!seen[s]){int count=0;queue<int>q;q.push(s);seen[s]=1;while(!q.empty()){int u=q.front();q.pop();count++;for(int v=0;v<n;v++)if(T[u][v]&&!seen[v])seen[v]=1,q.push(v);}sizes.push_back(count);}sort(sizes.begin(),sizes.end());return sizes==vector<int>({10,10});
}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int count,n;if(!(cin>>count>>n))return 2;int survivors=0,rejected=0;for(int c=0;c<count;c++){vector<vector<int>>T(n,vector<int>(n));for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){int x;cin>>x;T[i][j]=T[j][i]=x;}vector<vector<int>>G=T;for(int i=0;i<n;i++)G[i][i]=2;if(has_negative_minor(G)){rejected++;continue;}assert(positive_two_cycles(T));survivors++;}cout<<"FILTER "<<count<<" "<<rejected<<" "<<survivors<<"\n";assert(survivors==1);}
