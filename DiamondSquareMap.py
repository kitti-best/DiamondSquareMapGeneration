import math
import random
import Color
from Setting import *


class DiamondSquareMap:
    def __init__(self, pos = (0, 0), w=5, h=5, min_corner_str=-5, max_corner_str=5, min_random_str=-2, max_random_str=2, map_full_size = None):
        self.pos = pos
        self.w = w
        self.h = h
        self.full_size = map_full_size
        if not map_full_size:
            self.full_size = (self.w, self.h)
        print(self.full_size)
        self.cell_w = round(self.full_size[0] / self.w)
        self.corner_strength = (min_corner_str, max_corner_str)
        self.random_strength = (min_random_str, max_random_str)
        self.__map_list = self.__create_blank_map()
        self.__perform_generation()
        self.__min_h, self.__max_h = self.get_min_max_height()
        self.map = self.__cache_map()

    def get_str_map(self):
        return '\n'.join([' '.join([str(e) for e in row]) for row in self.__map_list])

    def get_min_max_height(self):
        special_map = []
        for row in self.__map_list:
            special_map += row
        return min(special_map), max(special_map)

    def __create_blank_map(self):
        return [[0.] * self.w for _ in range(self.h)]

    def __perform_generation(self):
        step = self.w - 1
        self.__perform_corner()
        while step > 1:
            self.__perform_square(step)
            step = int(step / 2)
            self.__perform_diamond(step)

    def __perform_diamond(self, step):
        min_range, max_range = self.random_strength
        for i, y in enumerate(range(0, self.h, step)):
            start_x = step * (i % 2 == 0)
            for x in range(start_x, self.w, 2 * step):
                x1, y1 = x - step, y
                x2, y2 = (x + step) % self.w, y
                x3, y3 = x, (y + step) % self.h
                x4, y4 = x, y - step

                v1 = self.__map_list[y1][x1]
                v2 = self.__map_list[y2][x2]
                v3 = self.__map_list[y3][x3]
                v4 = self.__map_list[y4][x4]

                random_factor = (random.randint(min_range, max_range)) * step
                self.__map_list[y][x] = (v1 + v2 + v3 + v4) / 4 + random_factor

    def __perform_square(self, step):
        min_range, max_range = self.random_strength
        for y in range(step, self.h, step):
            for x in range(step, self.w, step):
                x1, y1 = x, y
                x2, y2 = x - step, y
                x3, y3 = x, y - step
                x4, y4 = x - step, y - step

                v1 = self.__map_list[y1][x1]
                v2 = self.__map_list[y2][x2]
                v3 = self.__map_list[y3][x3]
                v4 = self.__map_list[y4][x4]

                avg_x = (x1 + x2 + x3 + x4) // 4
                avg_y = (y1 + y2 + y3 + y4) // 4

                random_factor = (random.randint(min_range, max_range)) * step / 4
                self.__map_list[avg_y][avg_x] = (v1 + v2 + v3 + v4) / 4 + random_factor

    def __perform_corner(self):
        min_range, max_range = self.corner_strength
        tl = random.randint(min_range, max_range)
        tr = random.randint(min_range, max_range)
        bl = random.randint(min_range, max_range)
        br = random.randint(min_range, max_range)
        self.__map_list[0][0] = tl
        self.__map_list[0][self.w - 1] = tr
        self.__map_list[self.h - 1][0] = bl
        self.__map_list[self.h - 1][self.w - 1] = br
        mid_x, mid_y = self.w // 2, self.h // 2
        random_factor = (random.randint(min_range, max_range))
        self.__map_list[mid_y][mid_x] = (tl + tr + bl + br) / 4 + random_factor

    def __cache_map(self):
        map_img = pygame.Surface(self.full_size)
        height_range = (self.__max_h - self.__min_h)
        biome_range = [-0.1, -0.05, 0.0, 0.5]
        # print(self.__min_h, self.__max_h)

        for y, row in enumerate(self.__map_list):
            for x, height in enumerate(row):
                if height < height_range * biome_range[0]:
                    color = Color.AZURE
                elif height < height_range * biome_range[1]:
                    color = Color.DEEPSKYBLUE
                elif height < height_range * biome_range[2]:
                    color = Color.SANDSTONEIVORY
                elif height < height_range * biome_range[3]:
                    color = Color.HEAVENLYGREEN
                else:
                    color = Color.SLATEGRAY
                pygame.draw.rect(map_img, color, rect=(x * int(self.cell_w), y * int(self.cell_w), int(self.cell_w), int(self.cell_w)))

        return map_img

    def draw(self):
        SCREEN.blit(self.map, self.pos)

    def regenerate(self):
        self.__init__(self.pos, self.w, self.h, *self.corner_strength, *self.random_strength, self.full_size)
