import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
		//int N  = 5;
		
		for (int i = N; i > 0; i--) {
			for(int j = 0 ; j < N-i; j++){
				System.out.print(" ");
			}
			for (int j = 0; j < i*2-1; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
		sc.close();
	}
}
