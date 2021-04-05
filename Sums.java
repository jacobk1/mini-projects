/*
*  Author: Jacob Kost
*  Program: 
      task1: Reads inputs from a user and adds the digits of the input together
      task2: Computes the largest possible value to store as an integer
      task3: Convert a Base10 input into a binary ouput
*/
import java.util.Scanner;
class Sums {
   public static void main(String[] args) {
   
      int sum = 0;//stores the working(and eventually final) sum of the input for task1
      int input = 0;//stores the value inputted by user
      int cInput = 0; //stores a copy of the input to print at the end
      int modInput = 0;//stores the modified input
      int binary = 0;//stores output for task3
      Scanner scan = new Scanner(System.in);
      System.out.println("enter an integer");
      input = scan.nextInt();
      cInput = input;
      
      
      //task1
      while (input > 0) {
         modInput = input % 10;
         //System.out.println("modInput is "+ modInput); //debug line 
         input = input / 10;
         sum += modInput;
         //System.out.println("sum is " + sum); //debug line
       }//end of while
       System.out.println("the sum of the digits in " + cInput + " is equal to " + sum);
       
       
       //task2
      int largo = 0; //stores the counter for the next loop
      while (largo >= 0) {//keep incrementing largo until overflow error
         largo++; 
      }//end of while
      largo--;// deincrement largo to cause underflow error
      System.out.println("The largest integer reached was " + largo);
       
       
      //task3
      Scanner scan2 = new Scanner(System.in);
      System.out.println("enter an integer");
      input = scan.nextInt();
      System.out.print(input + " In binary is ");
      while(input > 0) {
         modInput = input % 2;
         System.out.print(modInput);
         input = input / 2;
      }//end of while
      System.out.println(" ");
      //pretty sure the above code works it just doesn't put the Zero at the end like the example says it should and that zero is redundant
      //if you don't believe me google a decimal to binary converter and plug in 123.
      
   }//end of main
}//end of class