class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply_comment):
        self.replies.append(reply_comment)

    def remove_reply(self):
        self.text = "This comment has been deleted."
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level

        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(level + 1)


root_comment = Comment("What a wonderful book!", "Bodya")
reply1 = Comment("The book is a complete disappointment :(", "Andrew")
reply2 = Comment("What is wonderful about it?", "Maryna")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

root_comment.display()
print("-------")
reply1_1 = Comment("Not a book, but a pile of paper was transferred for nothing...", "Sergey")
reply1.add_reply(reply1_1)
root_comment.display()
print("-------")
reply1.remove_reply()

root_comment.display()