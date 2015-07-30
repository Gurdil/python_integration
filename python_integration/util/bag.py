__author__ = 'philip_j'
__all__ = ['Speaking']


class Speaking():
    """
    An exemple interface
    """

    def speak(self, name=None):
        """
            Print the class name

            :param name: the name to print
            :type name: String
            :return: None
        """
        if name == None:
            name = self.__class__.__name__

        print('''I'm a ''' + name + ' class.')


def main():
    s = Speaking()
    s.speak()


if __name__ == '__main__':
    main()
