# django
from django.utils.translation import ugettext_lazy as _
from django.db import models
# contrib
from ckeditor_uploader.fields import RichTextUploadingField


class TextBlock(models.Model):
    """ Block of text """

    title = models.CharField(
        _('Nombre'),
        max_length = 128,
        blank = False,
        null = True,
        help_text = _(
            'Escoge el nombre que se verá públicamente asociado a este perfil'
        )
    )
    body = RichTextUploadingField(
        _('Texto'),
        blank=False,
        null=True,
        help_text = _(
            'Texto del bloque'
        )
    )
    body_en = RichTextUploadingField(
        _('Texto inglés'),
        blank=False,
        null=True,
        help_text = _(
            'Texto del bloque en inglés'
        )
    )

    class Meta:
        verbose_name        = _('bloque')
        verbose_name_plural = _('bloques')

    def __str__(self):
        return self.title
