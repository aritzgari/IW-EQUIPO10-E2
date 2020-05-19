
var finalizarproceso =document.getElementsByClassName("pinchecheckbox");

for(let i=0;i<finalizarproceso.length;i++){
    finalizarproceso[i].addEventListener("click",function(e){
        let form = e.target.parentNode;
        let infoform = new FormData(form);
        console.log(infoform.get("idProceso"))
        fetch("./deleteAPI", {
            method: "POST",
            body: infoform,
        })
        .then(function (response) {
        if (response.ok) {
          return response.text();
        } else {
          throw "Error en la llamada Ajax";
        }
      })
      .then(function (texto) {
        form.parentNode.parentNode.remove();
      })
      .catch(function (err) {
        alert("Error inesperado");
      });
    })
}
