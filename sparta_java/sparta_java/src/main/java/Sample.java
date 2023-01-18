//class ArrayCalculation {
//
//    int[] arr = { 0, 1, 2, 3, 4 };
//
//    public int divide(int denominatorIndex, int numeratorIndex)
//            throws ArithmeticException, ArrayIndexOutOfBoundsException {
//        return arr[denominatorIndex] / arr[numeratorIndex];
//    }
//}
//
//public class Sample {
//    public static void main(String[] args) {
//        ArrayCalculation arrayCalculation = new ArrayCalculation();
//
//        System.out.println("2 / 1 = " + arrayCalculation.divide(2, 1));
//        try {
//            System.out.println(
//                    "1 / 0 = " + arrayCalculation.divide(1, 0));
//        } catch (ArithmeticException arithmeticException) {
//            System.out.println("잘못된 계산입니다. " + arithmeticException.getMessage());
//        }
//        try {
//            System.out.println("Try to divide using out of index element = "
//                    + arrayCalculation.divide(5, 0));
//        } catch (ArrayIndexOutOfBoundsException arrayIndexOutOfBoundsException) {
//            System.out.println(
//                    "잘못된 index 범위로 나누었습니다. 타당 index 범위는 0부터" + (arrayCalculation.arr.length - 1) + "까지 입니다.");
//        }
//    }
//
//}