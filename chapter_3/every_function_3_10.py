color_palette = ['blue', 'green', 'yellow', 'red', 'black', 'orange', 'purple', 'white', 'gray']
print('Color palette: ' + str(color_palette) + '\n')

color_palette.sort()
print('This is sorted color palette: ' + str(color_palette) + '\n')

print('This is length of color palette: ' + str(len(color_palette)) + '\n')

color_palette.reverse()
print('This is reversed color palette: ' + str(color_palette) + '\n')

print('This is temporary sorted color palette: ' + str(sorted(color_palette)) + '\n')

color_palette.sort(reverse=True)
print('This is  sorted backwards color palette: ' + str(color_palette) + '\n')

color_palette.append('brown')
print('This is color list with brown at the end added: ' + str(color_palette) + '\n')

color_palette.insert(0, 'navy blue')
print('This is  color list with navy blue at the beggining: ' + str(color_palette) + '\n')

color_palette[0] = 'navy blue color'
print('This is  color list with changed first iteam: ' + str(color_palette) + '\n')

del color_palette[0]
print('This is  list with deleted first iteam: ' + str(color_palette) + '\n')

color_palette.pop()
print('This is list with last item deleted: ' + str(color_palette) + '\n')

print('deleting: ' + color_palette.pop(1))
print('This is list with second item deleted: ' + str(color_palette) + '\n')
#use pop instead of del if u want to access to iteam you deleting

color_palette.remove('black')
print('This is list with black deleted: ' + str(color_palette) + '\n')
#use when u want to delete specified iteam, only first in list

print('my favourte color is ' + color_palette[2])

