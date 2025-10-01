/* 
Autor: Denys Litvynov Lymanets
Fecha: 29-09-2025
Descripción: Script con lógica simulada (fake) para pruebas de la aplicación sin conexión al backend real.
*/

import { PeticionarioREST } from './peticionario_REST.js';

// ----------------------------------------------------------

export class LogicaFake {
    constructor() {
        this.peticionario = new PeticionarioREST();
    }

    async obtenerUltimaMedida() {
        const url = '/api/v1/ultima-medida';
        return await this.peticionario.hacerPeticionRest('GET', url);
    }
}

// ----------------------------------------------------------

