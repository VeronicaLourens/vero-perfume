const welcomeDiv = document.getElementById('welcome-div');
const personalDetailsDiv = document.getElementById('personal-details-div');
const btnPersonalDetails = document.getElementById('btn-personal-details');
const orderDiv = document.getElementById('orders-div');
const btnMyOrders = document.getElementById('btn-my-orders');

document.addEventListener('DOMContentLoaded', function(){

    btnPersonalDetails.addEventListener('click', (e) => {
        personalDetailsDiv.classList.add('d-flex');
        welcomeDiv.style.display = 'none';
    });

    btnMyOrders.addEventListener('click', (e) => {
        orderDiv.classList.add('d-flex');
        welcomeDiv.style.display = 'none';
        personalDetailsDiv.style.display = 'none';
    })

})