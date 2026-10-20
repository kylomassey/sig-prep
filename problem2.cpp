#include <iostream>
#include <vector>
#include<map>
using namespace std;

vector<vector<long long>> binary_search(vector<vector<long long>> prices, long long price, long long pos){
    int l = 0;
    int r = prices.size() - 1;
    int mid = 0;
    while (l <= r){
        mid = 1 + (r - l) / 2;
        if(price == prices[mid][0]){
            prices.insert(prices.begin() + mid + 1, {price, pos});
            return prices;
        }
        if(price > prices[mid][0]) l = mid + 1;
        if(price > prices[mid][0]) r = mid - 1;
    }
    if(price > prices[mid][0]){
        prices.insert(prices.begin() + mid + 1, {price, pos});
    }else{
        prices.insert(prices.begin() + mid, {price, pos});
    }
    return prices;
}

int main() {
    char side;
    long long id, qty, price;
    map<long long,map<string, long long>> sells;
    vector<vector<long long>> buys;
    vector<vector<long long>> sellorder;
    vector<vector<long long>> trades;
    int i = 0;
    while (cin >> side >> id >> qty >> price) {
        if(side == 'B'){
            if(!sellorder.empty()){
                i = 0;
                while(i < sellorder.size()){
                    if (sellorder[i][0] <= price){
                        if (qty >= sells[sellorder[i][1]]["qty"]){
                            qty -= sells[sellorder[i][1]]["qty"];
                            trades.push_back({id, sellorder[i][1],sells[sellorder[i][1]]["qty"], sellorder[i][0]});
                            sells.erase(sellorder[i][1]);
                        }else{
                            sells[sellorder[i][1]]["qty"] -= qty;
                            trades.push_back({id, sellorder[i][1],qty, sellorder[i][0]});
                            qty = 0;
                            break;
                        }

                    }
                    i++;
                }
            }
            if (qty != 0) buys.push_back({id, qty, price});
        }
        if(side == 'S'){ 
            if(!buys.empty()){
                i = 0;
                while(i < buys.size()){
                    if(buys[i][2] >= price){
                        if (qty >= buys[i][1]){
                            qty -= buys[i][1];
                            trades.push_back({buys[i][0], id, buys[i][1], price});
                            buys.erase(buys.begin() + i);
                        }else{
                            buys[i][1] -= qty;
                            trades.push_back({buys[i][0], id, qty, price});
                            qty = 0;
                            break;
                        }
                    }
                    i++;
                }
            }
            if(qty != 0){
                if(sellorder.empty()) sellorder.push_back({price, id});
                else sellorder = binary_search(sellorder, price, id);
                sells[id] = {("qty", qty), ("price", price)};
            }
        }
    }
    for(auto trade : trades){
        cout << "TRADE" << trade[0] << "\t" << trade[1] << "\t" << trade[2] << "\t" << trade[3] << endl;
    }
}