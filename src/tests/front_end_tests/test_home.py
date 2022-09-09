from core.page_models.index_pet_store import IndexPetStore


def test_home(browser):
    index_home = IndexPetStore(browser)
    index_home.load()