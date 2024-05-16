from models import Pet, db
from app import app

db.drop_all()
db.create_all()

p1 = Pet(
    name="Trixie",
    species="Cat",
    photo_url="https://www.thesprucepets.com/thmb/MI_DdqwIekRwyKk8oaY7oGbz76U=/1920x0/filters:no_upscale():strip_icc()/step_3-lucky-59b9b688685fbe0011c6ac78-59bae4f0054ad90011988d89.jpg",
    age=8,
    notes="Best cat ever.",
    available=False,
)
p2 = Pet(
    name="Riley",
    species="Dog",
    photo_url="https://mleiatrkukou.i.optimole.com/cb:iQWp.102bc/w:auto/h:auto/q:mauto/f:best/https://bonevoyagedogrescue.com/wp-content/uploads/2023/10/Meet-The-Sheltie-Shetland-Sheepdog-1.jpg",
    age=7,
    notes="Miniature Sheltie",
)
p3 = Pet(
    name="Dakota",
    species="Dog",
    photo_url="https://www.thelabradorsite.com/wp-content/uploads/2023/05/rachael3-1.jpg",
    age=5,
    notes="Chocolate Lab",
)

db.session.add_all([p1, p2, p3])
db.session.commit()
