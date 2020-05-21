//Esta línea con el listener nos permite actuar cuando se seleciona el botón.
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
  var col0 = fila.insertCell(0);
  var col1 = fila.insertCell(1);
  var col2 = fila.insertCell(2);
  var col3 = fila.insertCell(3);
  var col4 = fila.insertCell(4);
  var col5 = fila.insertCell(5);

  col0.innerHTML = infoform.get("marca");
  col1.innerHTML = infoform.get("modelo");
  col2.innerHTML = infoform.get("categoria");
  col3.innerHTML = infoform.get("fecha_adquisicion_year")+"/"+ infoform.get("fecha_adquisicion_month")
  +"/"+ infoform.get("fecha_adquisicion_day");
  col4.innerHTML = infoform.get("fecha_instalacion_year")+"/"+ infoform.get("fecha_instalacion_month")
                      +"/"+ infoform.get("fecha_instalacion_day");
  col5.innerHTML = `<a href="/appGestion_de_la_produccion/responsable/equipo/${id}" title="Detalles">Ver detalles</a>`;
}


