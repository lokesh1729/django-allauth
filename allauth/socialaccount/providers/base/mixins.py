from django.shortcuts import render

from allauth.account import app_settings as account_app_settings
from allauth.socialaccount import app_settings


class OAuthLoginMixin:
    def dispatch(self, request, *args, **kwargs):
        provider = self.adapter.get_provider()
        # Default LOGIN_ON_GET value is False and request method is also GET. What will happen?
        if (not app_settings.LOGIN_ON_GET) and request.method == "GET":
            # What will happen when the POST method is called from the web?
            return render(
                request,
                "socialaccount/login." + account_app_settings.TEMPLATE_EXTENSION,
                {
                    "provider": provider,
                    "process": request.GET.get("process"),
                },
            )
        return self.login(request, *args, **kwargs)

    def login(self, request, *args, **kwargs):
        raise NotImplementedError
