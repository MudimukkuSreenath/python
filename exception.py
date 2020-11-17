class Demo:
    @staticmethod
    def dowork1():
        try:
            try:
                ages=[21,22,23]
                print(ages[3])
            except Exception as e:
                print('inner exception is caught:',e)
            a,b=10,0
            print(a/b)
        except Exception as e:
            print('outer exception is caught:',e)
Demo.dowork1()