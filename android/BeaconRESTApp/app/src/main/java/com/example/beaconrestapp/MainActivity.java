package com.example.beaconrestapp;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Build;
import android.util.Log;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private static final int CODIGO_PETICION_PERMISOS = 11223344;
    private EscanerIBeacons escaner;
    private LogicaFake logicaFake = new LogicaFake();
    private TextView tvMedidas;
    private String urlServidor = "https://httpbin.org/post"; // Para pruebas; cambia a tu servidor

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvMedidas = findViewById(R.id.tv_medidas);

        // Permisos (manejo aquí para simplicidad)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            if (ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_SCAN) != PackageManager.PERMISSION_GRANTED ||
                    ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
                ActivityCompat.requestPermissions(this,
                        new String[]{Manifest.permission.BLUETOOTH_SCAN, Manifest.permission.BLUETOOTH_CONNECT},
                        CODIGO_PETICION_PERMISOS);
            } else {
                iniciarEscaneo();
            }
        } else {
            if (ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH) != PackageManager.PERMISSION_GRANTED ||
                    ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_ADMIN) != PackageManager.PERMISSION_GRANTED ||
                    ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                ActivityCompat.requestPermissions(this,
                        new String[]{Manifest.permission.BLUETOOTH, Manifest.permission.BLUETOOTH_ADMIN, Manifest.permission.ACCESS_FINE_LOCATION},
                        CODIGO_PETICION_PERMISOS);
            } else {
                iniciarEscaneo();
            }
        }
    }

    private void iniciarEscaneo() {
        escaner = new EscanerIBeacons(this, jsonMedida -> {
            runOnUiThread(() -> {
                tvMedidas.append("Medida recibida: " + jsonMedida + "\n");
                Toast.makeText(this, "Enviando a servidor...", Toast.LENGTH_SHORT).show();
            });
            logicaFake.guardarMedida(jsonMedida, urlServidor);
        });
        escaner.iniciarEscaneoAutomatico("ProbaEnCasa"); // Cambia al nombre de tu dispositivo
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        escaner.onRequestPermissionsResult(requestCode, permissions, grantResults); // Delega si hace falta
        if (requestCode == CODIGO_PETICION_PERMISOS && grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            iniciarEscaneo();
        } else {
            Toast.makeText(this, "Permisos denegados", Toast.LENGTH_LONG).show();
        }
    }
}