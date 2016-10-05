from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('owner'), null=True)
    title = models.CharField(_('title'), max_length=120)
    image = models.ImageField(_('main image'), upload_to='blog/%Y-%m-%d', blank=True, null=True)
    content = RichTextUploadingField(_('content'), config_name='default')
    updateDateTime = models.DateTimeField(_('create date'), auto_now_add=True, auto_now=False)
    createDateTime = models.DateTimeField(_('update date'), auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'id':self.id})