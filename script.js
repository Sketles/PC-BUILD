
/*PRECIO DEL DOLAR ACTUALIZADO EN JQUERY API*/
$.getJSON('https://mindicador.cl/api', function(data) {
    var dailyIndicators = data;
    $("<p/>", {
        html: 'El valor actual del dolar es: $' + dailyIndicators.dolar.valor + ' Pesos Chilenos'
    }).appendTo("#ValorDolar");
}).fail(function() {
    console.log('Error al consumir la API!');
});







