from django.core.management.base import BaseCommand
from cook_site.models import Recipes, RecipesCategory
from faker import Faker


class Command(BaseCommand):
    help = "Create new Recipe"

    def add_arguments(self, parser):
        faker = Faker('ru-ru')
        parser.add_argument('--name', default=faker.text(max_nb_chars=15), type=str, help='Recip name' )
        parser.add_argument('--description', default=faker.text(max_nb_chars=30), type=str, help='description')
        parser.add_argument('--cooking_steps', default=faker.text(max_nb_chars=10), type=str, help='cooking_steps')
        parser.add_argument('--cooking_time', default=faker.random_number(digits=3, fix_len=False), type=int, help='cooking_time')
        parser.add_argument('--author', default=faker.name(), type=str, help='Name author')
        parser.add_argument('--recipescategory_id', default=1, type=int, help='recipescategory ID')



    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        cooking_steps = kwargs.get('cooking_steps')
        cooking_time = kwargs.get('cooking_time')
        rec_id=kwargs.get('recipescategory_id')
        author = kwargs.get('author')

        category = RecipesCategory.objects.get(pk=rec_id)


        new_recipe = Recipes.objects.create(
            name=name,
            description=description,
            cooking_steps=cooking_steps,
            cooking_time=cooking_time,
            image='',
            author=author,
            date_create='',
            recipescategory=category        #добавляем рецепт в категорию  recipescategory_id


        )


        self.stdout.write(f'Recipe {new_recipe.name} created')