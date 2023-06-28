import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Stream;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); 
		int n = Integer.parseInt(sc.nextLine());
		for(int i = 0; i < n; i++) {
			String s = sc.nextLine();
			int size = Integer.parseInt(s.split(" ")[0]);
	        int[] score = Stream.of(Arrays.copyOfRange(s.split(" "), 1, s.split(" ").length)).mapToInt(Integer::parseInt).toArray();
	        int total = 0;
	        for(int j = 0 ; j < score.length; j++) {
	        	total += score[j];
	        }
	        double avg = total / (double)size;

	        int count = 0;
	        for(int j = 0; j < score.length; j++) {
	        	if((double)score[j] > avg) {
	        		count ++;
	        	}
	        }
	        
	        double f = (count/(double)size * 100);
	        System.out.printf("%.3f%%\n", f);

		}
		sc.close();
	}
}
