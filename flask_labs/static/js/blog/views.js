define(
    ["underscore", "backbone", "handlebars", "blog/templates"],
    function(_, Backbone, Handlebars, templates) {
        var Views = {
            PostView: Backbone.View.extend({
                el: $("#body")[0],
                render: function(){
                    var js = JSON.parse(JSON.stringify(this.model.toJSON()));
                    var template = Handlebars.templates["post"];
                    this.$el.html(template({ post: this.model.attributes }));
                    return this;
                },
                close: function() {

                }
            }),
            PostListView: Backbone.View.extend({
                render: function() {
                    // var js = JSON.parse(JSON.stringify(this.model.toJSON()));
                    // var template = Handlebars.templates["postlist"];
                    // this.$el.html(template({ post: this.model.attributes }));
                    // return this;
                }
            }),
            SectionView: Backbone.View.extend({
                el: $("#body")[0],
                render: function(){
                    var js = JSON.parse(JSON.stringify(this.model.toJSON()));
                    var template = Handlebars.templates["section"];
                    var rendered_template = template({section: this.model.attributes});
                    // get rendered template, then populate rendered template with postlist
                    // _.each(post in this.model.posts) {
                        // var $el = $('<li>');
                        // var post_listing = newPostListView({ el : $el[0], model: post });
                    // }
                    this.$el.html(rendered_template);
                    return this;
                },
                close: function() {

                }
            })

        };
        return Views;
    }
);
