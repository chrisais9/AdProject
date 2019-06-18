package com.kookmin.chrisais9.adproject.wordwar;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class GameWordResponse {
    @SerializedName("echo")
    @Expose
    private String word;
    @SerializedName("total")
    @Expose
    private String totalOfWord;

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }
    public String getTotalOfWord(){
        return totalOfWord;
    }
    public void setTotalOfWord(String totalWord){
        this.totalOfWord = totalWord;
    }
}
