class Solution {
public:
    int calPoints(vector<string>& operations) 
    {
        stack<int> record;
        for(string s : operations)
        {
            if(s == "+")
            {
                int op2 = record.top();
                record.pop();
                int op1 = record.top();
                record.push(op2);
                record.push(op1+op2);
            }
            else if(s == "D")
            {
                int prev = record.top();
                record.push(prev*2);
            }
            else if (s == "C")
            {
                record.pop();
            }
            else
            {
                int num = stoi(s);
                record.push(num);
            }
        }

        int sum = 0;
        while(! record.empty())
        {
            sum += record.top();
            record.pop();
        }

        return sum;
    }
};