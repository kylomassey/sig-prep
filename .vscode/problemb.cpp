#include <iostream>
#include <map>
#include <vector>
#include <bits/stdc++.h>


int main(){
    struct Trader {
        std::deque<std::pair<long long, long long>> window; 
        long long best = 0; 
        long long total = 0;
    };
    struct Trade {long long t; std::string tr; long long n;};
    int n;
    int w;
    std::cin >> n >> w;
    std::vector<Trade> feed;
    std::map<std::string, Trader> traders;
    long long timestamp;
    std::string name;
    long long notional;
    long long temp;
    std::vector<std::pair<std::string, long long>> ans;
    for(int i = 0; i < n; i ++){
        std::cin >> timestamp >> name >> notional;
        feed.push_back({timestamp, name, notional});
    }
    sort(feed.begin(), feed.end(), [](const Trade& a, const Trade& b) {
    return a.t < b.t;
    });
    for(const auto& [timestamp, name, notional]: feed){
        if(!traders.count(name)){
            traders.insert({name, Trader()});
        }
        while(traders[name].window.size() != 0 && timestamp - traders[name].window.front().first >= w){
            temp = traders[name].window.front().second;
            traders[name].window.pop_front();
            traders[name].total -= temp;
        }
        traders[name].window.push_back({timestamp, notional});
        traders[name].total += notional;
        traders[name].best = std::max(traders[name].total, traders[name].best);
    }
    for(const auto& [name, entry]: traders){
        ans.push_back({name,entry.best});
    }
    sort(ans.begin(), ans.end(), [](std::pair<std::string, long long> a, std::pair<std::string, long long> b) {
    return a.second > b.second;
    });
    for(const auto& [name, entry]: ans){
        std::cout << name << " " << entry << "\n";
    }
}