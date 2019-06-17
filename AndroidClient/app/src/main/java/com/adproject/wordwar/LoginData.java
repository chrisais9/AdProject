package com.adproject.wordwar;

public class LoginData {
    private static LoginData instance = null;

    private String username;
    private String name;
    private String token;

    public static LoginData getInstance()
    {
        if(instance == null) instance = new LoginData();
        return instance;
    }

    public LoginData() {
        this("", "","");
    }

    public LoginData(String username, String name, String token) {
        this.username = username;
        this.name = name;
        this.token = token;
    }

    public void setData(LoginResponse loginResponse){
        this.username = loginResponse.getUsername();
        this.name = loginResponse.getName();
        this.token = loginResponse.getToken();
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
}
