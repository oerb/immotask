from blog.models import Item
from django import template
register = template.Library()

def menu(request):
    menu_items = Item.objects.all() # TODO: here must Menulist to be implemented
    print("Menu is used")
    return {"menu_items": menu_items}

register.inclusion_tag('menu/menu.html')(menu)