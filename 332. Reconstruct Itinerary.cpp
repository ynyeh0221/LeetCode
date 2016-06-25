#include <unordered_map>
#include <stack>
class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {  
        vector<string> res;
        map<string, multiset<string>> fromto;  
        for(auto val:tickets)
            fromto[val.first].insert(val.second);
        stack <string> s;  
        s.push("JFK");
        
        while(!s.empty())
        {  
            string temp=s.top();  
            if(fromto.find(temp) != fromto.end() && fromto[temp].size() > 0)  
            {  
                s.push(*fromto[temp].begin());
                fromto[temp].erase(fromto[temp].begin());
            }
            else
            {
                res.insert(res.begin(), temp);
                s.pop();
            }
        }
        return res;  
    }  
};
