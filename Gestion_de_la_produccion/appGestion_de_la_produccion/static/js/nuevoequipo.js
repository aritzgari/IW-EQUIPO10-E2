document.getElementById("botonnuevo").addEventListener("click", function (event) {
  event.preventDefault();


  let form = document.getElementById("formnuevoequipo");

  let infoform = new FormData(form);

  fetch("./añadirequipoAPI", {
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

    .then(function (text) {
      console.log(text);
      form.append(anadir_datos(infoform,text));
      alert("Equipo añadido");
    })
    .catch(function (err) {
      console.log(err);
      alert("error inesperado");
    });
});


function anadir_datos(infoform,id) {
  var tabla = document.getElementById("cosasequipo");

  var fila = tabla.insertRow(); //si le pones un -1 lo pone al final
  var cell0 = fila.insertCell(0);
  var cell1 = fila.insertCell(1);
  var cell2 = fila.insertCell(2);
  var cell3 = fila.insertCell(3);
  var cell4 = fila.insertCell(4);
  var cell5 = fila.insertCell(5);

  cell0.innerHTML = infoform.get("marca");
  cell1.innerHTML = infoform.get("modelo");
  cell2.innerHTML = infoform.get("categoria");
  cell3.innerHTML = infoform.get("fecha_adquisicion_year")+"/"+ infoform.get("fecha_adquisicion_month")
  +"/"+ infoform.get("fecha_adquisicion_day");
  cell4.innerHTML = infoform.get("fecha_instalacion_year")+"/"+ infoform.get("fecha_instalacion_month")
                      +"/"+ infoform.get("fecha_instalacion_day");
  cell5.innerHTML = `<a href="/appGestion_de_la_produccion/responsable/equipo/${id}" title="Detalles">Ver detalles</a>`;
}


