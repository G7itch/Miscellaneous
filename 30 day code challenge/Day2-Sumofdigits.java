import java.util.*;  

public class ScannerPractice
{
    static Scanner sc= new Scanner(System.in);
    public static void main(String[] args)  
    {  
        System.out.print("Enter number- ");
        int number = sc.nextInt();
        int total = 0;
        while (number > 0) {
 
            // Finding the remainder (Last Digit)
            int remainder = number % 10;
 
            // Printing the remainder/current last digit
            total = total + remainder;
 
            // Removing the last digit/current last digit
            number = number / 10;
        }
        System.out.println(total);
    } 
} 