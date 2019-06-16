package com.adproject.wordwar;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Patterns;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.Toast;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class AuthLoginActivity extends AppCompatActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        final EditText emailEditText = findViewById(R.id.email);
        final EditText passwordEditText = findViewById(R.id.password);
        final Button loginButton = findViewById(R.id.login);
        final ProgressBar loadingProgressBar = findViewById(R.id.loading);

        emailEditText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if(!isEmailValid(emailEditText.getText().toString())){
                    emailEditText.setError("사용할 수 없는 이메일입니다.");
                    loginButton.setEnabled(false);
                }
                else if(isPasswordValid(passwordEditText.getText().toString())){
                    loginButton.setEnabled(true);
                }
                else{
                    loginButton.setEnabled(false);
                }
            }
        });

        passwordEditText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                if(!isPasswordValid(passwordEditText.getText().toString())){
                    passwordEditText.setError("사용할 수 없는 비밀번호입니다.");
                    loginButton.setEnabled(false);
                }
                else if(isEmailValid(emailEditText.getText().toString())){
                    loginButton.setEnabled(true);
                }
                else{
                    loginButton.setEnabled(false);
                }
            }
        });



        loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                getWindow().setFlags(WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE, WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE);
                loadingProgressBar.setVisibility(View.VISIBLE);

                Retrofit retrofit = new Retrofit.Builder()
                        .baseUrl(RetrofitService.baseURL)
                        .addConverterFactory(GsonConverterFactory.create())
                        .build();
                RetrofitService retrofitService = retrofit.create(RetrofitService.class);

                AuthLoginRequest authLoginRequest = new AuthLoginRequest(emailEditText.getText().toString(), passwordEditText.getText().toString());
                Call<AuthLoginResponse> call = retrofitService.login(authLoginRequest);
                call.enqueue(new Callback<AuthLoginResponse>() {
                    @Override
                    public void onResponse(Call<AuthLoginResponse> call, Response<AuthLoginResponse> response) {
                        if (response.isSuccessful()) {
                            Toast.makeText(getApplicationContext(), "로그인 성공", Toast.LENGTH_LONG).show();
                            AuthLoginData.getInstance().setData(response.body());
                            getWindow().clearFlags(WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE);
                            goMain();
                        }
                        else {

                            Toast.makeText(getApplicationContext(), response.raw().message(), Toast.LENGTH_LONG).show();
                            getWindow().clearFlags(WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE);
                            loadingProgressBar.setVisibility(View.GONE);
                        }
                    }

                    @Override
                    public void onFailure(Call<AuthLoginResponse> call, Throwable t) {
                        t.printStackTrace();
                        Toast.makeText(getApplicationContext(), "서버 연결 실패", Toast.LENGTH_LONG).show();
                        getWindow().clearFlags(WindowManager.LayoutParams.FLAG_NOT_TOUCHABLE);
                        loadingProgressBar.setVisibility(View.GONE);
                    }
                });
            }
        });
    }

    private void goMain(){
        Intent intent = new Intent(getApplicationContext(), MainActivity.class);
        startActivity(intent);
    }

    private boolean isEmailValid(String username) {
        if (username == null) {
            return false;
        }
        if (username.contains("@")) {
            return Patterns.EMAIL_ADDRESS.matcher(username).matches();
        } else {
            return !username.trim().isEmpty();
        }
    }

    private boolean isPasswordValid(String password) {
        return password != null && password.trim().length() >= 0;
    }
}
