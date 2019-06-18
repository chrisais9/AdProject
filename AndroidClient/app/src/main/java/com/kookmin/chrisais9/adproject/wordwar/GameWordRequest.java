package com.kookmin.chrisais9.adproject.wordwar;

public class GameWordRequest {
    private String nowWord;
    private String prevWord;

    public GameWordRequest(String nowWord, String prevWord){
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
