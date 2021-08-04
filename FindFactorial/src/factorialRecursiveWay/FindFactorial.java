package factorialRecursiveWay;

import java.util.Scanner;

public class FindFactorial {
	
	public static long multipyNumbers(long input) {
		if (input >= 1) {
			return input * multipyNumbers(input - 1);
		}
		else {
			return 1;
		}
	}
	
	@SuppressWarnings("all")
	
	public static void main(String[] args) {
		System.out.println("Enter number:");
		Scanner scanner = new Scanner(System.in);
		long input = scanner.nextInt();
		long factorial = multipyNumbers(input);
		System.out.println("Factorial of " + input + " is: " + factorial);
		
	}

}
