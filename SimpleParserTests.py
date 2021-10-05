import sys
from SimpleParser import SimpleParser


class SimpleParseTests:
    """
    簡單示範沒用測試框架的單元測試
    """

    def testReturnsZeroWhenEmptyString(self):
        try:
            sp = SimpleParser()
            result = sp.parseAndSum('')
            if(result != 0):
                print('Test Error')
            else:
                print('Test OK')
        except:
            print("Unexpected error:", sys.exc_info())
            raise


test = SimpleParseTests()
test.testReturnsZeroWhenEmptyString()
