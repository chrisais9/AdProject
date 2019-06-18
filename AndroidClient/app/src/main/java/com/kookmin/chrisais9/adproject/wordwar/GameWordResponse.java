package com.kookmin.chrisais9.adproject.wordwar;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class GameWordResponse {

    @SerializedName("flag")
    @Expose
    private String flag;

    public String getFlag(){
        return flag;
    }
    public void setFlag(String flag){
        this.flag = flag;
    }
}
