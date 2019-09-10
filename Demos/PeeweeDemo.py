from peewee import *
from datetime import date

db = SqliteDatabase('people.db')


# Model Definition
class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


# connect to database
db.connect()


# create tables
db.create_tables([Person, Pet])


# add data
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save()

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='mittens', animal_type='cat')

# modify data
grandma.name = 'Lily'
grandma.save()

herb_fido.owner = uncle_bob
herb_fido.save()

# delete data
herb_mittens.delete_instance()

# query data
grandma = Person.get(Person.name == 'Lily')

for person in Person.select():
    print(person.name)

query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

query = (Pet.select(Pet, Person).join(Person).where(Pet.animal_type == 'cat'))
for pet in query:
    print(pet.name, pet.owner.name)

query = (Pet.select().join(Person).where(Person.name == 'Bob'))
for pet in query:
    print(pet.name)

for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print(pet.name)

d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person.select().where(Person.birthday < d1940 | Person.birthday > d1960))
for person in query:
    print(person.name, person.birthday)

for person in Person.select():
    print(person.name, person.pets.count(), 'pets')


# close database
db.close()