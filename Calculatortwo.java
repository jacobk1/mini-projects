import java.util.Scanner;
 public class Calculatortwo {
   public static void main(String[] args) {
   //get imput values from user
      System.out.print("Enter the first value ");
      Scanner scan = new Scanner(System.in);
      double x = scan.nextDouble();
      
      System.out.println("Choose an operation: 1-multiply 2-divide 3-add 4-subtract");
      int operation = scan.nextInt();
      
      System.out.print("Enter the next value ");
      double y = scan.nextDouble();
      
      if (operation == 2 && y == 0)
         System.out.println("Error: Divide By Zero");
      else{
         //calculator logic
         double result = 0;
         switch (operation) {
            case 1:
               result = x * y;
               break;
            
            case 2: 
               result = x / y;
               break;
            
            case 3:
               result = x + y;
               break;
               
            case 4:
               result = x - y;
               break;
               
            default:
               System.out.println("Error: operation not found");
         }
      System.out.println("Result: " + result);
      }
         

   }
}