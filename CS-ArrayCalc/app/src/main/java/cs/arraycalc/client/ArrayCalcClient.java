package cs.arraycalc.client;
import java.net.Socket;
import java.io.*;
import java.util.StringTokenizer;
public class ArrayCalcClient {
    public static void main(String[] args) throws Exception {
        // This part handles the arguments based on the protocol:
        String command = args[0];
        int size = Integer.parseInt(args[1]);
        String arrayElements = args[2];
        StringTokenizer tokenizer = new StringTokenizer(arrayElements, ",");
        
        int[] array = new int[tokenizer.countTokens()];
        int index = 0;
        while (tokenizer.hasMoreTokens()) {
            array[index++] = Integer.parseInt(tokenizer.nextToken());
        }

                // Convert array to comma-separated format for the header
        StringBuilder arrayAsString = new StringBuilder();
            for (int i = 0; i < array.length; i++) {
                arrayAsString.append(array[i]);
                if (i < array.length - 1) arrayAsString.append(",");
        }

        // This is where we generate and send the headers! (Again, BASED ON THE PROTOCOL!)
        try(Socket serverConnection = new Socket("localhost", 9999)){
            InputStream in = serverConnection.getInputStream();
            OutputStream out = serverConnection.getOutputStream();
            BufferedReader headerReader = new BufferedReader(new InputStreamReader(in));
            BufferedWriter headerWriter = new BufferedWriter(new OutputStreamWriter(out));

            if (command.equals("sort")) {
                // Construct header based on protocol: "sort size array\n"
                String header = "sort " + size + " " + arrayAsString.toString() + "\n";
                headerWriter.write(header);
                headerWriter.flush();

                // Read response from server
                String responseHeader = headerReader.readLine();

                if ("INVALID INPUT".equals(responseHeader)) {
                    System.out.println("Sorry, Invalid input! Try again.");
                } else if ("SORTED".equals(responseHeader)) {
                    // Read and print the sorted array from the server
                    String sortedArray = headerReader.readLine();
                    System.out.println("Sorted Array: " + sortedArray);
                } else {
                    System.out.println("Unexpected server response: " + responseHeader);
                }

            } if (command.equals("max")){
                String header = "max " + size + " " + arrayAsString + "\n";
                headerWriter.write(header);
                headerWriter.flush();

                String responseHeader = headerReader.readLine();

                if("INVALID INPUT".equals(responseHeader)){
                    System.out.println("Sorry, Invalid input! Try again.");
                } else if ("MAX".equals(responseHeader)){
                    int max = Integer.parseInt(responseHeader);
                    System.out.println("Maximum value: " + max);
                }
            } else {
                System.out.println("Unexpected server response: ");
            }
        }
    }
}
