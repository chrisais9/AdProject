package com.kookmin.chrisais9.adproject.wordwar;

public class GameWordRequest {
    private String nowWord;
    private String preWord;

    public GameWordRequest(String nowWord, String preWord){
        this.nowWord = nowWord;
        this.preWord = preWord;
    }

    public String getNowWord(){
        return nowWord;
    }
    public void setNowWord(String nowWord){
        this.nowWord = nowWord;
    }

    public String getPreWord(){return preWord;}
    public void setPreWord(String prevWord){this.preWord = prevWord;}


}
