from flask import (request, render_template, redirect, url_for, flash, g, jsonify, abort, json)
from flask.ext.login import current_user, login_required, login_user, logout_user
from flask_labs import app, db
from flask_labs.models import User, Section, Post, Quotation, Registry
from flask_labs.forms import LoginForm, EditorForm, RegistryForm


@app.before_request
def before_request():
    writing = Section.query.filter(Section.name == "Writing").first()
    design = Section.query.filter(Section.name == "Design").first()
    g.sections = [design, writing]
    g.current_user = current_user


@app.route("/")
def index():
    lead = Post.get_recent(num_posts=4, random_post=True)
    quotation = Quotation.random_quote()
    return render_template("index.html",
                            lead=lead,
                            quotation=quotation)


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm(request.form, next=request.args.get('next'))
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username == login_form.username.data).first()
        if user is not None and user.check_password(login_form.raw_password.data):
            if login_user(user):
                flash('Logged in.')
            else:
                # probably deactivated
                flash('Failed to log in.')
            return redirect(login_form.next.data or url_for('index'))
        flash('Login incorrect.')
        return redirect(request.referrer)
    return render_template('login.html', login_form=login_form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.')
    return redirect(url_for('index'))


@app.route('/admin/posts')
def admin_posts():
    editor_form = EditorForm(request.form)
    return render_template('editor.html', editor_form=editor_form)


@app.route('/admin/post/<post_slug>')
def post_editor(post_slug):
    this_post = Post.query.filter(Post.slug == post_slug)
    editor_form = EditorForm(request.form, this_post)
    return render_template('editor.html', editor_form=editor_form)


@app.route('/sections')
def sections():
    sections = Section.query.all()
    if request.is_xhr:
        return jsonify(sections=[section.serialize for section in sections])
    abort(404)


@app.route('/sections/<section_slug>')
def section(section_slug):
    section = Section.query.filter(Section.slug == section_slug).first_or_404()
    if request.is_xhr:
        return jsonify(posts=[post.serialize for post in section.posts])
    return render_template('section.html',
                            title=section.name,
                            section=section)


@app.route('/posts')
def posts():
    posts = Post.query.all()
    if request.is_xhr:
        return jsonify(posts=[post.serialize for post in posts])
    abort(404)


@app.route('/posts/<post_slug>')
def post(post_slug):
    post = Post.query.filter(Post.slug == post_slug).first_or_404()
    if request.is_xhr:
        return jsonify(post=post.serialize)
    return render_template('post.html',
                            title=post.title,
                            post=post,
                            current_section=post.section)


@app.route('/registry', methods=['POST', 'GET'])
@login_required
def registry():
    registry_items = {
        'normal': Registry.query.filter(Registry.is_special != True).order_by('book_author').all(),
        'special': Registry.query.filter(Registry.is_special == True).order_by('book_author').all()
    }
    registry_form = RegistryForm(request.form)
    if request.method == 'POST':
        if registry_form.book_title.data is not None:
            item = Registry(registry_form.book_title.data,
                            registry_form.book_author.data,
                            registry_form.is_special.data,
                            registry_form.item_notes.data)
            if not item.exists():
                db.session.add(item)
                db.session.commit()
                flash('Item added to registry')
            else:
                flash('Item already exists in registry')
            return redirect(url_for('registry'))
        if request.is_xhr:
            item_id = request.json.get('id')
            registry_item = Registry.query.get(item_id)
            response = registry_item.buy()
            return render_template('ajax/response.json', response=response)
    return render_template('registry.html',
                            title='Wedding Registry',
                            registry_items=registry_items,
                            registry_form=registry_form)
