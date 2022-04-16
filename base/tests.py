from django.test import TestCase
from django.urls import reverse
from .models import Intentions
import pytest

# Create your tests here.

#unit test for homepage
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

#integration test for Intentions

@pytest.mark.django_db 
def test_create_Intention():
    intention = Intentions.objects.create(
        intention='Pytest',
        category='test',
        requestor='test',
        requestor_email ='test@email.com',
        requestor_phone ='1234567890',
        donation_amount ='100',
        status ='test'
    )
    assert intention.intention == "Pytest"

#using fixtures
@pytest.fixture
def new_intention(db):
    intention = Intentions.objects.create(
        intention='Pytest',
        category='test',
        requestor='test',
        requestor_email ='test@email.com',
        requestor_phone ='1234567890',
        donation_amount ='100',
        status ='test'
    )
    return intention

def test_search_intentions(new_intention):
    assert Intentions.objects.filter(intention='Pytest').exists()

def test_update_intention(new_intention):
    new_intention.intention = 'Pytest-Django'
    new_intention.save()
    assert Intentions.objects.filter(intention='Pytest-Django').exists()


