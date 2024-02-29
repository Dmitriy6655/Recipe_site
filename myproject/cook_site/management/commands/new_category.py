from django.core.management.base import BaseCommand
from cook_site.models import Recipes, RecipesCategory


class Command(BaseCommand):
    help = "Create new Recipe"

    def add_arguments(self, parser):
        parser.add_argument('--name_category', default='Горячие блюда', type=str, help='name_category')

    def handle(self, *args, **kwargs):
        name_category = kwargs.get('name_category')


        RecipesCategory.objects.create(name_category=name_category)

        self.stdout.write(f'new category {name_category} created')
