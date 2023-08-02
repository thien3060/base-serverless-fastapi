import os
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from app.core.config import settings


def get_dynamodb_host():
    if os.environ.get('IS_OFFLINE', "false") == "true":
        host = 'http://localhost:8800'
    else:
        host = f'https://dynamodb.{settings.DYNAMODB_REGION}.amazonaws.com'
    return host


class User(Model):
    class Meta:
        table_name = settings.USER_DYNAMODB_TABLE
        host = get_dynamodb_host()
        region = settings.DYNAMODB_REGION

    user_id = UnicodeAttribute(hash_key=True, null=False)
    user_name = UnicodeAttribute(null=False)
    createdAt = UTCDateTimeAttribute(null=False, default=datetime.now())
    updatedAt = UTCDateTimeAttribute(null=False)

    def save(self, conditional_operator=None, **expected_values):
        self.updatedAt = datetime.now()
        super(User, self).save()

    def __iter__(self):
        for name, attr in self.get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
