from django.urls import reverse
from pytest_django.asserts import assertContains

@pytest.fixure
def resposta(client):
    return client.get(reverse('tarefas:home'))

def test_status_code(client):
    assert resposta.status_code == 200

def test_formulario_present(client):
    assertContains(resposta, '<form')

def test_button_save_present(client):
    assertContains(resposta, '<button type="submit"')


    