package com.adproject.wordwar;

public class GameWordData {
    private static GameWordData instance = null;
    private String word;

    private static GameWordData getInstance(){
        if(instance == null) instance = new GameWordData();
        return instance;
    }

    public GameWordData() {this("");}

    public GameWordData(String word){
        this.word = word;
    }

    public void setData(GameWordResponse gameWordResponse){
        this.word = gameWordResponse.getWord();
    }
    public String getWord(){
        return word;
    }
    public void setWord(String word){
        this.word = word;
    }



}
