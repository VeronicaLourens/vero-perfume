let ids=["30ml", "50ml", "75ml", "100ml"];
let SizeDropDown = document.getElementById("product-size");

SizeDropDown.onchange = function () {
    for (let x = 0; x < ids.length; x++) {
        document.getElementById(ids[x]).style.display = "none";
    }
    document.getElementById(this.value).style.display = "block";
}
