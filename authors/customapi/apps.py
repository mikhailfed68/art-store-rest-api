from oscarapi import apps


class OscarAPIConfig(apps.OscarAPIConfig):
    name = "oscarapi"

    def ready(self):
        super().ready()
        # Implicitly connect signal handlers decorated with @receiver.
        from authors.customapi import signals
