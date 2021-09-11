// Create Stripe card element
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe('pk_test_51JWU5BJRbaONEYoNYWYlHfzBbILSbNiRLvwdw8sxEnqzskSlcp7j8WzXceQKsTUbz8e9rfRw6Ar7wAcJjhZLyjUG00C4Jcy9wx');
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#FF0000',
        iconColor: '#FF0000'
    }
};
var card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// Check for errors
card.on('change', ({
    error
}) => {
    let displayError = document.getElementById('card-errors');
    if (error) {
        var message = `<span class="card-error-color"><i class="fas fa-exclamation-circle card-error-color pr-1"></i>${error.message}</span>`;
        $(displayError).html(message);
    } else {
        displayError.textContent = '';
    }
});


// Submit Payment
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#pay-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            let displayError = document.getElementById('card-errors');
            var message = `<span class="card-error-color"><i class="fas fa-exclamation-circle card-error-color pr-1"></i>${result.error.message}</span>`;
            $(displayError).html(message);
            card.update({
                'disabled': false
            });
            $('#pay-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});