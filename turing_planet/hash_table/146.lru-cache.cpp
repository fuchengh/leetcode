/*
 * @lc app=leetcode id=146 lang=cpp
 *
 * [146] LRU Cache
 */

// @lc code=start
class LRUCache
{
  public:
    using KV = pair<int, int>;
    list<KV>                               lruList;   // stores actual [key, value]
    unordered_map<int, list<KV>::iterator> keyTable;  // stores the position of key in list
    int                                    maxCap;

    LRUCache(int capacity) { maxCap = capacity; }

    void moveKVToFront(int key, int value)
    {
        // get original position
        auto keyIt = keyTable[key];
        lruList.push_front({key, value});
        lruList.erase(keyIt);
        keyTable[key] = lruList.begin();
    }

    int get(int key)
    {
        if (!keyTable.count(key))
            return -1;
        auto keyIt      = keyTable[key];
        auto [k, value] = *keyIt;  // deref iterator and get the pair

        // reposition: put it to the front of the list
        moveKVToFront(key, value);

        return value;
    }

    void put(int key, int value)
    {
        if (!keyTable.count(key))
        {
            lruList.push_front({key, value});
            keyTable[key] = lruList.begin();
            // remove lru if size > maxCap
            if (keyTable.size() > maxCap)
            {
                auto lruIt            = prev(lruList.end());
                auto [lruKey, lruVal] = *lruIt;
                lruList.pop_back();
                keyTable.erase(lruKey);
            }
        }
        else  // update value and move it to the front
        {
            moveKVToFront(key, value);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end
