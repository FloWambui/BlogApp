from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class AddBlog(FlaskForm):
    title = StringField('Title', validators =[DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post Blog')

class CommentForm(FlaskForm):

    comment = StringField('Add a Comment',validators=[DataRequired()])
    submit = SubmitField('Submit')

