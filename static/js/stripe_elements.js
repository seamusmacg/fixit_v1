
// var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
// var client_secret = $('#id_client_secret').text().slice(1, -1);
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
var card = elements.create('card', {style: style});
card.mount('#card-element');