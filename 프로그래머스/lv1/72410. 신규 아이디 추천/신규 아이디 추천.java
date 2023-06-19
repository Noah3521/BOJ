class Solution {
	public String solution(String s1) {
		String answer = "";
		
		s1 = s1.toLowerCase(); // 1
//		System.out.println("1 \t: " + s1);
		
		//2
		String myFilter = "abcdefghijklmnopqrstuvwxyz0123456789-_.";
		for(int i = 0; i < s1.length();i++) {
			char ch = s1.charAt(i);
			if(myFilter.contains(ch+"")) {
				answer += ch;
			}
		}
//		System.out.println(answer);
//		System.out.println("2 \t: " + answer);
		
		//===================================
		
		while(answer.contains("..")) {
			answer = answer.replace("..", ".");
		}
		
		//===================================
		
		if(answer.startsWith("."))		// 4-1
			answer = answer.replaceFirst(".", "");
//		System.out.println("4-1 \t: " + answer);
		if(answer.endsWith(".")) {	// 4-2
			answer = answer.substring(0, answer.length()-1);
		}
//		System.out.println("4-2 \t: " + answer);
		
		// ====================================
		
		if(answer.length()==0) {
			answer = " ";
		}
		
		answer = answer.replace(" ", "a"); // 5
		
		//=====================================
		
		if (answer.length() >= 16) 	{// 6 
			answer = answer.substring(0, 15);
			if(answer.endsWith(".")) {	// 4-2
				answer = answer.substring(0, answer.length()-1);
			}
		}
		
		//=======================
		

		if(answer.length() <= 2) {	// 7
			while(answer.length() < 3) {
				answer += answer.charAt(answer.length()-1);
			}
		}
//		System.out.println("7 \t: " + answer);
		
		return answer;
	}
}