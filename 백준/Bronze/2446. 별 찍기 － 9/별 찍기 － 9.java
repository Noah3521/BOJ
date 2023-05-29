import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		for (int i = N; i > 1; i--) {
			for (int k = i; k < N; k++) {
				System.out.print(" ");
			}
			for (int j = i * 2 - 1; j > 0; j--) {
				System.out.print("*");
			}
			System.out.println();
		}
		for (int i = 1; i < N+1; i++) {
			for (int k = i; k < N; k++) {
				System.out.print(" ");
			}
			for (int j = i * 2 - 1; j > 0; j--) {
				System.out.print("*");
			}
			System.out.println();
		}
//		System.out.println("********* ");
//		System.out.println(" ******* ");
//		System.out.println("  ***** ");
//		System.out.println("   *** ");
//		System.out.println("    * ");
//		System.out.println("   *** ");
//		System.out.println("  ***** ");
//		System.out.println(" ******* ");
//		System.out.println("********* ");
		sc.close();
	}
}
