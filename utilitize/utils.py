import softest
import logging

class Utilz(softest.TestCase):
    def assert_item_in_list(self, lists, value):
        for stop in lists:
            print(f"Text is " + stop.text)
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("passed")
            else:
                print("failed")
        self.assert_all()


    def custome_logger(logLevel=logging.DEBUG):
        # Create logger
        logger = logging.getLogger("logger")
        logger.setLevel(logLevel)
        fil = logging.FileHandler("automation.log", mode='w')
        format = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fil.setFormatter(format)
        logger.addHandler(fil)
        return logger
