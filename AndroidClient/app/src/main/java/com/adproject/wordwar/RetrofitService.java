package com.adproject.wordwar;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface RetrofitService {
    //public static final String baseURL = Resources.getSystem().getString(R.string.baseUrl);
//    public static final String baseURL = "http://192.168.0.12:8000/";
    public static final String baseURL = "https://172.30.1.6:8000/";

    @POST("logintest")
    Call<LoginResponse> login(
            @Body LoginRequest loginRequest
    );
}
