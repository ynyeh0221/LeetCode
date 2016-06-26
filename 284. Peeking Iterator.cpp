// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};


class PeekingIterator : public Iterator {
private:
    int peeked_num = INT_MAX;
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    
	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        if (peeked_num < INT_MAX)
            return peeked_num;
        else
        {
            peeked_num = Iterator::next();
            return peeked_num;
        }
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    if (peeked_num < INT_MAX)
	    {  
            int temp = peeked_num;
            peeked_num = INT_MAX;
            return temp;
        }
        else
            return Iterator::next();
	}

	bool hasNext() const {
        return (Iterator::hasNext() || (!Iterator::hasNext() && peeked_num < INT_MAX) ? true : false);  
	}
};
