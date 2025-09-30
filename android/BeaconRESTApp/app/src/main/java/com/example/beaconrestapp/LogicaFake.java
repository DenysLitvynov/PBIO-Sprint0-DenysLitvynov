package com.example.beaconrestapp;

import android.util.Log;

public class LogicaFake {

    public void guardarMedida(String jsonMedida, String baseUrl, String endpoint) {
        String urlCompleta = baseUrl + endpoint;  // <- Construye la URL full aquí (ej. "http://192.168.1.100:8000" + "/api/v1/guardar-medida")
        Log.d("LogicaFake", "URL construida: " + urlCompleta);  // Para depurar

        PeticionarioREST elPeticionario = new PeticionarioREST();

        elPeticionario.hacerPeticionREST("POST", urlCompleta, jsonMedida,
                new PeticionarioREST.RespuestaREST() {
                    @Override
                    public void callback(int codigo, String cuerpo) {
                        Log.d("LogicaFake", "Respuesta del servidor: codigo=" + codigo + ", cuerpo=" + cuerpo);
                    }
                });
    }
}