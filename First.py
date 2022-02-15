from faker import Faker
import  time

fake = Faker()

def get_registered_user():
    return{
        "name":fake.name(),
        "address":fake.address(),
        "created_at":fake.year()
    }

if __name__ == '__main__':
    while True:
        print(get_registered_user())
        time.sleep(5)

