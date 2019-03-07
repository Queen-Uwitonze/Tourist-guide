class MapForm(FlaskForm):
    places = StringField('category',validators=[Required()])
    
    submit = SubmitField('Submit')