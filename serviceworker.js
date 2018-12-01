var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilos.css',
    '/static/core/img/Apolo.jpg',
    '/static/core/img/Bigotes.jpg',
    '/static/core/img/Chocolate.jpg',
    '/static/core/img/crowfunding.jpg',
    '/static/core/img/Duque.jpg',
    '/static/core/img/logo.png',
    '/static/core/img/Luna.jpg',
    '/static/core/img/Maya.jpg',
    '/static/core/img/Oso.jpg',
    '/static/core/img/perro.png',
    '/static/core/img/Pexel.jpg',
    '/static/core/img/rescate.jpg',
    '/static/core/img/social-inst.png',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/socialplus.png',
    '/static/core/img/Tom.jpg',
    '/static/core/img/Wifi.jpg',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/js/inicializacion.js',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});