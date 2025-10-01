/* 
Autor: Denys Litvynov Lymanets
Fecha: 29-09-2025
Descripción: Script principal de interacción en el frontend. Maneja eventos y funcionalidades de la interfaz.
*/

// ----------------------------------------------------------

document.addEventListener('DOMContentLoaded', ()=> {
    const boton = document.getElementById('obtenerMedidaBtn');
    const display = document.getElementById('medidaDisplay');

    boton.addEventListener('click', async () => {
        const logicaFake = new LogicaFake();
        try {
            const resultado = await logicaFake.obtenerUltimaMedida();
            display.textContent =`Medida: ${resultado.medida}`;
        } catch (error) {
            display.textContent = 'Error al obtener la medida';
            console.error(error);
        }
    });
});

// ----------------------------------------------------------

