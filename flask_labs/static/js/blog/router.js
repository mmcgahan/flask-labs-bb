define(
    ["backbone", "blog/collections", "blog/models", "blog/views"],
    function(Backbone, Collections, Models, Views) {
        var Router = Backbone.Router.extend({
            routes:{
                "sections/": "renderSections",
                "sections/:section": "renderSection",
                "posts/:post": "renderPost"
            },
            clearViews: function() {
                if (this.sectionView) this.sectionView.close();
                if (this.postView) this.postView.close();
            },
            getSectionsCollection: function(callback) {
                this.sectionsCollection = new Collections.Sections();
                var that = this;
                this.sectionsCollection.fetch({
                    success: function() {
                        if (that.requestedSection) {
                            that.renderSection(that.requestedSection);
                        }
                    }
                });
            },
            getPostsCollection: function() {
                this.postsCollection = new Collections.Posts();
                var that = this;
                this.postsCollection.fetch({
                    success: function() {
                        if (that.requestedPost) {
                            that.renderPost(that.requestedPost);
                        }
                    }
                });
            },
            renderSections: function() {
                if (this.sectionsCollection) {
                    this.sectionView = new Views.SectionView({ model: this.section });
                    this.sectionView.render();
                } else {
                    this.getSectionsCollection();
                }
            },
            renderSection: function(section) {
                if (this.sectionsCollection) {
                    this.section = this.sectionsCollection.get(section);
                    this.sectionView = new Views.SectionView({ model: this.section });
                    this.sectionView.render();
                } else {
                    this.requestedSection = section;
                    this.getSectionsCollection();
                }
            },
            renderPost: function(post) {
                if (this.postsCollection) {
                    this.post = this.postsCollection.get(post);
                    this.postView = new Views.PostView({ model: this.post });
                    this.postView.render();
                } else {
                    this.requestedPost = post;
                    this.getPostsCollection();
                }
            }
        });
        return Router;
    }
);
