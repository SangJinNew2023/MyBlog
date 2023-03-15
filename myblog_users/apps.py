from django.apps import AppConfig


class MyblogUsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myblog_users"

    def ready(self):
        import myblog_users.signals
