Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
>>> y = ['A','B','C','D','E','Z','A','B','C','D','E','Z','A','B','C','D','E','F','Z','A','B','C','D','E','Z','A','B','C','D','E','Z','A','B','C','D','E','Z','A','B','C','D','E','A','B','C','D','A','B','C','Z','A','B','C','A','B','C','A','B','C','Z','A','B','C','A','B','C','A','B','C','A','B','C','A','B']
>>> def combine(list1, list2):
    list1 = iter(list1)
    for item2 in list2:
        if item2 == list2[0]:
            item1 = next(list1)
        yield ''.join(map(str, (item1, item2)))

        
>>> list(combine(x,y))
['1A', '1B', '1C', '1D', '1E', '1Z', '2A', '2B', '2C', '2D', '2E', '2Z', '3A', '3B', '3C', '3D', '3E', '3F', '3Z', '4A', '4B', '4C', '4D', '4E', '4Z', '5A', '5B', '5C', '5D', '5E', '5Z', '6A', '6B', '6C', '6D', '6E', '6Z', '7A', '7B', '7C', '7D', '7E', '8A', '8B', '8C', '8D', '9A', '9B', '9C', '9Z', '10A', '10B', '10C', '11A', '11B', '11C', '12A', '12B', '12C', '12Z', '13A', '13B', '13C', '14A', '14B', '14C', '15A', '15B', '15C', '16A', '16B', '16C', '17A', '17B']
>>> 
