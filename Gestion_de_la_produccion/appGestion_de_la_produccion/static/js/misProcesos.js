//Se adquieren los valores del objeto seleccionado en el checkbox
var finalizarproceso = document.getElementsByClassName("chekboxoperario");

//Se itera por lo valores y se selecciona el id para saber cual borrar, y mediante la url se aplica el código que está en views.
for(let i=0;i<finalizarproceso.length;i++){
    finalizarproceso[i].addEventListener("click",function(e){
        let form = e.target.parentNode;
        let infoform = new FormData(form);
        console.log(infoform.get("idProceso"))
        fetch("./deleteAPI", {
            method: "POST",
            body: infoform,
        })
        //Si da un error de ajax salta.
        .then(function (response) {
        if (response.ok) {
          return response.text();
        } else {
          throw "Error en la llamada Ajax";
        }
      })
     //La funcion que manda borrar la fila entera
      .then(function (texto) {
        form.parentNode.parentNode.remove();
      })
       //Si da cualquier otro error salta.
      .catch(function (err) {
        alert("Error inesperado");
      });
    })
}
