flowers = ['Rose', 'Jasmine', 'Orchid', 'Sunflower', 'Daisy']
for index in range(len(flowers)):
    print('Flowers {}: {}'.format((index+1), flowers[index]))
    
print('\n') #example using enumerate
for index, flower in enumerate(flowers, start=1):
    print('Flowers {}: {}'.format((index), flower))
  