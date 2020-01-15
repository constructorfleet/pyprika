# Pyprika
Python Package to talk to Paprika's backend server.

## Features
* Configurable periodic retrieval of data
* Recipes, Categories, Meals, Menus are all linked via relational id
* Ability to filter recipes that include categories, exclude categories, total cook/prep duration, recipe difficulty and recipe names.

## Usage
### Initialize
Initialize `Pyprika` with your username and password from your mobile app. If you so choose, you can also tell it to auto fetch after a certain delay:

```python
pyprika = Pyprika(username, password)
```

```python
pyprika = Pyprika(username, password, fetch_delay=timedelta(hours=2), auto_fetch=True)
```

### Get all data

```python
recipe_book = pyprika.get_all()
```

### Filter recipes

```python
recipes = pyprika.get_recipes(
            categories=None,
            not_categories=None,
            difficulty=None,
            duration=None,
            name_like=None,
            name_not_like=None
          )
```
**NOTE** All arguments here are optional. Passing no arguments will return every recipe.

### Enable/disable auto fetch

```python
pyprika.set_auto_fetch(True)  #Enable auto-fetch after delay
pyprika.set_auto_fetch(False)  #Disable auto-fetch immediately
```