from flask import request

from app.libs.redprint import RedPrint
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum

from app.models.user import User

api = RedPrint('client')


@api.route('/register', methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
          ClientTypeEnum.USER_EMAIL: __register_user_by_email,
          ClientTypeEnum.USER_MINA: __register_user_by_mina
        }
        promise[form.type.data]()
    return 'success'
    # form json
    # web  モバイル(webモバイル)
    # WTForms


def __register_user_by_email():
    """
    emailの新規処理
    :return:
    """
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)
    pass


def __register_user_by_mina():
    """
    wechatappの新規処理
    :return:
    """
    pass