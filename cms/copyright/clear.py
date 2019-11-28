import os

from datamodel.models import Copyright
from picserver.settings import BASE_DIR
from util.base.view import BaseView


class ClearErrorCopyright(BaseView):

    def delete(self, request, **kwargs):
        qs = Copyright.objects.all()
        for p in qs:
            path = os.path.join(BASE_DIR, p.img.url)
            if os.path.exists(path):
                continue
            p.delete()
        return self.success()
