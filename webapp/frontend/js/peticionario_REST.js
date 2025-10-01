/* 
Autor: Denys Litvynov Lymanets
Fecha: 29-09-2025
Descripción: Módulo encargado de realizar peticiones REST al backend. Contiene funciones de GET, POST, PUT y DELETE.
*/

// ----------------------------------------------------------

class PeticionarioREST {
    async hacerPeticionRest(method, url, body = null) {
        const options = {
            method: method,
            headers: {
                'Content-Type' : 'application/json'
            }
        };
        if (body) {
            options.body = JSON.stringify(body);
        }
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error('Error: ${response.status}');
        }
        return await response.json();
    }
}

// ----------------------------------------------------------

