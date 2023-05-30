from django.core.management.base import BaseCommand, CommandError
from users.models import User


class Command(BaseCommand):
    help = 'Create Admin User'

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--username",
            type=str,
            help="define um nome de usuario",
        )

        parser.add_argument(
            "--password",
            type=str,
            help="define senha",
        )

        parser.add_argument(
            "--email",
            type=str,
            help="define o email de usuario"
        )

    def handle(self, *args: tuple, **options: dict) -> str | None:
        username_var = options.get("username", "admin") or "admin"

        password_var = options.get("password", "admin1234") or "admin1234"
        email_var = options.get("email", f'{username_var}@example.com') or f'{username_var}@example.com'

        usename_exists = User.objects.filter(username=username_var).exists()
        email_exists = User.objects.filter(email=email_var).exists()

        if usename_exists:
            raise CommandError(f"Username `{username_var}` already taken.")
        
        if email_exists:
            raise CommandError(f"Email `{email_var}` already taken.")

        User.objects.create_superuser(
            username=username_var,
            password=password_var,
            email=email_var
        )
        self.stdout.write(self.style.SUCCESS(f"Admin `{username_var}` successfully created!"))
        