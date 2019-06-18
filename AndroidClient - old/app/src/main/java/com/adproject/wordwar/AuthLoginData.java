package com.adproject.wordwar;

public class AuthLoginData {
    private static AuthLoginData instance = null;

    private String username;
    private String name;
    private String token;

    public static AuthLoginData getInstance()
    {
        if(instance == null) instance = new AuthLoginData();
        return instance;
    }

    public AuthLoginData() {
        this("", "","");
    }

    public AuthLoginData(String username, String name, String token) {
        this.username = username;
        this.name = name;
        this.token = token;
    }

    public void setData(AuthLoginResponse authLoginResponse){
        this.username = authLoginResponse.getUsername();
        this.name = authLoginResponse.getName();
        this.token = authLoginResponse.getToken();
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
