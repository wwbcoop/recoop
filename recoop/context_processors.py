# django
from django.conf import settings

def site_info_processor(request):
    """Injects into global context the defaults about the HTML document"""

    document_title       = settings.DOCUMENT_TITLE
    document_description = settings.DOCUMENT_DESCRIPTION

    return locals()

def debug_processor(request):
    """Injects debug flags into context"""

    debug    = settings.DEBUG
    debug_js = settings.DEBUG_JS
    debug_css = settings.DEBUG_CSS

    return locals()
