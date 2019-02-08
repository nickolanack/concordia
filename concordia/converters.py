from django.urls.converters import SlugConverter


class UnicodeSlugConverter(SlugConverter):
    # This is similar to the slug_unicode_re pattern but is not anchored to the
    # start of the string:
    regex = r"[-\w+]+"