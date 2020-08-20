from django.test import TestCase
from after_deploy.models import tasks as taskModel
from after_deploy.management.commands import after_deploy as afterDeployCommand

class TaksTestCase(TestCase):
    def setUp(self):
        taskModel.objects.create(pk='20200819232557',)
        taskModel.objects.create(pk='20200412112437',)

    def test_if_task_is_save(self):
        first  = taskModel.objects.get(pk='20200819232557')
        second = taskModel.objects.get(pk='20200412112437')
        self.assertEqual(first.pk,  '20200819232557')
        self.assertEqual(second.pk, '20200412112437')
