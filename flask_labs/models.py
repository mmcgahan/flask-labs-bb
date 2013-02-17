import random, pdb
from markdown import markdown
from sqlalchemy import sql, and_
from flask_labs import db, bcrypt
from flask_labs.utils import make_slug, dump_datetime


post_tag = db.Table('post_tag', db.Model.metadata,
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    quote_id = db.Column(db.Integer, db.ForeignKey('quotation.id'))
    title = db.Column(db.String(255), nullable=False)
    subtitle = db.Column(db.String(255))
    slug = db.Column(db.String(255), nullable=False, unique=True)
    teaser = db.Column(db.String(511))
    lead_img = db.Column(db.String(255), default="default.jpg")
    markdown = db.Column(db.Text)
    html = db.Column(db.Text)
    create_date = db.Column(db.TIMESTAMP, default=sql.functions.current_timestamp())

    def set_html(self):
        self.html = markdown(self.markdown)

    @property
    def serialize_leaf(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'slug': self.slug,
            'uri': '/posts/%s' % self.slug,
            'teaser': self.teaser,
            'lead_img': self.lead_img,
            'markdown': self.markdown,
            'html': self.html,
            'create_date': dump_datetime(self.create_date),
            'tags': [tag.name for tag in self.tags]
        }

    @property
    def serialize(self):
        """Return object data with related object data in easily serializeable format"""
        # pdb.set_trace()
        leaf = self.serialize_leaf
        leaf.update({
            'author': self.author.serialize_leaf,
            'section': self.section.serialize_leaf
        })
        return leaf

    @staticmethod
    def get_recent(num_posts=1, random_post=False, section_name=None):
        base_query = Post.query.order_by(sql.expression.desc(Post.create_date))
        if section_name is not None:
            base_query = base_query.join(Section).filter(Section.name == section_name)
        recent_posts = base_query.limit(num_posts).all()
        return (random.choice(recent_posts) if random_post else recent_posts)

    def __init__(self,
                title,
                markdown_content=''):
        self.title = title
        self.slug = make_slug(title)
        self.markdown = markdown_content
        self.set_html()


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    image = db.Column(db.String(255))
    # content type can be image, post, or page (content will be formatted this way)
    description = db.Column(db.String(511))
    content_type = db.Column(db.String(255), default='post')
    posts = db.relationship('Post', backref='section')
    topics = db.relationship('Topic', backref='section')

    @property
    def serialize_leaf(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'image': self.image,
            'description': self.description
        }

    @property
    def serialize(self):
        """Return object data with related object data in easily serializeable format"""
        # pdb.set_trace()
        leaf = self.serialize_leaf
        leaf.update({
            'posts': [post.serialize_leaf for post in self.posts]
        })
        return leaf

    def __init__(self, name, description='', content_type='post'):
        self.name = name
        self.slug = make_slug(name)
        self.description = description
        self.content_type = content_type


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    create_date = db.Column(
        db.TIMESTAMP,
        default=sql.functions.current_timestamp()
    )
    posts = db.relationship('Post', backref='author')
    active = db.Column(db.Boolean(), default=True, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)

    @property
    def serialize_leaf(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def check_password(self, raw_pw):
        return bcrypt.check_password_hash(
            self.password,
            '%s%s' % (self.username, raw_pw)
        )

    def set_password(self, raw_pw):
        self.password = bcrypt.generate_password_hash(
            '%s%s' % (self.username, raw_pw)
        )

    @staticmethod
    def username_exists(username):
        return db.session.query(
            sql.exists().where(User.username == username)
        ).scalar()

    def __init__(self, username, raw_pw, first_name='', last_name=''):
        self.username = username
        self.set_password(raw_pw)
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User %s>' % self.username


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), default='')
    posts = db.relationship('Post', secondary=post_tag, backref='tags')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{}'.format(self.name)


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)

    def __init__(self, name, section):
        self.name = name
        self.section = section


class Quotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(1023), nullable=False)
    source = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255))
    posts = db.relationship('Post', backref='quote')

    @staticmethod
    def random_quote():
        return Quotation.query.order_by(sql.func.rand()).first()

    def __init__(self, quote, source):
        self.quote = quote
        self.source = source


class Registry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(255))
    book_author = db.Column(db.String(255))
    is_special = db.Column(db.Boolean, default=False)
    item_notes = db.Column(db.Text)
    bought = db.Column(db.Boolean, default=False)

    def buy(self):
        self.bought = True
        db.session.add(self)
        db.session.commit()
        return self.bought

    def exists(self):
        check_item = Registry.query.filter(and_(
            Registry.book_title == self.book_title,
            Registry.book_author == self.book_author
        )).first()
        return check_item is not None

    def __init__(self, title, author, is_special=False, notes=None, bought=False):
        self.book_title = title
        self.book_author = author
        self.is_special = is_special
        self.item_notes = notes
        self.bought = bought
