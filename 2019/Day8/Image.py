from Point2D import Point2D

class Image:
    def __init__(self,image_data,width,height):
        self.width = width
        self.height = height
        self.layers = {}
        self.num_layers = 0

        layer_id = 1
        with open(image_data,'r') as img_data:
            while True:
                layer = Layer()
                for curr_row in range(0,self.height):
                    layer_row_pixels = img_data.read(self.width)
                    if not layer_row_pixels == "":
                        layer.add_row(curr_row,layer_row_pixels)
                    else:
                        return
                self.layers[layer_id] = layer
                self.num_layers = layer_id
                layer_id += 1

    def count_distr(self):
        for key,value in self.layers.items():
            zeros = value.pixel_colour_count('0')
            ones =value.pixel_colour_count('1')
            twos =value.pixel_colour_count('2') 
            print(f'{key},{zeros},{ones},{twos}')
    
    def part1(self):
        # find layer with fewest number of 0 and multiple number of 1s and 2s in this layer
        layer_most_zeros = min(self.layers.items(),key=lambda elem : elem[1].pixel_colour_count('0'))
        answer = layer_most_zeros[1].pixel_colour_count('1') * layer_most_zeros[1].pixel_colour_count('2') 
        return answer

    def part2(self):
        # build final_image
        final_image = {}
        for x in range(0,self.width):
            for y in range(0,self.height):
                for layer_no in range(1,self.num_layers+1):
                    # go through every layer until first non-transparent pixel found
                    # mark this as final_image pixel for this co-ord and move to next co-ord
                    if self.layers[layer_no].pixels[Point2D(x,y)] != '2':
                        final_image[Point2D(x,y)] = self.layers[layer_no].pixels[Point2D(x,y)]
                        break
        
        # display as a width * height grid, black as a *, white as a ' ' 
        for y in range(0,self.height):
            row = ''
            for x in range(0,self.width):
                if final_image[Point2D(x,y)] == '0':
                    row += ' '
                else:
                    row += '*'    
            print(row)
            
class Layer:
    def __init__(self):
        self.pixels = {}

    def add_row(self,row,row_pixels):
        for x in range(0,len(row_pixels)):
            self.pixels[Point2D(x,row)] = row_pixels[x]

    def pixel_colour_count(self,colour):
        return len(list(filter(lambda elem : elem[1] == colour,self.pixels.items())))
        