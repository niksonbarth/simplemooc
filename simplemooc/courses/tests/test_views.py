from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings

from simplemooc.courses.models import Course

class ContactCourseTestCase(TestCase):

    #executa a cada teste
    def setUp(self):
        self.course = Course.objects.create(name='Django', slug='django')

    #executa a cada teste
    def tearDown(self):
        self.course.delete()

    #executa uma ves por classe
    @classmethod
    def setUpClass(cls):
        pass

    #executa uma ves por classe
    @classmethod
    def tearDownClass(cls):
        pass

    def test_contact_from_error(self):
        data = {'name': 'Fulano de Tal', 'email': '', 'message': ''}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_contact_from_success(self):
        data = {'name': 'Fulano de Tal', 'email': 'admin@admin.com', 'message': 'oi'}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])
