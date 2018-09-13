from Caculator import Caculator, CaculationError


# what?
# caculate expression, and compare to expected value
class CaculatorLibrary(object):
    def __init__(self):
        self._cal = Caculator()

    def caculate(self, buttons):
        # filter out space: buttons.replace(' ', '')
        for button in buttons.replace(' ', ''):
            print(button, type(button))
            result = self._cal.push(button)
        else:
            return result

    def should_fail(self, expression):
        try:
            self.caculate(expression)
        except CaculationError as e:
            return str(e)
        else:
            AssertionError('%s should fail' % expression)