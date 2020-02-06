import kivy
import os
from os.path import dirname
from kivy.lang import Builder
from controller.CalculatorApp import CalculatorApp

kivy.require("1.11.1")


class Main:
    loaded = False

    def __init__(self):
        self.view_dir = os.path.join(dirname(__file__), 'view')
        self.loaded = self._loader()

    def _loader(self) -> bool:
        """
        Load the ux assets inside the specified view directory.

        :return: bool
        """

        try:
            # Loop through the specified dir assuming that it contains all the view files.
            for File in os.listdir(self.view_dir):
                # Preload the files on init so that it will be available
                # for controllers to call.
                if File.endswith('kv'):
                    Builder.load_file(f'{self.view_dir}/{File.lower()}')

            return True
        except FileNotFoundError:
            return False

    def main(self):
        """
        Application logic will be invoked in this method.

        :return: None
        """
        if self.loaded:
            CalculatorApp().run()


if __name__ == '__main__':
    Main().main()
