#include <stdio.h>
#include <string.h>

int cnt = 0;
int recursion(const char* s, int l, int r) {
    cnt += 1;
    if (l >= r) return 1;
    else if (s[l] != s[r]) return 0;
    else return recursion(s, l + 1, r - 1);
}

int isPalindrome(const char* s) {
    
    return recursion(s, 0, strlen(s) - 1);
}

int main() {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        cnt = 0;
        char word[1000];
        scanf("%s", word);
        int res1 = isPalindrome(word);
        printf("%d %d\n", res1, cnt);
    }
}