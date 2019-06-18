package com.adproject.wordwar;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface RetrofitService {
    //public static final String baseURL = Resources.getSystem().getString(R.string.baseUrl);
    public static final String baseURL = "http://172.30.1.4:8000/";

    @GET("validword/")
    Call<GameWordResponse> setWord(
            @Query ("word") String word
    );
}
