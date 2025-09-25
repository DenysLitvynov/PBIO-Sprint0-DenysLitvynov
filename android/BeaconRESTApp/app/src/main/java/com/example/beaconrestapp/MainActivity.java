package com.example.beaconrestapp;

import android.content.pm.PackageManager;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import android.util.Log;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private static final int CODIGO_PETICION_PERMISOS = 11223344;
    private EscanerIBeacons escaner;
    private LogicaFake logicaFake = new LogicaFake();
    private TextView tvMedidas;
    private String urlServidor = "https://webhook.site/d839c356-4b86-4e52-b23a-6dc7b339a7c9";
    private static final String ETIQUETA_LOG = ">>>>";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvMedidas = findViewById(R.id.tv_medidas);

        escaner = new EscanerIBeacons(this, jsonMedida -> {
            runOnUiThread(() -> {
                tvMedidas.setText("Última medida recibida: " + jsonMedida);
                Toast.makeText(this, "Enviando a servidor...", Toast.LENGTH_SHORT).show();
            });
            logicaFake.guardarMedida(jsonMedida, urlServidor);
        });

        Log.d(ETIQUETA_LOG, " onCreate(): empieza ");

        escaner.inicializarBlueTooth();

        Log.d(ETIQUETA_LOG, " onCreate(): termina ");

        escaner.iniciarEscaneoAutomatico("ProbaEnCasa");
    }

    public void onRequestPermissionsResult(int requestCode, String[] permissions,
                                           int[] grantResults) {
        super.onRequestPermissionsResult( requestCode, permissions, grantResults);

        switch (requestCode) {
            case CODIGO_PETICION_PERMISOS:
                if (grantResults.length > 0 &&
                        grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                    Log.d(ETIQUETA_LOG, " onRequestPermissionResult(): permisos concedidos  !!!!");
                    escaner.iniciarEscaneoAutomatico("ProbaEnCasa");
                }  else {

                    Log.d(ETIQUETA_LOG, " onRequestPermissionResult(): Socorro: permisos NO concedidos  !!!!");

                }
                return;
        }
    } // ()
}