/*
Author: Anya Hossaini
Date: 12.17.2020

Problem: Create a public class called Cube without a constructor which gets one single private integer variable Side, 
a getter GetSide() and a setter SetSide(int num) method for this property. Actually, getter and setter methods are not 
the common way to write this code in C#. In the next kata of this series, we gonna refactor the code and make it a bit more professional...

Coding Language: Java
*/

public class Cube {

    // note: use primitive data type for the side of the cube
    private int side;

    public int getSide(){
        return side;
    }

    public void setSide(int num){
        this.side = num;
    }

}
