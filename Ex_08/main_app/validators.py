
from django.core.exceptions import ValidationError

class RangeValidators:
    def __init__(self,min_value, max_value,message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self,value):
        if value is None:
            self.__message =  f"The rating must be between {self.min_value} and {self.max_value}"
        else:
            self.__message = value

    def __call__(self, value):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.RangeValueValidator',
            [self.min_value, self.max_value],
            {'message': self.message},
        )
