require 'stripe'
require 'sinatra'

Stripe.api_key = 'sua_chave_secreta_aqui'

set :static, true
set :port, 4242

YOUR_DOMAIN = 'http://localhost:4242'

post '/create-checkout-session' do
  content_type 'application/json'

  session = Stripe::Checkout::Session.create(
    payment_method_types: ['card'],
    line_items: [{
      price: 'price_1234',  # coloque seu price_id real aqui
      quantity: 1,
    }],
    mode: 'payment',
    success_url: "#{YOUR_DOMAIN}/success.html",
    cancel_url: "#{YOUR_DOMAIN}/cancel.html"
  )

  { id: session.id }.to_json
end
