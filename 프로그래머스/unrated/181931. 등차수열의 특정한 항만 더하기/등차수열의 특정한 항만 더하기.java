class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        int n = a;
        for(boolean flag : included) {
            answer += flag ? n : 0;
            n+=d;
        }
        return answer;
    }
}