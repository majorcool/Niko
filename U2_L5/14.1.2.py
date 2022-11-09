class User:
    def __init__(self, id_: str, nickname: str, credits: int):
        self.id_ = id_
        self.nickname = nickname
        self.credits = credits

    def get_info(self):
        print("id=", self, id_, "\nnickname=", self.nickname, "\ncredits=", credits)

    def upgrade_to_vip(self, level):
        return Vip(self.id_, self.nickname, self.credits, level)

    pass


class Vip(User):
    def __init__(self, id_: str, nickname: str, credits: int, level: int):
        super().__init__(id_, nickname, credits)
        self.level = level

    def get_info(self):
        super().get_info()
        print("\nlevel=", self.level)

    pass
