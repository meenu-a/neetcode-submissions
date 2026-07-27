class Solution {
public:
    bool isValid(string s) 
    {
        stack<char> paren;

        for(char p : s)
        {
            if(p == '(' || p == '{' || p == '[')
            {
                paren.push(p);
            }
            else if(p == ')')
            {
                if(paren.empty() || paren.top() != '(')
                {
                    return false;
                }
                paren.pop();
            }            
            else if(p == '}')
            {
                if(paren.empty() || paren.top() != '{')
                {
                    return false;
                }
                paren.pop();
            }            
            else if(p == ']')
            {
                if(paren.empty() || paren.top() != '[')
                {
                    return false;
                }
                paren.pop();
            }
        }
        return paren.empty();
    }
};
