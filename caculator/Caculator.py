class Caculator(object):
    Buttons = '0123456789-+*/=C'
    def __init__(self):
        self._result = ''

    def push(self, button):
        if button not in self.Buttons:
            raise CaculationError('invalid button')
        elif button == '=':
            self._result = self._calculate()
        elif button == 'C':
            self._result = ''
        elif button == '/':
            self._result += '//'
        else:
            self._result += button

        return self._result

    def _calculate(self):
        try:
            return str(eval(self._result))
        except ZeroDivisionError:
            raise CaculationError('zero division')
        except SyntaxError:
            raise CaculationError('invalid expression')
        
class CaculationError(Exception):
    pass