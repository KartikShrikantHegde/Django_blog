from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

def upload_location(instance,filename):
    return "%s/%s" % (instance.id,filename)

class Post(models.Model):

    ''' Text fiels are lot bigger than char fields
    Username, title are for char fields
    '''

    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location,null=True, blank=True, width_field="width_field",height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()

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
        return reverse("posts:detail",kwargs={"id":self.id})
        #return "posts/%s/" %(self.id)

    class Meta:
        ordering =["-timestamp","-updated"]