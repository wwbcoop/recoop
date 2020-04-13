# django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify

class Initiative(models.Model):
    """ Block of text """

    name = models.CharField(
        _('Nombre'),
        max_length = 128,
        blank = False,
        null = True,
        help_text = _(
            'Nombre de la iniciativa'
        )
    )
    summary = models.TextField(
        _('Descripción'),
        blank=False,
        null=True,
        help_text = _(
            'Explícanos la iniciativa para que podamos valorar tu solicitud'
        )
    )
    ip = models.GenericIPAddressField(
        _('IP'),
        blank = False,
        null = True,
        help_text = _(
            'IP del servidor donde vas a alojar el dominio'
        )
    )
    domain = models.CharField(
        _('Subdominio'),
        max_length = 128,
        blank = False,
        null = True,
        unique = True,
        help_text = _(
            'Escoge el subdominio que deseas usar. Por ejemplo un valor "ejemplo" '
            'creará un subdominio "ejemplo.coop.re"'
        )
    )
    email = models.EmailField(
        _('Correo electrónico'),
        blank=False,
        null=True,
        help_text = _(
            'Un correo electrónico para que podamos contactar contigo'
        )
    )

    # Meta
    slug = models.SlugField(
        _('Content slug'),
        blank=True
    )
    creation_date = models.DateField(
        _('Creation date'),
        editable=False,
        default=timezone.now
    )
    update_date = models.DateField(
        _('Last modified'),
        editable=False,
        auto_now=True,
    )
    published = models.BooleanField(
        _('Publico'),
        blank = False,
        default = False,
    )

    class Meta:
        verbose_name        = _('iniciativa')
        verbose_name_plural = _('iniciativas')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Populate automatically 'slug' field"""
        if not self.slug:
            self.slug = slugify(self.name)
        super(Initiative, self).save(*args, **kwargs)
