from django.contrib.auth.models import User
from posts.models import Post

# python manage.py makemigrations  # create all models(tables)
# python manage.py migrate  # create all models(tables)

user1 = User(username="surajgupta", email="surajgupta@email.com", password="@pa55word@")
user1.save()
user1 = User.objects.filter_by(username="surajgupta").first()
post1 = Post(title="Blog Post 1", content="Blog Post 1 content", author=user1)
post1.save()
# user1.posts  # [Blog Post 1 - 2024-12-15 17:38:29.005847]
# post1.user_id  # 1

user2 = User(username="testuser", email="testuser@email.com", password="@p55sword@")
user2.save()
user2 = User.objects.filter_by(username="testuser").first()
post2 = Post(title="Blog Post 2", content="Blog Post 2 content", author_id=user2.id)
post2.save()
# user2.posts  # [Blog Post 2 - 2024-12-15 17:38:29.005847]
# post2.user_id  # 2

User.objects.all()  # True
User.objects.first()  # True
User.objects.count()  # True
users = User.objects.filter(username="surajgupta").all()  # True
user1 = User.objects.filter(username="surajgupta").first()  # True
User.objects.get(username="surajgupta")  # True
user = User.objects.last()  # True
post = Post(title="Blog Post 1", content="Blog Post 1 content", author=user)
print(post.author.email)
for i in range(1, 13):
    post = Post(title=f"Blog Post {i}", content=f"Blog Post {i} content", author=user)
    post.save()
user.post_set.all()
user.post_set.count()
user.post_set.create(title="Blog Post 3", content="Blog Post 3 content")

users = User.objects.all()
for user in users:
    for i in range(1, 13):
        post = Post(title=f"Blog Post {i}", content=f"Blog Post {i} content", author=user)
        post.save()


# from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
# s = Serializer("secret")
# token = s.dumps({"user_id": "1"})
# s.loads(token, max_age=30)
