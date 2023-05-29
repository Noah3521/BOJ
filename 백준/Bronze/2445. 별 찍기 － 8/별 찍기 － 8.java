import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N-1; j++) {
				if (i >= j)
					System.out.print("*");
				else if (j != N - 1)
					System.out.print(" ");
			}
			for (int j = N; j >= 0; j--) {
				if (i < j && i != N - 1)
					System.out.print(" ");
				else
					System.out.print("*");
			}
			System.out.println();
		}

		for (int i = 0; i < N - 1; i++) {
			for (int j = N - 1 - i; j > 0; j--) {
				System.out.print("*");
			}
			for (int j = 0; j < (i+1)*2;j++) {
				System.out.print(" ");
			}
			for (int j = 0; j < N - 1 - i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
//
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print(" ");
//
//		System.out.print(" ");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.println();
//
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print(" ");
//		System.out.print(" ");
//
//		System.out.print(" ");
//		System.out.print(" ");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.print("*");
//		System.out.println();
        sc.close();
	}
}