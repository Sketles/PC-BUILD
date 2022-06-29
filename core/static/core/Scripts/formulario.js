
$(document).ready(function(){

    $("#enviar").click(function(){
        var nombre = $("#nombre").val();
        
        if(nombre==""){
            alert("Error, Porfavor rellene el campo nombre");
        }
    });

    $("#enviar").click(function(){
        var email = $("#email").val();
        
        if(email==""){
            alert("Error, Porfavor rellene el campo email");
        }
    });


    $("#enviar").click(function(){
        var mensaje = $("#mensaje").val();

        if(mensaje.length <= 10){
            alert("Porfavor escriba un poco mas (10 caracteres)");
        }

    });

});
