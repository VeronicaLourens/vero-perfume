let ids=["30ml", "50ml", "75ml", "100ml"];
let sizeDropDown = document.getElementById("product_size");
let prices = document.getElementsByClassName('prices')
let sizes = document.getElementsByClassName('size-picked')
let price = document.getElementById('product_price')

for (let size of sizes) {
    if (size) {
        size.classList.add('hidden')
    }
}
/*correctSizes = []
*for ( i in sizeDropDown.children) {
*    if (i % 2 != 0) {
*        correctSizes.push(sizeDropDown.children[i])
*    }
*}
*/

/*let userSizeInputs = correctSizes.slice(0, -3)
*userSizeInputs.forEach(input => {
*    input.addEventListener('change' , function() {
*        let idx = userSizeInputs(idx)
*        prices[idx].classList.remove('hidden')
*        console.log(prices[idx])
*    })
*});
*/

sizeDropDown.addEventListener('change', function() {
    if (this.value == '30ml') {
        price.innerText = '€ 75.00'
        // hiddenField.value = 75
    }
    else if (this.value == '50ml') {
        price.innerText = '€ 95.00'
    }
    else if (this.value == '75ml') {
        price.innerText = '€ 120.00'
    }
    else if(this.value == '100ml') {
        price.innerText = '€ 190.00'
    }
})