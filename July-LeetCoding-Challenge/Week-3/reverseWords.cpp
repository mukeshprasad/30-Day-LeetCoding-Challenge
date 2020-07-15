/* Reverse Words in a String

# SOLUTION:
  O(N) Time and O(1) Space
  First, reverse the whole string, then reverse each word.
*/
void reverseWords(string &s){
    reverse(s.begin(), s.end());
    int storeIndex = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] != ' '){
            if(storeIndex != 0) storeIndex++ ;
            int j = i;
            while(j < s.size() && s[j] != ' ') j++;
            reverse(s.begin() + storeIndex, s.begin() + j);
            storeIndex += (j - i);
            i = j;
        }
    }
    s.erase(s.begin() + storeIndex, s.end());
} 
