from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField


class BlogGroup(models.Model):
    title = models.CharField(_('group title'), max_length=200, default='')

    # python 2.x
    def __unicode__(self):
        return self.title

    # python 3.x
    def __unicode__(self):
        return self.title

class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('owner'), null=True)
    group = models.ForeignKey(BlogGroup, verbose_name=('group'), related_name='group', on_delete=models.CASCADE, null=True)
    title = models.CharField(_('title'), max_length=120)
    image = models.ImageField(_('main image'), upload_to='blog/%Y-%m-%d', blank=True, null=True)
    content = RichTextUploadingField(_('content'), config_name='default')
    attach_file = models.FileField(_('Attach File'), null=True, blank=True, help_text=_('this is optional.'))
    updateDateTime = models.DateTimeField(_('create date'), auto_now_add=True, auto_now=False)
    createDateTime = models.DateTimeField(_('update date'), auto_now_add=False, auto_now=True)

    # python 2.x
    def __unicode__(self):
        return self.title

    # python 3.x
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id':self.id})