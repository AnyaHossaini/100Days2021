/*

Author: Anya Hossaini
Date: 12.17.2020

Problem: Given a string s, write a method (function) that will return true if its a valid single integer
or floating number or false if its not.

Coding Language: Java
*/

import java.util.Scanner; // Import the Scanner class

public class MyUtilities {

    public boolean isDigit(String s) {
        try {
            // Integer.parseInt(s);
            Float.parseFloat(s);
        } 
        catch (NumberFormatException ex) {
            return false;
        }

        return true;

    } // isDigit End

    public void main() {
        Scanner myObj = new Scanner(System.in); // Create a Scanner object
        System.out.println("Enter a number");

        // String input
        String number = myObj.nextLine();
        isDigit(number);

    } // Main end

} // END OF CLASS
