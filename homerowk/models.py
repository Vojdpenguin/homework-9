from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField
from datetime import datetime


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

    def __str__(self):
        return self.fullname


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)

    def __str__(self):
        return f'"{self.quote}" - {self.author.fullname}'


def save_data():
    einstein = Author(
        fullname="Albert Einstein",
        born_date="March 14, 1879",
        born_location="in Ulm, Germany",
        description="In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University of Zurich by 1909..."
    )
    einstein.save()

    steve_martin = Author(
        fullname="Steve Martin",
        born_date="August 14, 1945",
        born_location="in Waco, Texas, The United States",
        description="Stephen Glenn 'Steve' Martin is an American actor, comedian, writer, playwright..."
    )
    steve_martin.save()

    quote1 = Quote(
        tags=["change", "deep-thoughts", "thinking", "world"],
        author=einstein,
        quote="The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."
    )
    quote1.save()

    quote2 = Quote(
        tags=["inspirational", "life", "live", "miracle", "miracles"],
        author=einstein,
        quote="There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle."
    )
    quote2.save()

    quote3 = Quote(
        tags=["adulthood", "success", "value"],
        author=einstein,
        quote="Try not to become a man of success. Rather become a man of value."
    )
    quote3.save()

    quote4 = Quote(
        tags=["humor", "obvious", "simile"],
        author=steve_martin,
        quote="A day without sunshine is like, you know, night."
    )
    quote4.save()
