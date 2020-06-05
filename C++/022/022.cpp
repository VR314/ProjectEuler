#include <iostream>
#include <set>
#include <fstream>

/*
*	Problem #: 022
*	Date Attempted: 06/04/20
*	Date Solved: 06/04/20
*
*	What is the total of all the name scores in the file?
*
*	Answer: 871198282
*/

long alphabeticalScore(std::string s) {
    int n = s.length();
    char* chararray = new char[n+1];
    strcpy_s(chararray, (size_t)(n+1), s.c_str());

    long sum{ 0 };
    for (int i = 0; i < n; i++) {
        char c = chararray[i];
        sum += (int)c - 64;
    }
    std::cout << s << " " << sum << std::endl;
    delete(chararray);
    return sum;
}

int main()
{
    std::ifstream fin("names.txt");

    std::set<std::string> sortedNames{};
    std::string s;
    fin >> s;
    std::string delimiter = "\",\"";

    size_t pos = 0;
    std::string token;
    s.erase(0, 1);
    while ((pos = s.find(delimiter)) != std::string::npos) 
    {
        token = s.substr(0, pos);
        sortedNames.insert(token);
        s.erase(0, pos + delimiter.length());
    }
    s.erase(s.end() - 1, s.end());
    sortedNames.insert(s);

    long long int sum{ 0 };
    int index = 0;
    for (auto it = sortedNames.begin(); it != sortedNames.end(); ++it) {
        index++;
        std::cout << *it << std::endl;
        long long int nameScore = (index) * alphabeticalScore(*it);
        sum += nameScore;
    }

    std::cout << sum << std::endl;
}
