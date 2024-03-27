package com.hotelreservationapp.models;

import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.text.ParseException;

import org.json.JSONObject;
import org.json.JSONTokener;
// import org.json.simple.parser.JSONParser;
// import org.json.simple.parser.ParseException;

public class DatabaseConnection {
    // Method to read database settings from settings.json file
    private static JSONObject readSettings() {
        try {
            JSONTokener tokener = new JSONTokener(new FileReader("settings.json"));
            JSONObject root = new JSONObject(tokener);
            return root;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    // Method to establish a connection to the database
    public static Connection getConnection() {
        JSONObject settings = readSettings();
        if (settings == null) {
            return null;
        }

        String jdbcUrl = (String) settings.get("jdbc_url");
        String username = (String) settings.get("user");
        String password = (String) settings.get("password");

        Connection connection = null;
        try {
            // Register the JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            // Create a connection to the database
            connection = DriverManager.getConnection(jdbcUrl, username, password);
            System.out.println("Connected to the database.");
        } catch (ClassNotFoundException | SQLException e) {
            System.err.println("Error connecting to the database: " + e.getMessage());
        }
        return connection;
    }

    // Method to close the database connection
    public static void closeConnection(Connection connection) {
        if (connection != null) {
            try {
                connection.close();
                System.out.println("Database connection closed.");
            } catch (SQLException e) {
                System.err.println("Error closing database connection: " + e.getMessage());
            }
        }
    }

    // public static void main(String[] args) {
    //     // Test the connection
    //     Connection connection = getConnection();
    //     closeConnection(connection);
    // }
}
