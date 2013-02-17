from flask_labs.models import User, Section, Topic, Quotation
from flask_labs import app, db


def setup():
    if (raw_input('Delete database? (y/n) ') == 'y'):
        db.drop_all()
        db.create_all()
        print 'creating admin user...'
        admin_user = User(username='Admin', raw_pw=app.config['INITIAL_PASSWORD'])
        print 'adding objects to database...'
        writing_section = Section('Writing', 'images/plume.png')
        design_section = Section('Design', 'images/chalkboard.png')
        photo_section = Section('Photography', 'images/camera.png')
        about_section = Section('About', 'images/user.png')
        db.session.add_all([
            admin_user,
            writing_section,
            design_section,
            photo_section,
            about_section,
            Topic('Programming', writing_section),
            Topic('Education', writing_section),
            Topic('Design', writing_section),
            Topic('Travel', writing_section),
            Topic('Web', design_section),
            Topic('Information', design_section),
            Topic('Interaction', design_section),
            Topic('Travel', photo_section),
            Topic('People', photo_section),
            Topic('CV', about_section),
            Topic('Contact', about_section),
            Quotation('The universe is a big place, perhaps the biggest.', 'Kurt Vonnegut')
        ])
        db.session.commit()
        print 'done.'
    return True


if __name__ == '__main__':
    setup()
