package com.adproject.wordwar;

public class LoginResponse {
    private String username;
    private String name;
    private String token;
    private boolean isFirst;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) { this.username = username; }

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

    public boolean isFirst() {
        return isFirst;
    }

    public void setFirst(boolean first) {
        isFirst = first;
    }
}
