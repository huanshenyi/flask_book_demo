from wtforms import Form

from app.libs.error_code import ParameterException

class BaseForm(Form):
    def __init__(self, data):
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # form errors | self.errors fromに属する 本来は異常出さない
            raise ParameterException(msg=self.errors)
