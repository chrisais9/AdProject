package com.kookmin.chrisais9.adproject.wordwar;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Query;

public interface RetrofitService {
    //public static final String baseURL = Resources.getSystem().getString(R.string.baseUrl);
<<<<<<< HEAD:AndroidClient/app/src/main/java/com/kookmin/chrisais9/adproject/wordwar/RetrofitService.java
    public static final String baseURL = "http://172.30.1.4:8000/";

    @GET("validword/")
    Call<GameWordResponse> setWord(
            @Query("word") String word
=======
    public static final String baseURL = "http://192.168.10.4:8000/";

    @POST("logintest/")
    Call<LoginResponse> login(
            @Body LoginRequest loginRequest
>>>>>>> parent of ca9f5f4... word validation check / game view and logic:AndroidClient/app/src/main/java/com/adproject/wordwar/RetrofitService.java
    );
}
