from lib.cog import Cog
from lib.command import Command, command
from lib.web import get


class Chuck(Cog):
    @command(aliases=["coof"], description="")
    def run(self, c: Command):
        self.sendmsg("AH, a tasty bat soup!")
        self.sendmsg("AH, is so tasty!")
        self.sendmsg("so dericious *coof* UH... UH OH")
        self.sendmsg("Oh uh, im.. *coof* *coof* Im gunna...")
        self.sendmsg("OH GOD IM.. IM. IM")
        self.sendmsg("GUNNA COOOOOF... *COOOF COOOF* OH GOD IM COOFING!")
