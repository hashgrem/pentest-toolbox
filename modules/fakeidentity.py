from faker import Faker
from colorama import Fore, Back, Style
import random
import datetime

def generate_age():
    return random.randint(18, 90)

def generate_birthdate(age):
    year = datetime.datetime.now().year - age
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.datetime(year, month, day)   

# Génération d'une instance de Faker avec une locale choisie
def get_fake_instance(locale):
    return Faker(locale)

# Génération d'un nom aléatoire
def generate_name(fake_instance):
    return fake_instance.name()

# Génération d'un job aléatoire
def generate_job(fake_instance):
    return fake_instance.job()

# Génération d'une adresse aléatoire
def generate_address(fake_instance):
    return fake_instance.address()

# Génération d'un mail aléatoire
def generate_email(fake_instance):
    return fake_instance.email()

# Fonction principale pour générer une fausse identité
def generate_fake_identity(locale):
    fake_instance = get_fake_instance(locale)
    name = generate_name(fake_instance)
    age = generate_age()
    birthdate = generate_birthdate(age)
    address = generate_address(fake_instance)
    job = generate_job(fake_instance)
    email = generate_email(fake_instance)

    fake_identity =  {
        'name': name,
        'age': age,
        'birth': birthdate,
        'address': address,
        'job' : job,
        'email' : email
    }

    fake_data = "\n\n===================\n"
    fake_data += "Your fake identity\n"
    fake_data += "===================\n"

    for element, value in fake_identity.items():
        fake_data += f"{Fore.GREEN}{element}{Style.RESET_ALL}\t=>\t{Fore.MAGENTA}{value}{Style.RESET_ALL}\n"
    
    return fake_data


