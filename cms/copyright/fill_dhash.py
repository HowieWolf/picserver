import os

from PIL import Image

from datamodel.models import Copyright
from picserver.settings import BASE_DIR
from similarity import DHash
from util.base.view import BaseView


class FillDHashForCopyright(BaseView):

    def post(self, request, **kwargs):
        qs = Copyright.objects.filter(dhash='')
        for p in qs:
            path = os.path.join(BASE_DIR, p.img.url)
            if not os.path.exists(path):
                continue
            dhash = DHash.calculate_hash(Image.open(path))
            Copyright.objects.filter(id=p.id).update(dhash=dhash)
        return self.success()
