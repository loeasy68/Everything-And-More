public class stringFormat {
  public static void main(String[] args) {
    String myStr = "Hello %s! One kilobyte is %,d bytes.";
    String result = String.format(myStr, "World", 1024);
    System.out.println(result);
  }
}