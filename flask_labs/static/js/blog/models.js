define(
    ["backbone"],
    function(Backbone) {
        var Models = {
            Post: Backbone.Model.extend({
                idAttribute: "slug"
            }),
            Section: Backbone.Model.extend({
                idAttribute: "slug"
            })
        };
        return Models;
    }
);
