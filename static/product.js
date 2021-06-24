/** Variables iniciales */
const elemVolume = document.getElementById('volume'),
      elemPrice = document.getElementById('price'),
      elemSupplier = document.getElementById('supplier');

let volume = 0,
    price = 0,
    supplier = '';

const lenProduct = productList.length;

/** Función para calcular promedio */
function prom(value,len){
  let prom = value/len;
  return prom
}

/** Se recorre arreglo de productos para encontrar mejor proveedor e ir sumando totales de precios y volumnes */
productList.forEach((product, index) => {
  if(index == 0){
    supplier = product.name_supplier;
  } else {
    if(parseFloat(product.price) < price){
      supplier = product.name_supplier;
    }
  }
  price += parseFloat(product.price);
  volume += parseFloat(product.volume);
});

price = prom(price,lenProduct);
volume = prom(volume,lenProduct);

/** Se da formato de moneda */
price = new Intl.NumberFormat().format(price);

elemVolume.prepend(volume.toFixed(2));
elemPrice.append(price);
elemSupplier.innerHTML = supplier;