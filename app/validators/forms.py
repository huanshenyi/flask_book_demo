from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.libs.enums import ClientTypeEnum


class ClientForm(Form):
    """
    アカウント
    パスワード secret
    クライアントタイプ
    """
    account = StringField(validators=[DataRequired(), length(
        min=5, max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    # クライアントタイプ検証の関数
    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
           raise e
        pass