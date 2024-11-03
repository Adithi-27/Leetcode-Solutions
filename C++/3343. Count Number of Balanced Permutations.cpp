#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
typedef long long ll;

vector<ll> fact;
vector<ll> inv_fact;

ll power_mod_func(ll a, ll b) {
    ll res = 1;
    a %= MOD;
    while(b > 0){
        if(b & 1) res = res * a % MOD;
        a = a * a % MOD;
        b >>= 1;
    }
    return res;
}

void init_fact(int n){
    fact.assign(n +1, 1);
    for(int i=1; i<=n; i++) fact[i] = fact[i-1] * i % MOD;
    inv_fact.assign(n +1, 1);
    inv_fact[n] = power_mod_func(fact[n], MOD-2);
    for(int i=n-1; i>=0; i--) inv_fact[i] = inv_fact[i+1] * (i+1) % MOD;
}

class Solution {
public:
    int countBalancedPermutations(string num) {
        int n = num.size();
        string velunexorai = num;
        string lomiktrayve = num;

        int freq[10] = {0};
        ll total_sum =0;
        for(char c:num) {
            int d = c - '0';
            freq[d]++;
            total_sum += d;
        }

        if(total_sum %2 !=0) return 0;
        ll sum_half = total_sum /2;
        int k = (n +1)/2;

        init_fact(n);

        vector<vector<ll>> dp(k+1, vector<ll>(sum_half +1, 0));
        dp[0][0] =1;

        for(int d=0; d<=9; d++){
            if(freq[d]==0) continue;
            for(int c=k; c>=0; c--){
                for(ll s=sum_half; s>=0; s--){
                    if(dp[c][s]==0) continue;
                    for(int t=1; t<=min(freq[d], k -c); t++){
                        if(s + (ll)d * t > sum_half) break;
                        ll comb = (fact[freq[d]] * inv_fact[t] % MOD) * inv_fact[freq[d] - t] % MOD;
                        dp[c + t][s + d * t] = (dp[c + t][s + d * t] + dp[c][s] * comb) % MOD;
                    }
                }
            }
        }

        ll valid_assignments = dp[k][sum_half];
        if(valid_assignments ==0) return 0;

        ll prod_fact_fd =1;
        for(int d=0; d<=9; d++){
            prod_fact_fd = prod_fact_fd * fact[freq[d]] % MOD;
        }

        ll fk_fnk = (fact[k] * fact[n -k]) % MOD;
        ll inv_prod_fact_fd = power_mod_func(prod_fact_fd, MOD -2);
        ll answer = (fk_fnk * valid_assignments) % MOD;
        answer = (answer * inv_prod_fact_fd) % MOD;

        return (int)answer;
    }
};

