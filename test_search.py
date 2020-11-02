from http import HTTPStatus

import self as self
from django.test import TestCase

class FoodSearchTests(TestCase):
    def test_get(self):
        response = self.client.get("/nutrihacker/search")

        self.assertEqual(response.status_code, HTTPStatus.OK)


    def test_searchFood_success(self):
        response = self.client.get(
            "/nurtrihacker/search", data={"name": "Pineapple"}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)


class RecipeSearchTests(TestCase):
    def test_get(self):
        response = self.client.get("/nutrihacker/search-recipe")

    def test_searchRecipe_success(self):
            response = self.client.get(
                "/nurtrihacker/search-recipe", data={"name": "Crab"}
            )


