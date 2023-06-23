	class Solution {
	    public int solution(String ineq, String eq, int n, int m) {
	    	boolean flag1 = (ineq.equals(">")&&eq.equals("=")&&n>=m);
	    	boolean flag2 = (ineq.equals("<")&&eq.equals("=")&&n<=m);
	    	boolean flag3 = (ineq.equals(">")&&eq.equals("!")&&(n>=m));
	    	boolean flag4 = (ineq.equals("<")&&eq.equals("!")&&(n<=m));
	    	if(flag1||flag2|flag3|flag4)
                return 1;
            return 0;
	    }
	    
	}