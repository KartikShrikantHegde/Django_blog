from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

def upload_location(instance,filename):
    return "%s/%s" % (instance.id,filename)

class Post(models.Model):

    ''' Text fiels are lot bigger than char fields
    Username, title are for char fields
    '''

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,null=True, blank=True, width_field="width_field",height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)

    ''' Auto_now        --> Every time it is something is saved into database it will update it
        Auto_now_add    -->  Whenever it is added into the database initially not whenever it is saved.
                             So its one time. So saved and set.   '''

    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

# If the unicode data is not there then it will just show 'Post object' in the admin page rather than showing the actual object
# So the unicode is important as it refers to the actual object being created

    def __unicode__(self):
        return self.title

# for python 3.0 users

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})


    class Meta:
        ordering =["-timestamp","-updated"]

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

# if this function recieves anything else then, add those into args or keyword args

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)
