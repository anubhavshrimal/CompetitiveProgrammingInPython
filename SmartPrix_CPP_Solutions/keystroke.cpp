#include <bits/stdc++.h>
using namespace std;
int main() {
    string inputStr;
    getline(cin, inputStr);
    vector < string > outputText; //output text arr
    outputText.push_back("");
    bool caps = 0; //capslock flag
    int currX = 0, currY = 0; //cursor variables

    // Start reading text
    for (int i = 0; i < inputStr.length(); i++) {
        // If character is alphanumeric or space
        if ((inputStr[i] >= 'a' && inputStr[i] <= 'z') || (inputStr[i] >= 'A' && inputStr[i] <= 'Z') || (inputStr[i] >= '0' && inputStr[i] <= '9') || inputStr[i] == ' ') {
            char temp;
            if (caps && (inputStr[i] >= 'a' && inputStr[i] <= 'z')) temp = inputStr[i] - 'a' + 'A';
            else temp = inputStr[i];
            if (currY == outputText[currX].length()) outputText[currX].push_back(temp);
            else outputText[currX].insert(outputText[currX].begin() + currY, temp);
            currY++;
        }

        // If current input character is '#', Newline 
        else if (inputStr[i] == '#') {
            currX++;
            outputText.insert(outputText.begin() + currX, outputText[currX - 1].substr(currY));
            outputText[currX - 1] = outputText[currX - 1].substr(0, currY);
            currY = 0;
        }
        
        // If current input character is '@', change capslock state
        else if (inputStr[i] == '@')
            caps = (caps + 1) % 2;

        // If current character is '<', shift left
        else if (inputStr[i] == '<') {
            if (currX == 0 && currY == 0) continue;
            if (currY > 0) {
                currY--;
                continue;
            }
            currX--;
            currY = outputText[currX].length();
        }

        // If current character is '>', shift right
        else if (inputStr[i] == '>') {
            if (currX == outputText.size() - 1 && currY == outputText[currX].length()) continue;
            if (currY < outputText[currX].length()) currY++;
            else if (currX < outputText.size() - 1) currX++, currY = 0;
        }

        // If current character is '/', delete previous char and shift left
        else if (inputStr[i] == '/') {
            if (currX == 0 && currY == 0) continue;
            if (currY > 0) {
                outputText[currX].erase(outputText[currX].begin() + currY - 1), currY--;
                continue;
            }
            string temp = outputText[currX];
            outputText.erase(outputText.begin() + currX);
            currX--;
            currY = outputText[currX].length();
            outputText[currX] += temp;
        } else if (inputStr[i] == '^') {
            if (currX == 0) {
                while (inputStr[i] == '^') i++;
                i--;
                continue;
            }
            while (inputStr[i] == '^' && currX > 0) currX--, i++;
            while (inputStr[i] == '^') i++;
            if (currY > outputText[currX].length()) currY = outputText[currX].length();
            if (outputText[currX].length() == 0) currY = 0;
            i--;
        } else if (inputStr[i] == '?') {
            if (currX == outputText.size() - 1) {
                while (inputStr[i] == '?') i++;
                i--;
                continue;
            }
            while (inputStr[i] == '?' && currX < outputText.size() - 1) currX++, i++;
            while (inputStr[i] == '?') i++;
            if (currY > outputText[currX].length()) currY = outputText[currX].length();
            if (outputText[currX].length() == 0) currY = 0;
            i--;
        }
    }

    // Output the final text
    for (int i = 0; i < outputText.size(); i++) 
        cout << outputText[i] << endl;
    return 0;
}