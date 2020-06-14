from django.utils.text import slugify


from yourapp.utils import random_string_generator

def random_string_generator(size=10, chars=string.acii_lowercase + strin.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):


    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instace.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{random}".format(
                    slug = slug,
                    randstr=random_string_generator(size=4)
            )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug