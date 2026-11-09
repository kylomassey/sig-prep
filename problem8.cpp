#include <iostream>
#include <vector>
#include <map>
#include <bits/stdc++.h>

int main(){
    int n;
    int k;
    std::string symbol;
    int qty;
    std::cin >> n >> k;
    std::vector<std::pair<int, std::string>> tickers2;
    std::map<std::string, int> tickers;
    for(int i = 0; i < n; i++){
        std::cin >> symbol >> qty;
        if (tickers.find(symbol) != tickers.end()){
            tickers[symbol] += qty;
        }else{
            tickers[symbol] = qty;
        }
    }
    for (auto i : tickers){
        tickers2.push_back({i.second, i.first});
    }
    std::sort(tickers2.begin(), tickers2.end());
    for (int i = tickers2.size() - 1; i > tickers2.size() - 1 - k; i--){
        std::cout << tickers2[i].second << " " << tickers2[i].first << "\n";
    }
}