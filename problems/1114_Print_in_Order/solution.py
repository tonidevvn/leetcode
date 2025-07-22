class Foo(object):
    def __init__(self):
        self.count = 1
        pass


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        if self.count == 1:
            printFirst()
            self.count += 1


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        while self.count < 2:
            pass        
        printSecond()
        self.count+=1
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.
        while self.count < 3:
            pass
        printThird()