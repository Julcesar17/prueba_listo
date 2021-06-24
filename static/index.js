/** Variables iniciales */
const elemInput = document.getElementById('inputProduct'),
      elemBotton = document.getElementById('btnBuscar');

const products = document.querySelectorAll('tbody tr');

/** Fucnción para buscar productos */
function search(product){

  products.forEach(item => {
    let data = item.dataset.product;
  });

  return true;
}

/** Se detecta el nombre del producto ingresado */
elemInput.addEventListener('change', (e) => {
  let value = e.target.value;
  if(value.length > 0){
    let target = search(value);
  }
});

elemInput.addEventListener('click', (e) => {
  let value = elemInput.value;
  if(value.length > 0){
    let target = search(value);
  }
});