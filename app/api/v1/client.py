from app.libs.redprint import RedPrint

api = RedPrint('client')


@api.route('/register')
def create_client():
    # WTForms
    pass