package com.kookmin.chrisais9.adproject.wordwar;

public class GameWordRequest {
    private String nowWord;
    private String preWord;

    public GameWordRequest(String nowWord, String prevWord){
        this.nowWord = nowWord;
        this.preWord = prevWord;
    }

    public String getNowWord(){
        return nowWord;
    }
    public void setNowWord(String nowWord){
        this.nowWord = nowWord;
    }

    public String getPrevWord(){return preWord;}
    public void setPrevWord(String prevWord){this.preWord = prevWord;}


}
