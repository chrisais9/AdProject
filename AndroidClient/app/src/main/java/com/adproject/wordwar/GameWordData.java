package com.adproject.wordwar;

public class GameWordData {
    private static GameWordData instance = null;
    private String word;
    private String totalOfWord;

    private static GameWordData getInstance(){
        if(instance == null) instance = new GameWordData();
        return instance;
    }

    public GameWordData() {this("","");}

    public GameWordData(String word, String totalWord){
        this.word = word;
        this.totalOfWord = totalWord;
    }
    public String getWord(){
        return word;
    }
    public void setWord(String word){
        this.word = word;
    }

    public String getTotalWord(){return totalOfWord;}
    public void setTotalWord(String totalWord){this.totalOfWord = totalWord;}



}
