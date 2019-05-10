package com.example.lakshmi.calcu;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

        Button btn_1,btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_0,btn_Add,btn_Sub,btn_Mul,btn_Div,btn_calc,btn_dec,btn_clear;
        EditText ed1;

        float Value1, Value2;
        boolean mAddition, mSubtract, mMultiplication, mDivision ;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);

            btn_0 = (Button) findViewById(R.id.bt0);
            btn_1 = (Button) findViewById(R.id.bt1);
            btn_2 = (Button) findViewById(R.id.bt2);
            btn_3 = (Button) findViewById(R.id.bt3);
            btn_4 = (Button) findViewById(R.id.bt4);
            btn_5 = (Button) findViewById(R.id.bt5);
            btn_6 = (Button) findViewById(R.id.bt6);
            btn_7 = (Button) findViewById(R.id.bt7);
            btn_8 = (Button) findViewById(R.id.bt8);
            btn_9 = (Button) findViewById(R.id.bt9);
            btn_Add = (Button) findViewById(R.id.btadd);
            btn_Div = (Button) findViewById(R.id.btdiv);
            btn_Sub = (Button) findViewById(R.id.btsub);
            btn_Mul = (Button) findViewById(R.id.btmul);
            btn_clear = (Button) findViewById(R.id.btc);
            ed1 = (EditText) findViewById(R.id.et);

            btn_0.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"0");
                }
            });

            btn_1.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"1");
                }
            });

            btn_2.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"2");
                }
            });

            btn_3.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"3");
                }
            });

            btn_4.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"4");
                }
            });

            btn_5.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"5");
                }
            });

            btn_6.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"6");
                }
            });

            btn_7.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"7");
                }
            });

            btn_8.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"8");
                }
            });

            btn_9.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+"9");
                }
            });

            btn_dec.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText(ed1.getText()+".");
                }
            });

            btn_Add.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {

                    if (ed1 == null){
                        ed1.setText("");
                    }else {
                        Value1 = Float.parseFloat(ed1.getText() + "");
                        mAddition = true;
                        ed1.setText(null);
                    }
                }
            });

            btn_Sub.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Value1 = Float.parseFloat(ed1.getText() + "");
                    mSubtract = true ;
                    ed1.setText(null);
                }
            });

            btn_Mul.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Value1 = Float.parseFloat(ed1.getText() + "");
                    mMultiplication = true ;
                    ed1.setText(null);
                }
            });

            btn_Div.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Value1 = Float.parseFloat(ed1.getText()+"");
                    mDivision = true ;
                    ed1.setText(null);
                }
            });

            btn_calc.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Value2 = Float.parseFloat(ed1.getText() + "");

                    if (mAddition == true){

                        ed1.setText(Value1 + Value2 +"");
                        mAddition=false;
                    }


                    if (mSubtract == true){
                        ed1.setText(Value1 - Value2 +"");
                        mSubtract=false;
                    }

                    if (mMultiplication == true){
                        ed1.setText(Value1 * Value2 + "");
                        mMultiplication=false;
                    }

                    if (mDivision == true){
                        ed1.setText(Value1 / Value2+"");
                        mDivision=false;
                    }
                }
            });

            btn_clear.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    ed1.setText("");
                }
            });
        }

    }
jav
