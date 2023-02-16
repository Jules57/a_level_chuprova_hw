def main():
    def convert_size(int_size: str):
        sizes = {
            'xxs': {'Piggy State': '42',
                    'Germany': '36',
                    'USA': '8',
                    'France': '38',
                    'UK': '24'},
            'xs': {'Piggy State': '44',
                   'Germany': '38',
                   'USA': '10',
                   'France': '40',
                   'UK': '26'},
            's': {'Piggy State': '46',
                  'Germany': '40',
                  'USA': '12',
                  'France': '42',
                  'UK': '28'},
            'm': {'Piggy State': '48',
                  'Germany': '42',
                  'USA': '14',
                  'France': '44',
                  'UK': '30'},
            'l': {'Piggy State': '50',
                  'Germany': '44',
                  'USA': '16',
                  'France': '46',
                  'UK': '32'},
            'xl': {'Piggy State': '52',
                   'Germany': '46',
                   'USA': '18',
                   'France': '48',
                   'UK': '34'},
            'xxl': {'Piggy State': '54',
                    'Germany': '48',
                    'USA': '20',
                    'France': '50',
                    'UK': '36'},
            'xxxl': {'Piggy State': '56',
                     'Germany': '50',
                     'USA': '22',
                     'France': '52',
                     'UK': '38'}
        }
        if int_size in sizes.keys():
            return sizes[int_size]
        else:
            return 'Please, check the entered size.'

    size = input('Please, enter the international size for conversion: ')
    print(convert_size(size.lower()))


if __name__ == '__main__':
    main()
