# Custom Context_Processors
from menues.models import Menu, MetaInfos


def menulist(request):
    """                                                                         
    A context processor that provides 'menu' for base HTML
    by a special line in settings.py                                    
    """                                                                         
    menulist = Menu.objects.filter(level=1)
    return { 'menulist': menulist }

def level2menulist(request):
    level2menulist= Menu.objects.filter(level=2)
    return  { 'level2menulist':level2menulist }


def metainfos_blogname(request):
    """
    Base.html Blogname
    """
    mblogname = MetaInfos.objects.filter(metainfo_subject='blogname')
    if mblogname:
        for e in mblogname:
            metainfo_blogname = e.metainfo
    else:
        metainfo_blogname = 'simplehome'
    return {'metainfo_blogname':metainfo_blogname}

def metainfos_footer(request):
    """
    Base.html Footer
    """
    mfooter = MetaInfos.objects.filter(metainfo_subject='footer')
    if mfooter:
        for e in mfooter:
            metainfo_footer = e.metainfo
    else:
        metainfo_footer = 'Simplehome Django based Blog Example by Oerb'
    return {'metainfo_footer':metainfo_footer}

def metainfos_author(request):
    """
    Base.html Meta author
    """
    author = MetaInfos.objects.filter(metainfo_subject="author")
    if author:
        for e in author:
            metainfo_author = e.metainfo
    else:
        metainfo_author = ''
    return {'metainfo_author':metainfo_author}

def metainfos_keywords(request):
    """
    Base.html Meta Keywords
    """
    keywords = MetaInfos.objects.filter(metainfo_subject="keywords")
    if keywords:
        for e in keywords:
            metainfo_keywords = e.metainfo
    else:
        metainfo_keywords = ''
    return {'metainfo_keywords':metainfo_keywords}

def metainfos_descriptions(request):
    """
    Base.html Meta descriptions
    """
    descriptions = MetaInfos.objects.filter(metainfo_subject="description")
    if descriptions:
        for e in descriptions:
            metainfo_descriptions = e.metainfo
    else:
        metainfo_descriptions = ''
    return {'metainfo_descriptions':metainfo_descriptions}
