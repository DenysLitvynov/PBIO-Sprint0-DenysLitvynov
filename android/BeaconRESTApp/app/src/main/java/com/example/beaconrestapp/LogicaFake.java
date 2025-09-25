package com.example.beaconrestapp;

import android.util.Log;

public class LogicaFake {

    public void guardarMedida(String jsonMedida, String urlServidor) {
        PeticionarioREST elPeticionario = new PeticionarioREST();

        elPeticionario.hacerPeticionREST("POST", urlServidor, jsonMedida,
                new PeticionarioREST.RespuestaREST() {
                    @Override
                    public void callback(int codigo, String cuerpo) {
                        Log.d("LogicaFake", "Respuesta del servidor: codigo=" + codigo + ", cuerpo=" + cuerpo);
                    }
                });
    }
}