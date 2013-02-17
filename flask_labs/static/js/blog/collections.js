define(
    ["backbone", "blog/models"],
    function(Backbone, Models) {
        var Collections = {
            Sections: Backbone.Collection.extend({
                url: "/sections",
                model: Models.Section,
                parse: function(response) {
                    return response.sections;
                }
            }),
            Posts: Backbone.Collection.extend({
                url: "/posts",
                model: Models.Post,
                parse: function(response) {
                    return response.posts;
                }
            })
        };
        return Collections;
    }
);
