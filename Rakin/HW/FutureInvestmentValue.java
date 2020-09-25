import java.util.Scanner;

public class FutureInvestmentValue {

   public static void main(String[] args) {
   
      Scanner in = new Scanner(System.in);
   
      System.out.print("Enter the investment amount: ");
      double investment = in.nextDouble();
      
      System.out.print("Enter the annual interest rate: ");
      double monthlyInterestRate = in.nextDouble()/1200;
      
      System.out.print("Enter the number of years: ");
      int numberOfYears = in.nextInt();
   
      double futureInvestmentValue = 
         investment * Math.pow(1 + monthlyInterestRate, numberOfYears * 12);
   	
      System.out.println("Accumulated value is $" + futureInvestmentValue);
   }
}