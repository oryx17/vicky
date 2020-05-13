from lib.cog import cog
from lib.command import Command, command


class Calc(Cog):
    @command(aliases=["calc"], description="")
    def do_calculation(self, c: Command):
        # c holds the needed shit
        print(f"{c.prefix} is the command prefix")
        print(f"{c.data} is the 'raw' message")
        print(f"{c.name} is the nick of the user who sent")
        print(f"{c.message} is the relevant bit of the message")
        message_parts = c.message.split(" ")
        print(f"Message parts: {message_parts}")
        # lisp style
        if message_parts[0] == "+" and len(message_parts) == 3:
            # arrays start at zero, len() starts at 1
            # also, type casting
            toadd1 = int(message_parts[1])
            toadd2 = int(message_parts[2])
            total = toadd1 + toadd2
            self.sendmsg("Your total is: {}".format(total))
        elif message_parts[0] == "-" and len(message_parts) == 3:
            tosub1 = int(message_parts[1])
            tosub2 = int(message_parts[2])
            subbed = tosub1 - tosub2
            self.sendmsg("Your total is: {}".format(subbed))
        elif message_parts[0] == "*" and len(message_parts) == 3:
            toMulti1  = int(message_parts[1])
            toMulti2 = int(message_parts[2])
            multiTotal = toMulti1 - toMulti2
            self.sendmsg("Your total is: {}".format(multiTotal))
        else:
            self.sendmsg("I only weached de furst gwade :(")



