from app.libs.redprint import RedPrint


api = RedPrint('user')


@api.route('', methods=["GET"])
def get_user():
    return "get user"


@api.route('', methods=["POST"])
def create_user():
    # 第三者であれば全てがuser
    # user =  client
    # 新規アカウントのタイプも多い email qq
    pass