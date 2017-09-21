#include <bits/stdc++.h>
using namespace std;

map<string, int> dict;

void addUtil(string a, string b, string c)
{
    if (dict.find(a) != dict.end()) {
        dict[c] = dict[a];
    }
    else {
        dict[c] = stoi(a);
    }
    if (dict.find(b) != dict.end()) {
        dict[c] += dict[b];
    }
    else {
        dict[c] += stoi(b);
    }
}

void echoUtil(string str)
{
    if (dict.find(str) != dict.end()) {
        cout << dict[str] << "\n";
    }
    else if (str[0] >= 48 && str[0] <= 57) {
        cout << str << "\n";
    }
    else {
        cout << "0\n";
    }
}

void setUtil(string str, string secondStr)
{
    if (dict.find(secondStr) != dict.end()) {
        dict[str] = dict[secondStr];
    }
    else if (secondStr[0] >= 48 && secondStr[0] <= 57) {
        dict[str] = stoi(secondStr);
    }
    else {
        dict[str] = 0;
    }
}

int main()
{
    int line = 0;
    string codeTxt[1000][4], str, a, b, c;

    map<string, int> label;
    
    while ((cin >> str)) {
        if (str == "SET") {
            cin >> a >> b;
            codeTxt[line][0] = str;
            codeTxt[line][1] = a;
            codeTxt[line][2] = b;
        }
        else if (str == "ECHO") {
            cin >> a;
            codeTxt[line][0] = str;
            codeTxt[line][1] = a;
        }
        else if (str == "EXIT") {
            codeTxt[line][0] = str;
        }
        else if (str == "ADD") {
            cin >> a >> b >> c;
            codeTxt[line][0] = str;
            codeTxt[line][1] = a;
            codeTxt[line][2] = b;
            codeTxt[line][3] = c;
        }
        else if (str == "LABEL") {
            string val;
            cin >> val;
            label[val] = line;
        }
        else if (str == "GOTO") {
            string val;
            cin >> val;
            codeTxt[line][0] = str;
            codeTxt[line][1] = val;
        }
        else if (str == "IF") {
            cin >> a >> b;
            codeTxt[line][0] = str;
            codeTxt[line][1] = a;
            codeTxt[line][2] = b;
        }
        else if (str == "END") {
            codeTxt[line][0] = str;
        }
        else if (str == "CONTINUE") {
            codeTxt[line][0] = str;
        }
        if (str != "LABEL")
            line++;
    }

    int num = line;
    line = 0;
    stack<bool> flagStack;

    stack<int> codeStack;
    flagStack.push(true);
    while (line < num) {
        str = codeTxt[line][0];
        bool flag = flagStack.top();

        if (str == "SET" && flag) {
            setUtil(codeTxt[line][1], codeTxt[line][2]);
            line++;
        }
        else if (str == "ECHO" && flag) {
            echoUtil(codeTxt[line][1]);
            line++;
        }
        else if (str == "EXIT" && flag) {
            return 0;
        }
        else if (str == "ADD" && flag) {
            addUtil(codeTxt[line][1], codeTxt[line][2], codeTxt[line][3]);
            line++;
        }
        else if (str == "GOTO" && flag) {
            line = label[codeTxt[line][1]];
        }
        else if (str == "IF") {
            int t1, t2;
            if (!flag) {
                flagStack.push(false);
            }
            else {
                if (dict.find(codeTxt[line][2]) != dict.end()) {
                    t2 = dict[codeTxt[line][2]];
                }
                else if (codeTxt[line][2][0] >= 48 && codeTxt[line][2][0] <= 57) {
                    t2 = stoi(codeTxt[line][2]);
                }
                else {
                    t2 = 0;
                }
                if (dict.find(codeTxt[line][1]) != dict.end()) {
                    t1 = dict[codeTxt[line][1]];
                }
                else if (codeTxt[line][1][0] >= 48 && codeTxt[line][1][0] <= 57) {
                    t1 = stoi(codeTxt[line][1]);
                }
                else {
                    t1 = 0;
                }
                if (t1 != t2) {
                    flagStack.push(false);
                }
            }
            codeStack.push(line);
            line++;
        }
        else if (str == "END") {
            flagStack.pop();
            if (flagStack.empty()) {
                flagStack.push(true);
            }
            line++;
            codeStack.pop();
        }
        else if (str == "CONTINUE" && flag) {
            line = codeStack.top();
        }
        else {
            line++;
        }
    }
    return 0;
}
