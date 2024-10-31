package cs.arraycalc.server;

import java.net.Socket;
import java.net.ServerSocket;

public class ArrayCalcServer{
    public static void main(String[] args) throws Exception{
        try(ServerSocket ss = new ServerSocket(9999)){
            while (true) {
                System.out.println("Waiting for Client to connect...");
                try(Socket clientConnection = ss.accept()){
                    new ClientHandler(clientConnection);
                }
            }
        }
    }
}