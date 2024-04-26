package problem;


/*
 * Problem Number: 13
 * https://leetcode.com/problems/roman-to-integer/description/
 */
public class RomanToInteger {
    public static void main(String[] args) {
        RomanToInteger romanToInteger = new RomanToInteger();
        System.out.println(romanToInteger.romanToInt("MCMXCIV"));
    }

    public int romanToInt(String s) {
        int length = s.length();
        int startIdx = 0;
        int sum = 0;
        while (startIdx < length) {
            sum += getRealNumber(s.charAt(startIdx));
            if (startIdx > 0) {
                if (s.charAt(startIdx) == 'V' || s.charAt(startIdx) == 'X') {
                    if (s.charAt(startIdx - 1) == 'I') {
                        sum -= 2;
                    }
                }
                if (s.charAt(startIdx) == 'L' || s.charAt(startIdx) == 'C') {
                    if (s.charAt(startIdx - 1) == 'X') {
                        sum -= 20;
                    }
                }
                if (s.charAt(startIdx) == 'D' || s.charAt(startIdx) == 'M') {
                    if (s.charAt(startIdx - 1) == 'C') {
                        sum -= 200;
                    }
                }
            }
            startIdx++;
        }
        return sum;
    }

    private int getRealNumber(char c) {
        return RomanNumber.getNumberOf(c);
    }

    public enum RomanNumber {
        I(1),
        V(5),
        X(10),
        L(50),
        C(100),
        D(500),
        M(1000);
        private final int number;

        RomanNumber(int number) {
            this.number = number;
        }

        public static int getNumberOf(char c) {
            return RomanNumber.valueOf(String.valueOf(c)).getNumber();
        }

        public int getNumber() {
            return this.number;
        }
    }
}
