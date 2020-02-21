from django.test import TestCase
from after_deploy.models import tasks as taskModel
from after_deploy.management.commands import after_deploy as afterDeployCommand

class TaksTestCase(TestCase):
    def setUp(self):
        taskModel.objects.create(pk='000245',)
        taskModel.objects.create(pk='005702',)

    def test_if_task_is_save(self):
        first  = taskModel.objects.get(pk='000245')
        second = taskModel.objects.get(pk='005702')
        self.assertEqual(first.pk,  '000245')
        self.assertEqual(second.pk, '005702')
