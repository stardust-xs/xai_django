from django.db import models


class MonitoredApps(models.Model):
  app_id = models.IntegerField(primary_key=True)
  app_activity = models.TextField()
  app_name = models.CharField(max_length=255)
  app_exe = models.CharField(max_length=255)
  app_started = models.DateTimeField()

  def __str__(self):
    return [self.app_name,
            self.app_exe]

  class Meta(object):
    verbose_name_plural = 'Monitored Applications'
