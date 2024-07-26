import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article
from django.db.models import Q, Count, Avg


# Create queries within functions


# print(Author.objects.get_authors_by_article_count())


def get_authors(search_name=None, search_email=None):
    auth = None
    if search_name is None and search_email is None:
        return ""

    if search_name is not None and search_email is not None:
        # query = Q(full_name__icontains=search_name) and Q(email__icontains=search_email)
        auth = Author.objects.filter(full_name__icontains=search_name, email__icontains=search_email).order_by('-full_name')
    elif search_name is not None:
        auth = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')
    elif search_email is not None :
        auth = Author.objects.filter(email__icontains=search_email).order_by('-full_name')
    res = []
    [res.append(f'Author: {author.full_name}, email: {author.email}, status: {"Banned" if author.is_banned else "Not Banned"}')
     for author in auth if auth]

    return "\n".join(res) if res else ""

# print(get_authors("o", "@"))

def get_top_publisher():
    author = Author.objects.annotate(publications_count=Count("articles")).order_by('-publications_count', 'email').first()
    # author = Author.objects.get_authors_by_article_count.first()
    if  author is None or author.publications_count==0:
        return ""
    return f"Top Author: {author.full_name} with {author.publications_count} published articles."

# print(get_top_publisher())

def get_top_reviewer():
    author = Author.objects.annotate(reviews_count=Count("reviews")).order_by('-reviews_count', 'email').first()
    if  author is None or author.reviews_count == 0:
        return ""
    return f"Top Reviewer: {author.full_name} with {author.reviews_count} published reviews."


# print(get_top_reviewer())


def get_latest_article():
    article = Article.objects.prefetch_related('authors', 'reviews').annotate(average_rating=Avg('reviews__rating')).order_by('-published_on').first()
    if article is None:
        return ""
    num_reviews = article.reviews.count()
    avg_rating = article.average_rating if article.average_rating else 0.0
    return f"The latest article is: {article.title}. Authors: {', '.join(x.full_name for x in article.authors.all().order_by('full_name'))}. Reviewed: {num_reviews if num_reviews else 0} times. Average Rating: {avg_rating:.2f}."

print(get_latest_article())



def get_top_rated_article():
    top_rated_article = Article.objects.annotate(avg_rating=Avg('reviews__rating')) \
        .order_by('-avg_rating', 'title') \
        .first()

    num_reviews = top_rated_article.reviews.count() if top_rated_article else 0
    if top_rated_article is None or num_reviews == 0:
        return ''

    avg_rating = top_rated_article.avg_rating or 0.0
    return f"The top-rated article is: {top_rated_article.title}, with an average rating of {avg_rating:.2f}, " \
           f"reviewed {num_reviews} times."



def ban_author(email=None):
    author = Author.objects.filter(email__exact=email).first()
    # print(author.full_name)
    if email is None or author is None:
        return "No authors banned."

    num_rev = author.reviews.count()
    author.is_banned = True
    author.save()
    author.reviews.all().delete()

    return f"Author: {author.full_name} is banned! {num_rev} reviews deleted."

# print(ban_author("ban@ban.bg"))
