package com.adproject.wordwar;

public class GameWordRequest {
    private String word;

    public GameWordRequest(String word){
        this.word = word;
    }

    public String getWord(){
        return word;
    }

    public void setWord(String word){
        this.word = word;
    }

}
