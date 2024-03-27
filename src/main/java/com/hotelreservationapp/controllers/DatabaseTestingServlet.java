package com.hotelreservationapp.controllers;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.hotelreservationapp.models.DatabaseConnection;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "databasetestingservlet", value = "/db-test-servlet")
public class DatabaseTestingServlet {

    public void init() {
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html");
        DatabaseConnection connection = new DatabaseConnection();
        java.sql.Connection conn = connection.getConnection();
        // Hello
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h1>DATABAE TEST</h1>");
        out.println("</body></html>");
    }

    public void destroy() {
    }
}
