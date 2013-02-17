requirejs.config({
    baseUrl: '/static/js',
    paths: {
        'jquery': 'vendor/jquery',
        'underscore': 'vendor/underscore',
        'backbone': 'vendor/backbone',
        'handlebars': 'vendor/handlebars.runtime'
    },
    shim: {
        'handlebars': {
            exports: 'Handlebars'
        },
        'blog/templates': {
            deps: ['handlebars']
        }
    }
});

require([
    'jquery',
    'blog/router'
    ],
    function($, Router) {
        $(document).ready(function(){

            var router = new Router();
            Backbone.history.start({pushState: true});

            $(document).on("click", "a[href]:not([data-bypass])", function(e) {
                // Get the absolute anchor href.
                var href = {
                    prop: $(this).prop("href"),
                    attr: $(this).attr("href")
                };
                // Get the absolute root.
                var root = location.protocol + "//" + location.host + "/";

                // Ensure the root is part of the anchor href, meaning it's relative.
                // if (href.prop.slice(0, root.length) === "/") {
                    // Stop the default event to ensure the link will not cause a page
                    // refresh.
                    e.preventDefault();

                    // `Backbone.history.navigate` is sufficient for all Routers and will
                    // trigger the correct events. The Router's internal `navigate` method
                    // calls this anyways.  The fragment is sliced from the root.
                    Backbone.history.navigate(href.attr, true);
                // }
            });
        });
    }
);
