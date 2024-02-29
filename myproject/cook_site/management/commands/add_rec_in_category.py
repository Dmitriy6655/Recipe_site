from django.core.management.base import BaseCommand
from cook_site.models import Recipes, RecipesCategory


class Command(BaseCommand):
    help = "Add Recipe"

    def add_arguments(self, parser):
        parser.add_argument('--recipes_id', default=1, type=int, help='rec_id')
        parser.add_argument('--recipescategory_id', default=1, type=int, help='categ_id')

        # parser.add_argument('--name_category', default='Закуски', type=str, help='name_category')

    def handle(self, *args, **kwargs):
        rec_pk = kwargs.get('recipes_id')
        category_pk = kwargs.get('recipescategory_id')

        rec=Recipes.objects.filter(pk=rec_pk).first()
        category = RecipesCategory.objects.get(pk=category_pk)

        # category.recipe.add(rec, through_defaults={"recipe": rec})
        category.recipe.add(rec)
        # category.recipe.set([rec])


        # ord.product.add(goods, through_defaults={"product": goods})

        self.stdout.write(f'new Recipe {rec.name} add in category {category.name_category}')