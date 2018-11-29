package cz.zcu.kiv.ds;

import java.net.InetAddress;
import java.net.UnknownHostException;

import static spark.Spark.*;

public class HelloWorldRestAPI {

    public static void main(String[] args) {

        port(8080);

        get("/hello", (req, res) -> {
            res.type("application/json");
            return getMessage();
        });

    }

    public static String getMessage() {
        String hostname;
        try {
            hostname = InetAddress.getLocalHost().getHostName();
        } catch (UnknownHostException e) {
            hostname = "unknown";
        }
        return "{ \"message\": \"Hello World from " + hostname + "\" }";
    }

}

// InetAddress.getLocalHost().getHostName()