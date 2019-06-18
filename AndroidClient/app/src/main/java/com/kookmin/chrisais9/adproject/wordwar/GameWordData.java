package com.kookmin.chrisais9.adproject.wordwar;

public class GameWordData {
    private static GameWordData instance = null;
    private String nowWord;
    private String prevWord;

    private static GameWordData getInstance(){
        if(instance == null) instance = new GameWordData();
        return instance;
    }

    public GameWordData() {this("","");}

    public GameWordData(String nowWord, String prevWord){
        this.nowWord = nowWord;
        this.prevWord = prevWord;
    }
    public String getNowWord(){
        return nowWord;
    }
    public void setNowWord(String nowWord){
        this.nowWord = nowWord;
    }

    public String getPrevWord(){return prevWord;}
    public void setPrevWord(String prevWord){this.prevWord = prevWord;}



}
