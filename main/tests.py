from django.urls import reverse
from django.core import mail

def test_main_page(client, faker):
    response = client.get(reverse('main'))
    assert response.status_code == 200
    assert b'PizzaHut were always here' in response.content

    data = {
        'email': faker.word(),
        'text': faker.sentence()
    }
    response = client.post(reverse('main'), data=data)
    assert response.status_code == 200
    assert not len(mail.outbox)

    data = {
        'email': faker.email(),
        'text': faker.sentence()
    }
    response = client.post(reverse('main'), data=data, follow=True)
    assert response.status_code == 200
    assert any(i[0] == reverse('main') for i in response.redirect_chain)
    assert mail.outbox[0].from_email == data['email']
    assert mail.outbox[0].body == data['text']
