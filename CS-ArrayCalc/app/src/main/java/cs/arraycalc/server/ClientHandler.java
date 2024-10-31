package cs.arraycalc.server;

import java.net.Socket;
import java.io.*;
import java.util.*;

public class ClientHandler {
    private InputStream in; 
    private OutputStream out;
    private BufferedReader headerReader;
    private BufferedWriter headerWriter;

    public ClientHandler(Socket clientConnection) throws Exception {
        in = clientConnection.getInputStream();
        out = clientConnection.getOutputStream();
        headerReader = new BufferedReader(new InputStreamReader(in));
        headerWriter = new BufferedWriter(new OutputStreamWriter(out));
        interact();
    }

    // Main interaction loop
    public void interact() throws Exception {
        String command;
        
        // Loop to keep processing client requests
        while ((command = headerReader.readLine()) != null) {
            String[] commandParts = command.split(" ");
            
            // Determine operation type
            switch (commandParts[0]) {
                case "sort":
                    handleSort(commandParts);
                    break;
                case "max":
                    handleMax(commandParts);
                    break;
                case "min":
                    handleMin(commandParts);
                    break;
                case "add":
                    handleAdd(commandParts);
                    break;
                case "multiply":
                    handleMultiply(commandParts);
                    break;
                default:
                    sendInvalidInput();
            }
        }
    }

    // Handles "sort" command
    private void handleSort(String[] commandParts) throws IOException {
        try {
            int[] array = parseArray(commandParts, 2);
            Arrays.sort(array);
            headerWriter.write("SORTED\n");
            headerWriter.write(arrayToString(array) + "\n");
            headerWriter.flush();
        } catch (Exception e) {
            sendInvalidInput();
        }
    }

    // Handles "max" command
    private void handleMax(String[] commandParts) throws IOException {
        try {
            int[] array = parseArray(commandParts, 2);
            int maxValue = Arrays.stream(array).max().orElseThrow();
            headerWriter.write("MAX " + maxValue + "\n");
            headerWriter.flush();
        } catch (Exception e) {
            sendInvalidInput();
        }
    }

    // Handles "min" command
    private void handleMin(String[] commandParts) throws IOException {
        try {
            int[] array = parseArray(commandParts, 2);
            int minValue = Arrays.stream(array).min().orElseThrow();
            headerWriter.write("MIN " + minValue + "\n");
            headerWriter.flush();
        } catch (Exception e) {
            sendInvalidInput();
        }
    }

    // Handles "add" command
    private void handleAdd(String[] commandParts) throws IOException {
        try {
            int[] array1 = parseArray(commandParts, 2);
            int[] array2 = parseArray(commandParts, 2 + array1.length + 1);
            int[] result = addArrays(array1, array2);
            headerWriter.write("ADDED\n");
            headerWriter.write(arrayToString(result) + "\n");
            headerWriter.flush();
        } catch (Exception e) {
            sendInvalidInput();
        }
    }

    // Handles "multiply" command
    private void handleMultiply(String[] commandParts) throws IOException {
        try {
            int[] array1 = parseArray(commandParts, 2);
            int[] array2 = parseArray(commandParts, 2 + array1.length + 1);
            int[] result = multiplyArrays(array1, array2);
            headerWriter.write("MULTIPLIED\n");
            headerWriter.write(arrayToString(result) + "\n");
            headerWriter.flush();
        } catch (Exception e) {
            sendInvalidInput();
        }
    }

// ================ This part is about the utilities that are used for the operations!!!!! =================

    // This method will help us parse the elements of the array based on the protocol!! 
    private int[] parseArray(String[] commandParts, int startIndex) {
        int size = Integer.parseInt(commandParts[startIndex - 1]);
        int[] array = new int[size];
        for (int i = 0; i < size; i++) {
            array[i] = Integer.parseInt(commandParts[startIndex + i]);
        }
        return array;
    }

    // Converts array to comma-delimited string
    private String arrayToString(int[] array) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < array.length; i++) {
            sb.append(array[i]);
            if (i < array.length - 1) sb.append(",");
        }
        return sb.toString();
    }
// ========= These utilities are useful for element-wise multiplication and summation =========
    // Adds two arrays element-wise
    private int[] addArrays(int[] array1, int[] array2) {
        int[] result = new int[array1.length];
        for (int i = 0; i < array1.length; i++) {
            result[i] = array1[i] + array2[i];
        }
        return result;
    }

    // Multiplies two arrays element-wise
    private int[] multiplyArrays(int[] array1, int[] array2) {
        int[] result = new int[array1.length];
        for (int i = 0; i < array1.length; i++) {
            result[i] = array1[i] * array2[i];
        }
        return result;
    }
    private void sendInvalidInput() throws IOException {
        headerWriter.write("INVALID INPUT\n");
        headerWriter.flush();
    }
}

