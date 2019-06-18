package com.adproject.wordwar;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class GameFragment extends Fragment {
    private View view;


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        view = inflater.inflate(R.layout.fragment_game, container, false);
        final Button confirmButton = view.findViewById(R.id.confirm);
        final EditText wordEditText = view.findViewById(R.id.wordinput);
        final TextView responseTextView = view.findViewById(R.id.response);

        wordEditText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                Log.d("text", s.toString());
                if(count>0){
                    confirmButton.setEnabled(true);
                }
                else{
                    confirmButton.setEnabled(false);
                }

            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });


        confirmButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            Retrofit retrofit = new Retrofit.Builder()
                    .baseUrl(RetrofitService.baseURL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build();
            RetrofitService retrofitService = retrofit.create(RetrofitService.class);
            GameWordRequest gameWordRequest = new GameWordRequest(wordEditText.getText().toString());
            Call<GameWordResponse> call = retrofitService.setWord(gameWordRequest.getWord());
            call.enqueue(new Callback<GameWordResponse>() {

                @Override
                public void onResponse(Call<GameWordResponse> call, Response<GameWordResponse> response) {
                    if(response.isSuccessful()) {
                        Toast.makeText(getActivity().getApplicationContext(), "서버 응답 성공", Toast.LENGTH_LONG).show();
                        responseTextView.setText("입력된 단어: " + response.body().getWord() + " 사전에서 찾은 횟수: " + response.body().getTotalOfWord() );

                    }
                    else{
                        Toast.makeText(getActivity().getApplicationContext(), response.raw().message(), Toast.LENGTH_LONG).show();

                    }

                }

                @Override
                public void onFailure(Call<GameWordResponse> call, Throwable t) {
                    t.printStackTrace();
                    Toast.makeText(getActivity().getApplicationContext(), "서버 연결실패", Toast.LENGTH_LONG).show();

                }
            });
            }
        });


        return view;
    }
}
