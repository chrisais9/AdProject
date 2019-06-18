package com.kookmin.chrisais9.adproject.wordwar;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class GameWordResponse {
    @SerializedName("echo")
    @Expose
    private String word;
    @SerializedName("flag")
    @Expose
    private String flag;

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }
    public String getFlag(){
        return flag;
    }
    public void setFlag(String flag){
        this.flag = flag;
    }
}
