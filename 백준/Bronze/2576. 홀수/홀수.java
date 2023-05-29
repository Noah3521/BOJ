import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int minOdd = 100;
		int totalOdd = 0;
		for(int i = 0; i < 7; i ++) {
			int num = Integer.parseInt(sc.next());
			if(num%2!=0) {
				if(num < minOdd) {
					minOdd = num;
				}
				totalOdd+=num;
			}
		}
		
		System.out.print(totalOdd > 0 ? (totalOdd + "\n" + minOdd) : -1);
		
		sc.close();
	}
}
